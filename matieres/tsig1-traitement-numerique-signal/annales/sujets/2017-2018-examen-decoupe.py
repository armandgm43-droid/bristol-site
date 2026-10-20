#!/usr/bin/env python3
"""Découpe de l'examen TSIG1 (TS201) du 08/03/2018 (2e session) en images.

Source : sources/tsig1/td/recueil-td-2023.pdf, pages 19 et 20 (« SUJET 2017 »,
vectoriel). Rendu à 200 dpi avec pdftoppm, niveaux de gris, rognage automatique.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig1-traitement-numerique-signal/annales/sujets/2017-2018-examen-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig1/td/recueil-td-2023.pdf')
NOM = '2017-2018-examen'
DPI = 200
MARGE = 15

# (nom, page du PDF, boîte (x0, y0, x1, y1) en pixels à 200 dpi)
BOITES = [
    ('ex1',    19, (180, 935, 1480, 1300)),
    ('ex1-q4', 19, (280, 1320, 1480, 1363)),
    ('ex1-q5', 19, (280, 1364, 1480, 1445)),
    ('ex2',    19, (180, 1480, 1480, 1710)),
    ('ex3',    19, (180, 1735, 1480, 2030)),
    ('ex3-q3', 19, (280, 2050, 1480, 2108)),
    ('ex3-q4', 20, (280, 198, 1480, 238)),
    ('ex3-q5', 20, (280, 239, 1480, 282)),
    ('ex4',    20, (180, 310, 1480, 565)),
    ('ex4-q6', 20, (250, 588, 1480, 630)),
    ('ex4-q7', 20, (250, 631, 1480, 722)),
]


def rendre(page, tmp):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-gray', '-png', '-singlefile',
                    '-f', str(page), '-l', str(page), PDF, base], check=True)
    return Image.open(base + '.png').convert('L')


def rogner(im, seuil=200, min_px=1):
    """Rogne au contenu puis ajoute une marge blanche de MARGE px."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def enregistrer(im, chemin):
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: rendre(p, tmp) for p in sorted({b[1] for b in BOITES})}
        for nom, p, boite in BOITES:
            im = rogner(pages[p].crop(boite))
            chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
            enregistrer(im, chemin)
            print(chemin, im.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
