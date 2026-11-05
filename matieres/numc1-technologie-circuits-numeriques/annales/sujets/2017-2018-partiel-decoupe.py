#!/usr/bin/env python3
"""Découpe du partiel EN208 « Technologie des circuits intégrés numériques » du
10/01/2018 (S. Renaud) en images : énoncé commun, en-tête de chaque partie, une
image par question.

Source : sources/numc1/annales/2017-2018-partiel.pdf (deux photos de la copie
papier, 2 pages, sans annotation). Pages rendues à 200 dpi avec pdftoppm, en
niveaux de gris, fond aplani (division par une estimation de l'éclairage), ce qui
efface le gris des photos et l'ombre des bords. Les largeurs sont uniformisées à
la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/numc1-technologie-circuits-numeriques/annales/sujets/2017-2018-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/numc1/annales/2017-2018-partiel.pdf')
NOM = '2017-2018-partiel'
PAGES = (1, 2)
MARGE = 15
DPI = 200
ECART = 25
LARGEUR_MAX = 1400

X0, X1 = 295, 1345
BOITES = [
    ('intro',     [(1, (X0, 648, X1, 780))]),
    ('ex1',       [(1, (X0, 826, X1, 1830)), (2, (440, 292, 1150, 594))]),
    ('ex1-q1',    [(2, (X0, 613, X1, 714))]),
    ('ex1-q2-1',  [(2, (X0, 767, X1, 886))]),
    ('ex1-q2-2',  [(2, (X0, 888, X1, 944))]),
    ('ex1-q2-3',  [(2, (X0, 947, X1, 982))]),
    ('ex2',       [(2, (X0, 1084, X1, 1652))]),
    ('ex2-q1',    [(2, (X0, 1676, X1, 1709))]),
    ('ex2-q2',    [(2, (X0, 1708, X1, 1767))]),
    ('ex2-q3',    [(2, (X0, 1766, X1, 1795))]),
    ('ex2-q4',    [(2, (X0, 1795, X1, 1824))]),
]
BLANC = {}


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    im = Image.open(base + '.png').convert('L')
    g = np.asarray(im, float)
    fond = np.asarray(im.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)), float)
    a = np.clip((g / np.maximum(fond, 1) - 0.45) / (0.85 - 0.45), 0, 1)
    for x0, y0, x1, y1 in BLANC.get(num, []):
        a[y0:y1, x0:x1] = 1
    return Image.fromarray((a * 255).astype(np.uint8))


def rogner(im, seuil=160, min_px=2):
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def empiler(morceaux):
    if len(morceaux) == 1:
        return morceaux[0]
    w = max(m.width for m in morceaux)
    h = sum(m.height for m in morceaux) + ECART * (len(morceaux) - 1)
    out = Image.new('L', (w, h), 255)
    y = 0
    for m in morceaux:
        out.paste(m, (0, y))
        y += m.height + ECART
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in PAGES}
        if os.environ.get('PAGES_DIR'):
            for p, im in pages.items():
                im.save(os.path.join(os.environ['PAGES_DIR'], f'{NOM}-page{p}.png'))
        for nom, morceaux in BOITES:
            ims[nom] = empiler([rogner(pages[p].crop(b)) for p, b in morceaux])
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
