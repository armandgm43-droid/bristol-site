#!/usr/bin/env python3
"""Découpe du partiel EA205 (EANA1) du 24 novembre 2017 en images (une par
exercice et une par sous-question).

Source : sources/eana1/annales/2017-2018-partiel.pdf (photos d'un tirage papier,
2 pages). Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris ; éclairage
corrigé (division par le fond estimé) ; pages assez droites pour se passer de
rotation. Aucune annotation manuscrite. Les sous-questions a), b)… des exercices
I et II sont nommées exN-qa, exN-qb… ; les questions numérotées des exercices III
et IV, exN-q1, exN-q2… Largeurs uniformisées à la fin, PNG 16 couleurs.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana1-composants-circuits-commutation/annales/sujets/2017-2018-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy, opencv-python.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(RACINE, 'sources/eana1/annales/2017-2018-partiel.pdf')
NOM = '2017-2018-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Réglages par page : rot = rotation (degrés, sens trigonométrique), photo =
# correction d'éclairage d'une photo (au lieu du simple contraste d'un scan).
PAGES = {1: {'photo': True}, 2: {'photo': True}}

# (fichier, [(page, (x0, y0, x1, y1)[, masques]), ...]) ; coordonnées à 200 dpi
# dans la page redressée ; masques = rectangles blanchis (annotations manuscrites).
BOITES = [
    ('ex1',    [(1, (230, 600, 1400, 990))]),
    ('ex1-qa', [(1, (230, 1012, 1400, 1043))]),
    ('ex1-qb', [(1, (230, 1043, 1400, 1070))]),
    ('ex1-qc', [(1, (230, 1070, 1400, 1098))]),
    ('ex1-qd', [(1, (230, 1098, 1400, 1126))]),
    ('ex1-qe', [(1, (230, 1126, 1400, 1160))]),
    ('ex2',    [(1, (230, 1175, 1400, 1600))]),
    ('ex2-qa', [(1, (230, 1622, 1400, 1652))]),
    ('ex2-qb', [(1, (230, 1652, 1400, 1680))]),
    ('ex2-qc', [(1, (230, 1680, 1400, 1707))]),
    ('ex2-qd', [(1, (230, 1707, 1400, 1742))]),
    ('ex3',    [(2, (240, 310, 1350, 775))]),
    ('ex3-q1', [(2, (240, 790, 1350, 895))]),
    ('ex3-q2', [(2, (240, 905, 1350, 1040))]),
    ('ex4',    [(2, (240, 1050, 1350, 1465))]),
    ('ex4-q1', [(2, (240, 1480, 1350, 1535))]),
    ('ex4-q2', [(2, (240, 1537, 1350, 1590))]),
    ('ex4-q3', [(2, (240, 1595, 1350, 1680))]),
    ('ex4-q4', [(2, (240, 1684, 1350, 1735))]),
    ('ex4-q5', [(2, (240, 1738, 1350, 1790))]),
]



def charger_page(num, tmp):
    """Page num du PDF à DPI, niveaux de gris, contraste renforcé, redressée."""
    p = PAGES[num]
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', SOURCE, base], check=True)
    a = np.asarray(Image.open(base + '.png').convert('L'))
    if p.get('photo'):
        a = eclairage(a)
    else:
        g = np.clip((a.astype(float) - 40) / (225 - 40), 0, 1)   # fond du scan blanc, noirs francs
        a = (g * 255).astype(np.uint8)
    im = Image.fromarray(a)
    if p.get('rot'):
        im = im.rotate(p['rot'], resample=Image.BICUBIC, fillcolor=255)
    return im


def eclairage(a):
    """Photo : division par le fond estimé (dilatation + flou), puis contraste."""
    import cv2
    a = a.astype(np.float32)
    petit = cv2.resize(a, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    petit = cv2.dilate(petit, np.ones((21, 21), np.uint8))
    petit = cv2.GaussianBlur(petit, (0, 0), 6)
    fond = cv2.resize(petit, (a.shape[1], a.shape[0]), interpolation=cv2.INTER_LINEAR)
    n = np.clip(a / np.maximum(fond, 1) * 255, 0, 255)
    return np.clip((n - 70) / (215 - 70) * 255, 0, 255).astype(np.uint8)


def rogner(im, seuil=160, min_px=2):
    """Rogne au contenu puis ajoute une marge blanche."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def zone(page, b, masques=()):
    """Découpe la boîte b ; les masques (coordonnées de la page) sont blanchis."""
    im = page.copy()
    for m in masques:
        im.paste(255, m)
    return im.crop(b)


def empiler(ims):
    w = max(i.width for i in ims)
    out = Image.new('L', (w, sum(i.height for i in ims)), 255)
    y = 0
    for i in ims:
        out.paste(i, (0, y))
        y += i.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: charger_page(p, tmp) for p in PAGES}
        for nom, morceaux in BOITES:
            parts = [zone(pages[m[0]], m[1], m[2] if len(m) > 2 else ()) for m in morceaux]
            ims[nom] = rogner(empiler([rogner(x) for x in parts]) if len(parts) > 1 else parts[0])
    wmax = min(LARGEUR_MAX, max(i.width for i in ims.values()))
    for nom, im in ims.items():
        if im.width > LARGEUR_MAX:
            im = im.resize((LARGEUR_MAX, round(im.height * LARGEUR_MAX / im.width)), Image.LANCZOS)
        fond = Image.new('L', (wmax, im.height), 255)
        fond.paste(im, (0, 0))
        chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
        fond.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)
        print(chemin, fond.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
