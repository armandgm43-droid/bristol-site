#!/usr/bin/env python3
"""Découpe de l'épreuve d'optimisation EE8AU213 du 05/05/2022 (AUTO3) en images
(une par en-tête d'exercice et une par question).

Sources : sources/auto3/annales/2022-2023-partiel.pdf est une photo (2 pages, de
travers) du sujet imprimé ; sources/auto3/annales/2022-2023-test.pdf contient le
même sujet en PDF vectoriel (pages 1-2) suivi d'un début de corrigé (page 3). Les
images sont tirées du PDF vectoriel, plus net. Pages rendues à 200 dpi avec
pdftoppm (1654 x 2339 px), en niveaux de gris ; largeurs uniformisées à la fin.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/auto3-optimisation/annales/sujets/2022-2023-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/auto3/annales/2022-2023-test.pdf')
NOM = '2022-2023-partiel'
MARGE = 15
DPI = 200

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
# Plusieurs morceaux = empilés verticalement.
BOITES = [
    ('ex1',     [(1, (150, 638, 1500, 1368))]),
    ('ex1-q1',  [(1, (150, 1393, 1500, 1592))]),
    ('ex1-q2',  [(1, (150, 1594, 1500, 1632))]),
    ('ex1-q3',  [(1, (150, 1637, 1500, 1675))]),
    ('ex2',     [(2, (150, 140, 1500, 436))]),
    ('ex2-q1',  [(2, (150, 466, 1500, 540))]),
    ('ex2-q2',  [(2, (150, 543, 1500, 582))]),
    ('ex2-q3a', [(2, (150, 586, 1500, 676))]),
    ('ex2-q3b', [(2, (150, 677, 1500, 714))]),
    ('ex2-q3c', [(2, (150, 716, 1500, 765))]),
    ('ex2-q4',  [(2, (150, 815, 1500, 1042))]),
    ('ex2-q5',  [(2, (150, 1046, 1500, 1085))]),
    ('ex2-q6',  [(2, (150, 1089, 1500, 1128))]),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    g = np.clip((g - 40) / (225 - 40), 0, 1)   # fond blanc, noirs francs
    return Image.fromarray((g * 255).astype(np.uint8))


def rogner(im, seuil=160, min_px=2):
    """Rogne au contenu puis ajoute une marge blanche."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def empiler(ims):
    """Empile verticalement des morceaux (alignés à gauche)."""
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
        pages = {p: page(p, tmp) for p in sorted({p for _, m in BOITES for p, _ in m})}
        for nom, morceaux in BOITES:
            ims[nom] = empiler([rogner(pages[p].crop(b)) for p, b in morceaux])
    # Largeur uniformisée : toutes les images ont la largeur de la plus large
    # (plafonnée à 1400 px), marge blanche à droite.
    wmax = min(1400, max(i.width for i in ims.values()))
    for nom, im in ims.items():
        if im.width > 1400:
            im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
        fond = Image.new('L', (wmax, im.height), 255)
        fond.paste(im, (0, 0))
        chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
        fond.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)
        print(chemin, fond.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
