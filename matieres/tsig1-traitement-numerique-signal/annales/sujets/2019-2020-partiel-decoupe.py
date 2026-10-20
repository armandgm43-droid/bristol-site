#!/usr/bin/env python3
"""Découpe du partiel TSIG1 (TS201) du 11/12/2019 (1re session 2019-2020) en images.

Source : sources/tsig1/td/recueil-td-2023.pdf, pages 21 à 23 (vectoriel). Rendu à
200 dpi avec pdftoppm, niveaux de gris, rognage automatique (même échelle que les
autres sujets issus du recueil, p. ex. 2017-2018-examen).
L'exercice 3 (sans sous-question) s'étend sur deux pages : son texte (p. 22) et le
tableau des modules et diagrammes (p. 23) sont empilés dans une seule image.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig1-traitement-numerique-signal/annales/sujets/2019-2020-partiel-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig1/td/recueil-td-2023.pdf')
NOM = '2019-2020-partiel'
DPI = 200
MARGE = 15

# (nom, [(page du PDF, boîte (x0, y0, x1, y1) en pixels à 200 dpi), ...])
# plusieurs boîtes : morceaux empilés verticalement dans une même image
BOITES = [
    ('ex1',    [(21, (180, 870, 1480, 940))]),
    ('ex1-q1', [(21, (230, 960, 1480, 1205))]),
    ('ex1-q2', [(21, (230, 1206, 1480, 1265))]),
    ('ex1-q3', [(21, (230, 1280, 1480, 1380))]),
    ('ex2',    [(21, (180, 1425, 1480, 2030))]),
    ('ex2-q1', [(21, (230, 2040, 1480, 2110))]),
    ('ex2-q2', [(22, (230, 190, 1480, 238))]),
    ('ex2-q3', [(22, (230, 239, 1480, 295))]),
    ('ex3',    [(22, (180, 310, 1480, 905)), (23, (170, 190, 1490, 1920))]),
    ('ex4',    [(22, (180, 1000, 1480, 1055))]),
    ('ex4-q1', [(22, (230, 1058, 1480, 1210))]),
    ('ex4-q2', [(22, (230, 1212, 1480, 1315))]),
]


def rendre(page, tmp):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-gray', '-png', '-singlefile',
                    '-f', str(page), '-l', str(page), PDF, base], check=True)
    return Image.open(base + '.png').convert('L')


def serrer(im, seuil=200, min_px=1):
    """Rogne au contenu (pixels plus sombres que le seuil)."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    return im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))


def empiler(morceaux, ecart=30):
    """Empile des morceaux rognés (alignés à gauche) et ajoute la marge blanche."""
    larg = max(m.width for m in morceaux)
    haut = sum(m.height for m in morceaux) + ecart * (len(morceaux) - 1)
    out = Image.new('L', (larg + 2 * MARGE, haut + 2 * MARGE), 255)
    y = MARGE
    for m in morceaux:
        out.paste(m, (MARGE, y))
        y += m.height + ecart
    return out


def enregistrer(im, chemin):
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: rendre(p, tmp) for p in sorted({p for _, l in BOITES for p, _ in l})}
        for nom, liste in BOITES:
            im = empiler([serrer(pages[p].crop(b)) for p, b in liste])
            chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
            enregistrer(im, chemin)
            print(chemin, im.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
