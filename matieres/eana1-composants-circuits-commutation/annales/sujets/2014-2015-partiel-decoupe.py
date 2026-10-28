#!/usr/bin/env python3
"""Découpe de l'examen de CCC (EANA1) du 12 novembre 2014 en images (une par
exercice et une par question).

Source : sources/eana1/annales/2014-2015-partiel.pdf (photos d'un tirage papier,
2 pages). Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris ; éclairage
corrigé (division par le fond estimé), page redressée (rotation), deux lettres
manuscrites (« a », « b ») effacées du schéma de l'exercice II. Largeurs
uniformisées à la fin (marge blanche à droite), PNG 16 couleurs.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana1-composants-circuits-commutation/annales/sujets/2014-2015-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy, opencv-python.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(RACINE, 'sources/eana1/annales/2014-2015-partiel.pdf')
NOM = '2014-2015-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Réglages par page : rot = rotation (degrés, sens trigonométrique), photo =
# correction d'éclairage d'une photo (au lieu du simple contraste d'un scan).
PAGES = {1: {'photo': True, 'rot': -1.0}, 2: {'photo': True, 'rot': -0.4}}

# (fichier, [(page, (x0, y0, x1, y1)[, masques]), ...]) ; coordonnées à 200 dpi
# dans la page redressée ; masques = rectangles blanchis (annotations manuscrites).
BOITES = [
    ('ex1',    [(1, (370, 620, 1420, 1435))]),
    ('ex1-q1', [(1, (370, 1455, 1340, 1496))]),
    ('ex1-q2', [(1, (370, 1508, 1340, 1680))]),
    ('ex1-q3', [(1, (370, 1692, 1340, 1730))]),
    ('ex2',    [(2, (330, 330, 1420, 990), [(992, 660, 1015, 690), (1000, 810, 1025, 840)])]),
    ('ex2-q1', [(2, (330, 998, 1420, 1056))]),
    ('ex2-q2', [(2, (330, 1082, 1420, 1144))]),
    ('ex2-q3', [(2, (330, 1164, 1420, 1226))]),
    ('ex2-q4', [(2, (330, 1247, 1420, 1280))]),
    ('ex2-q5', [(2, (330, 1300, 1420, 1334))]),
    ('ex2-q6', [(2, (330, 1356, 1420, 1414))]),
    ('ex3',    [(2, (330, 1440, 1340, 1780))]),
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
