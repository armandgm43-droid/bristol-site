#!/usr/bin/env python3
"""Découpe de l'épreuve d'optimisation EE7AU213 du 20/12/2023 (AUTO3) en images
(une par en-tête d'exercice et une par question).

Source : sources/auto3/annales/2023-2024-test.pdf (12 pages A4, PDF vectoriel) :
sujet à compléter pages 1-7 (cadres de réponse vides, non repris), corrigé pages
8-12 (non découpé). L'en-tête de l'exercice 2 empile le texte (page 3) et la figure
des courbes iso-critères (page 4). Pages rendues à 200 dpi avec pdftoppm
(1654 x 2339 px), en niveaux de gris ; largeurs uniformisées à la fin.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/auto3-optimisation/annales/sujets/2023-2024-test-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/auto3/annales/2023-2024-test.pdf')
NOM = '2023-2024-test'
MARGE = 15
DPI = 200

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
# Plusieurs morceaux = empilés verticalement. Les cadres de réponse sont exclus.
BOITES = [
    ('ex1',     [(1, (150, 635, 1500, 1640))]),
    ('ex1-q1a', [(1, (150, 1685, 1500, 2002))]),
    ('ex1-q1b', [(1, (150, 2012, 1500, 2054))]),
    ('ex1-q2a', [(2, (150, 924, 1500, 1210))]),
    ('ex1-q2b', [(2, (150, 1222, 1500, 1264))]),
    ('ex1-q3a', [(3, (150, 150, 1500, 410))]),
    ('ex1-q3b', [(3, (150, 424, 1500, 460))]),
    ('ex2',     [(3, (150, 1383, 1500, 1810)), (4, (150, 180, 1500, 1050))]),
    ('ex2-q1',  [(3, (150, 1880, 1500, 1950))]),
    ('ex2-q2',  [(5, (150, 150, 1500, 186))]),
    ('ex2-q3',  [(5, (150, 706, 1500, 884))]),
    ('ex2-q4',  [(5, (150, 1484, 1500, 1782))]),
    ('ex2-q5',  [(5, (150, 1786, 1500, 1854))]),
    ('ex2-q6',  [(5, (150, 1858, 1500, 1893))]),
    ('ex2-q7',  [(6, (150, 151, 1500, 220))]),
    ('ex2-q8',  [(6, (150, 1027, 1500, 1060))]),
    ('ex2-q9',  [(7, (150, 151, 1500, 187))]),
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
