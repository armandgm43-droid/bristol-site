#!/usr/bin/env python3
"""Découpe de l'épreuve d'optimisation EE8AU213 du 19/05/2022 (AUTO3) en images
(une par en-tête d'exercice et une par question).

Source : sources/auto3/annales/2021-2022-partiel.pdf (sujet seul, 2 pages A4, PDF
vectoriel). Le fichier 2021-2022-test.pdf contient le même sujet (pages 1-2, rendu
identique) suivi d'un corrigé (pages 3-4), non découpé. Pages rendues à 200 dpi
avec pdftoppm (1654 x 2339 px), en niveaux de gris ; largeurs uniformisées à la fin.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/auto3-optimisation/annales/sujets/2021-2022-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/auto3/annales/2021-2022-partiel.pdf')
NOM = '2021-2022-partiel'
MARGE = 15
DPI = 200

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
# Plusieurs morceaux = empilés verticalement.
BOITES = [
    ('ex1',    [(1, (150, 655, 1500, 912))]),
    ('ex1-q1', [(1, (150, 944, 1500, 984))]),
    ('ex1-q2', [(1, (150, 993, 1500, 1033))]),
    ('ex2',    [(1, (150, 1112, 1500, 1845))]),
    ('ex2-q1', [(1, (150, 1882, 1500, 1956))]),
    ('ex2-q2', [(1, (150, 1964, 1500, 2004))]),
    ('ex2-q3', [(1, (150, 2011, 1500, 2052))]),
    ('ex3',    [(2, (150, 140, 1500, 1485))]),
    ('ex3-q1', [(2, (150, 1608, 1500, 1714))]),
    ('ex3-q2', [(2, (150, 1716, 1500, 1755))]),
    ('ex3-q3', [(2, (150, 1757, 1500, 1827))]),
    ('ex3-q4', [(2, (150, 1828, 1500, 1871))]),
    ('ex3-q5', [(2, (150, 1873, 1500, 1945))]),
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
