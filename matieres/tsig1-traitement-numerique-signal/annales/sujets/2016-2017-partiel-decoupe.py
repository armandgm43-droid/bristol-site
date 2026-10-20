#!/usr/bin/env python3
"""Découpe du partiel TSIG1 (TS201) du 6/12/2016 en images (une par question).

Deux versions du sujet existent : le scan sources/tsig1/annales/2016-2017-partiel.pdf
et la reproduction vectorielle du recueil de TD (« SUJET 2016 »,
sources/tsig1/td/recueil-td-2023.pdf, pages 16 à 18 du PDF). Le contenu est
identique ; on découpe dans le recueil, plus net. Pages rendues à 200 dpi avec
pdftoppm (1654 x 2339 px), passées en niveaux de gris.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig1-traitement-numerique-signal/annales/sujets/2016-2017-partiel-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig1/td/recueil-td-2023.pdf')
NOM = '2016-2017-partiel'
MARGE = 15
DPI = 200

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
# Plusieurs morceaux = empilés verticalement (énoncé à cheval sur deux pages).
BOITES = [
    ('ex1',    [(16, (180, 895, 1560, 1060))]),
    ('ex1-q1', [(16, (180, 1060, 1560, 1165))]),
    ('ex1-q2', [(16, (180, 1190, 1560, 1295))]),
    ('ex2',    [(16, (180, 1320, 1560, 1556))]),
    ('ex2-q3', [(16, (180, 1590, 1560, 1645))]),   # seule question, numérotée « 3. »
    ('ex3',    [(16, (180, 1680, 1560, 2120)), (17, (180, 195, 1560, 470))]),
    ('ex3-q1', [(17, (180, 515, 1560, 572))]),
    ('ex3-q2', [(17, (180, 574, 1560, 705))]),
    ('ex4',    [(17, (150, 740, 1560, 1300))]),
    ('ex4-q1', [(17, (150, 1302, 1560, 1400))]),
    ('ex4-q2', [(17, (150, 1404, 1560, 1484))]),
    ('ex4-q3', [(17, (150, 1485, 1560, 1583))]),
    ('ex4-q4', [(17, (150, 1584, 1560, 1621))]),
    ('ex4-q5', [(17, (150, 1622, 1560, 1662))]),
    ('ex5',    [(17, (150, 1695, 1560, 1820))]),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    g = np.clip((g - 20) / (245 - 20), 0, 1)   # fond bien blanc, noirs francs
    return Image.fromarray((g * 255).astype(np.uint8))


def rogner(im, seuil=215, min_px=1):
    """Rogne au contenu (schémas bleu clair compris) puis ajoute une marge blanche."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def empiler(ims):
    w = max(i.width for i in ims)
    out = Image.new('L', (w, sum(i.height for i in ims)), 255)
    y = 0
    for i in ims:
        out.paste(i, (0, y)); y += i.height
    return out


def enregistrer(im, chemin):
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in (16, 17)}
        for nom, morceaux in BOITES:
            ims = [rogner(pages[p].crop(b)) for p, b in morceaux]
            im = empiler(ims) if len(ims) > 1 else ims[0]
            chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
            enregistrer(im, chemin)
            print(chemin, im.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
