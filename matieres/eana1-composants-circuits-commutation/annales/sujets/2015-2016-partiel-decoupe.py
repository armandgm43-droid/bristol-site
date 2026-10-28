#!/usr/bin/env python3
"""Découpe du partiel EA205 (EANA1) du 13 décembre 2015 en images (une par
exercice et une par question).

Source : sources/eana1/annales/2015-2016-partiel.pdf (scan, 3 pages). Pages
rendues à 200 dpi avec pdftoppm, en niveaux de gris, contraste renforcé. Les
annotations manuscrites d'un étudiant (table de vérité, niveaux logiques « 0 »
et « 1 » sur le schéma, flèche au-dessus de C1) sont effacées (rectangles
blanchis). L'en-tête de l'exercice II, à cheval sur les pages 2 et 3, est
recomposé en une image. Largeurs uniformisées à la fin, PNG 16 couleurs.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana1-composants-circuits-commutation/annales/sujets/2015-2016-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(RACINE, 'sources/eana1/annales/2015-2016-partiel.pdf')
NOM = '2015-2016-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Réglages par page : rot = rotation (degrés, sens trigonométrique), photo =
# correction d'éclairage d'une photo (au lieu du simple contraste d'un scan).
PAGES = {1: {}, 2: {}, 3: {}}

# Annotations manuscrites de la page 2 (coordonnées à 200 dpi).
MASQUES_P2 = [
    (1180, 440, 1400, 625),   # table de vérité à droite des questions 2 c, d et 3
    (900, 700, 1015, 733),    # flèche au-dessus de « C1 »
    (928, 760, 950, 787), (988, 736, 1020, 778),   # « 1 » de part et d'autre de C1
    (170, 968, 200, 995),     # « 1 » à l'entrée de la porte I
    (430, 968, 458, 1003),    # « 0 » à la sortie de la porte I
    (930, 1050, 958, 1080),   # « 0 » à la sortie de la porte II
    (752, 1110, 780, 1140),   # « 1 » sur Vc
    (1348, 1003, 1380, 1029), # « 1 » à la sortie de la porte III
]

# (fichier, [(page, (x0, y0, x1, y1)[, masques]), ...]) ; plusieurs morceaux
# sont empilés verticalement.
BOITES = [
    ('ex1',    [(1, (150, 830, 1500, 1940))]),
    ('ex1-q1', [(1, (150, 1975, 1500, 2020))]),
    ('ex1-q2', [(2, (150, 288, 1500, 525), MASQUES_P2)]),
    ('ex1-q3', [(2, (150, 557, 1150, 598))]),
    ('ex2',    [(2, (140, 672, 1500, 1890), MASQUES_P2), (3, (150, 285, 1500, 430))]),
    ('ex2-q1', [(3, (150, 503, 1500, 578))]),
    ('ex2-q2', [(3, (150, 654, 1500, 778))]),
    ('ex2-q3', [(3, (150, 848, 1500, 1040))]),
    ('ex2-q4', [(3, (150, 1110, 1500, 1266))]),
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
