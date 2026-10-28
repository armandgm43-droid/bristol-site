#!/usr/bin/env python3
"""Découpe du partiel de TP TS202 (TSIG2) 2016-2017 en images (une par question).

Source : sources/tsig2/annales/2016-2017-partiel.pdf (PDF LaTeX vectoriel, 2 pages au
format lettre US). Pages rendues à 200 dpi avec pdftoppm (1700 x 2200 px), en niveaux
de gris. Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig2-tp-signal/annales/sujets/2016-2017-partiel-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig2/annales/2016-2017-partiel.pdf')
NOM = '2016-2017-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('ex1',    [(1, (220, 650, 1480, 694))]),
    ('ex1-q1', [(1, (220, 724, 1480, 806))]),
    ('ex1-q2', [(1, (220, 854, 1480, 1354))]),
    ('ex1-q3', [(1, (220, 1419, 1480, 1547))]),
    ('ex1-q4', [(1, (220, 1551, 1480, 1709))]),
    ('ex2',    [(1, (220, 1755, 1480, 1805))]),
    ('ex2-p1', [(1, (220, 1829, 1480, 2117))]),
    ('ex2-p2', [(2, (220, 222, 1480, 263))]),
    ('ex2-q1', [(2, (220, 276, 1480, 354))]),
    ('ex2-q2', [(2, (220, 361, 1480, 397))]),
    ('ex2-q3', [(2, (220, 409, 1480, 451))]),
    ('ex2-q4', [(2, (220, 458, 1480, 653))]),
    ('ex2-q5', [(2, (220, 660, 1480, 701))]),
    ('ex2-q6', [(2, (220, 707, 1480, 749))]),
    ('ex2-q7', [(2, (220, 756, 1480, 797))]),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    return Image.open(base + '.png').convert('L')


def rogner(im, seuil=160, min_px=2):
    """Rogne au contenu puis ajoute une marge blanche."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in (1, 2)}
        for nom, morceaux in BOITES:
            (p, b), = morceaux
            ims[nom] = rogner(pages[p].crop(b))
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
