#!/usr/bin/env python3
"""Découpe du partiel EA210 « Circuits HF et oscillateurs » du 16/12/2022 en images
(une par question) : exercice I (questions générales) et exercice II (amplificateur à
transimpédance, localisation du pôle dominant).

Sources : sources/eana3/annales/2022-2023-partiel-circuits-hf-oscillateurs-p1.jpg et -p2.jpg
(photos 4032 x 3024 px, page tournée de 90°). Chaque photo est tournée d'un quart de tour
dans le sens horaire, redressée (rotation de quelques dixièmes de degré), réduite de moitié
(environ 170 dpi pour la page), passée en niveaux de gris ; l'éclairage inégal est corrigé
en divisant par le fond, estimé par un filtre maximum sur l'image réduite. Une image peut
être formée de plusieurs morceaux empilés verticalement (question II.1 : énoncé puis
figure 2). Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2022-2023-partiel-circuits-hf-decoupe.py [racine] [dossier_sortie]
Dépendances : Pillow, numpy.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
JPG = os.path.join(RACINE, 'sources/eana3/annales/2022-2023-partiel-circuits-hf-oscillateurs-p{}.jpg')
NOM = '2022-2023-partiel-circuits-hf'
MARGE = 15
REDRESSEMENT = {1: 0.8, 2: 0.7}  # rotation (degrés, sens trigonométrique) après le quart de tour
NOIR, BLANC = 0.35, 0.80          # niveaux (rapport au fond) ramenés au noir et au blanc
GAMMA = 1.4                       # renforce les gris pâles (haut de la page 1, peu éclairé)

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans l'image tournée, redressée
# et réduite de moitié (1512 x 2016 px).
BOITES = [
    ('ex1',     [(1, (160, 455, 1335, 497))]),
    ('ex1-q1',  [(1, (170, 503, 1330, 570))]),
    ('ex1-q2',  [(1, (170, 578, 1330, 614))]),
    ('ex1-q3',  [(1, (165, 625, 1330, 661))]),
    ('ex1-q4',  [(1, (165, 671, 1330, 707))]),
    ('ex1-q5',  [(1, (165, 715, 1330, 751))]),
    ('ex1-q6',  [(1, (160, 764, 1340, 861))]),
    ('ex1-q7',  [(1, (155, 877, 1340, 949))]),
    ('ex1-q8',  [(1, (150, 957, 1345, 1022))]),
    ('ex2',     [(1, (135, 1048, 1345, 1542))]),
    ('ex2-q1',  [(1, (115, 1563, 1058, 1634)), (1, (1100, 1563, 1312, 1866))]),
    ('ex2-q2',  [(1, (112, 1637, 1058, 1703))]),
    ('ex2-q3',  [(1, (110, 1704, 1062, 1776))]),
    ('ex2-q4',  [(1, (110, 1776, 1062, 1842))]),
    ('ex2-q5',  [(1, (110, 1843, 1062, 1884))]),
    ('ex2-q6',  [(2, (120, 82, 1390, 292))]),
    ('ex2-q7',  [(2, (115, 318, 1390, 470))]),
    ('ex2-q8',  [(2, (110, 497, 1390, 532))]),
    ('ex2-q9',  [(2, (110, 532, 1390, 567))]),
    ('ex2-q10', [(2, (110, 567, 1395, 728))]),
    ('ex2-q11', [(2, (110, 752, 1400, 1000))]),
]


def page(num):
    im = Image.open(JPG.format(num)).convert('L').rotate(-90, expand=True)
    im = im.rotate(REDRESSEMENT[num], resample=Image.BICUBIC, fillcolor=255)
    im = im.resize((im.width // 2, im.height // 2), Image.LANCZOS)
    petit = im.resize((im.width // 8, im.height // 8), Image.BILINEAR)
    fond = petit.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1))
    fond = np.asarray(fond.resize(im.size, Image.BILINEAR), float)
    g = np.asarray(im, float) / np.maximum(fond, 1)
    g = np.clip((g - NOIR) / (BLANC - NOIR), 0, 1) ** GAMMA
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


def empiler(morceaux):
    """Empile verticalement des morceaux rognés, alignés à gauche."""
    if len(morceaux) == 1:
        return morceaux[0]
    out = Image.new('L', (max(m.width for m in morceaux), sum(m.height for m in morceaux)), 255)
    y = 0
    for m in morceaux:
        out.paste(m, (0, y))
        y += m.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    pages = {p: page(p) for p in sorted({p for _, ms in BOITES for p, _ in ms})}
    ims = {nom: empiler([rogner(pages[p].crop(b)) for p, b in morceaux]) for nom, morceaux in BOITES}
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
