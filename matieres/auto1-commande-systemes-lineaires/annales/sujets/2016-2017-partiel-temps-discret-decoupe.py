#!/usr/bin/env python3
"""Découpe du partiel AU205 « Commande à temps discret » du 22 mars 2017 (session 1)
en images (énoncé commun avec le schéma fonctionnel, en-têtes de partie, une image par
question ou sous-question).

Source : sources/auto1/annales/2016-2017-partiel-temps-discret.pdf (scan, 2 pages).
Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris, puis redressées (ROTATION).
Annotation manuscrite d'un étudiant (cadre « ωu = 20, Mφ = 60° » à droite de G(p)) :
effacée (zones EFFACER). Le tampon et les marques de la page 2 sont hors des cadres.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/auto1-commande-systemes-lineaires/annales/sujets/2016-2017-partiel-temps-discret-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/auto1/annales/2016-2017-partiel-temps-discret.pdf')
NOM = '2016-2017-partiel-temps-discret'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Zones blanchies avant découpe : (page, (x0, y0, x1, y1)) à 200 dpi.
EFFACER = [
    (1, (1255, 1212, 1520, 1398)),  # cadre manuscrit « ωu = 20 / Mφ = 60° »
]

# Redressement des pages (scan de travers), en degrés, appliqué après effacement.
ROTATION = {1: 0.8, 2: -1.0}

# Restes du cadre manuscrit, blanchis sur la page redressée.
EFFACER_APRES = [
    (1, (1385, 1165, 1520, 1215)),  # trait manuscrit à droite de la boucle de retour
    (1, (1240, 1350, 1520, 1400)),  # bas du cadre manuscrit
]

# (fichier, page, (x0, y0, x1, y1)) ; coordonnées à 200 dpi, sur la page redressée.
BOITES = [
    ('enonce',  1, (125, 688, 1500, 1562)),
    ('ex1',     1, (125, 1604, 1500, 1638)),
    ('ex1-q1',  1, (125, 1638, 1500, 1764)),
    ('ex1-q2',  1, (125, 1792, 1500, 1838)),
    ('ex1-q2a', 1, (125, 1838, 1500, 1876)),
    ('ex1-q2b', 1, (125, 1876, 1545, 1968)),
    ('ex1-q2c', 1, (125, 1968, 1500, 2010)),
    ('ex1-q3',  1, (125, 2040, 1500, 2086)),
    ('ex1-q4',  1, (125, 2118, 1500, 2168)),
    ('ex2',     2, (140, 140, 1530, 180)),
    ('ex2-q5',  2, (140, 182, 1530, 822)),
    ('ex2-q5a', 2, (140, 855, 1530, 898)),
    ('ex2-q5b', 2, (140, 898, 1530, 940)),
    ('ex2-q5c', 2, (140, 940, 1530, 1020)),
    ('ex2-q6',  2, (140, 1060, 1530, 1272)),
    ('ex2-q6a', 2, (140, 1274, 1530, 1319)),
    ('ex2-q6b', 2, (140, 1319, 1530, 1399)),
    ('ex2-q6c', 2, (140, 1399, 1530, 1488)),
    ('ex2-q6d', 2, (140, 1488, 1530, 1566)),
    ('ex2-q7',  2, (140, 1596, 1530, 1642)),
    ('ex2-q8',  2, (140, 1677, 1530, 1724)),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    g = np.clip((g - 40) / (225 - 40), 0, 1)   # fond du scan blanc, noirs francs
    im = Image.fromarray((g * 255).astype(np.uint8))
    d = ImageDraw.Draw(im)
    for p, b in EFFACER:
        if p == num:
            d.rectangle(b, fill=255)
    if ROTATION.get(num):
        im = im.rotate(ROTATION[num], resample=Image.BICUBIC, fillcolor=255)
        d = ImageDraw.Draw(im)
    for p, b in EFFACER_APRES:
        if p == num:
            d.rectangle(b, fill=255)
    return im


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
        pages = {p: page(p, tmp) for p in sorted({b[1] for b in BOITES})}
        for nom, p, b in BOITES:
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
