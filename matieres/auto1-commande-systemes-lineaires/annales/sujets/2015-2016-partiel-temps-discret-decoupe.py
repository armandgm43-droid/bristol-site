#!/usr/bin/env python3
"""Découpe du partiel AU205 « Commande à temps discret » du 9 mars 2016 en images
(énoncé commun, en-têtes de partie, une image par question ou sous-question).

Source : sources/auto1/annales/2015-2016-partiel-temps-discret.pdf (scan, 1 page).
Page rendue à 200 dpi avec pdftoppm (1700 x 2338 px), en niveaux de gris.
Annotations manuscrites d'un étudiant (à droite des questions 2.3 et 2.4, et deux
petites marques au crayon) : hors des cadres ou effacées (zones EFFACER).
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/auto1-commande-systemes-lineaires/annales/sujets/2015-2016-partiel-temps-discret-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/auto1/annales/2015-2016-partiel-temps-discret.pdf')
NOM = '2015-2016-partiel-temps-discret'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Zones blanchies avant découpe : (page, (x0, y0, x1, y1)) à 200 dpi.
EFFACER = [
    (1, (0, 0, 14, 2338)),          # bord noir du scan
    (1, (255, 1225, 345, 1305)),    # marque au crayon à gauche de la formule de G0(w)
    (1, (262, 1036, 300, 1070)),    # point au crayon après « 1ère Partie »
    (1, (1555, 958, 1600, 992)),    # marque au crayon en fin d'énoncé
    (1, (95, 1540, 185, 1574)),     # marque au crayon devant « au cahier des charges »
    (1, (1340, 2030, 1700, 2338)),  # annotations manuscrites (x = 10^(XdB/10)…)
]

# (fichier, page, (x0, y0, x1, y1)) ; coordonnées à 200 dpi.
BOITES = [
    ('enonce',  1, (80, 588, 1600, 990)),
    ('ex1',     1, (80, 1036, 1600, 1112)),
    ('ex1-q1',  1, (80, 1112, 1600, 1318)),
    ('ex1-q1a', 1, (80, 1322, 1600, 1368)),
    ('ex1-q1b', 1, (80, 1370, 1600, 1450)),
    ('ex1-q1c', 1, (80, 1450, 1600, 1496)),
    ('ex1-q1d', 1, (80, 1496, 1600, 1575)),
    ('ex1-q2',  1, (80, 1575, 1600, 1616)),
    ('ex1-q3',  1, (80, 1617, 1600, 1658)),
    ('ex2',     1, (80, 1695, 1600, 1730)),
    ('ex2-q1',  1, (80, 1730, 1600, 1848)),
    ('ex2-q2',  1, (80, 1848, 1600, 1890)),
    ('ex2-q2a', 1, (80, 1890, 1600, 1932)),
    ('ex2-q2b', 1, (80, 1932, 1600, 1978)),
    ('ex2-q2c', 1, (80, 1980, 1600, 2024)),
    ('ex2-q3',  1, (80, 2058, 1340, 2100)),
    ('ex2-q4',  1, (80, 2100, 1340, 2142)),
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
