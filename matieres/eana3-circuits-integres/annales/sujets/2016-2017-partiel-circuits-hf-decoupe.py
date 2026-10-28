#!/usr/bin/env python3
"""Découpe du partiel EA210 « Circuits HF et oscillateurs » du 7/11/2016 en images
(une par question) : exercice I (questions générales sur les circuits intégrés HF)
et exercice II (charge active à paire croisée, résistance négative).

Source : sources/eana3/annales/2016-2017-partiel-circuits-hf-oscillateurs.pdf (scan,
2 pages). Pages rendues à 200 dpi avec pdftoppm (1700 x 2339 px), en niveaux de gris.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2016-2017-partiel-circuits-hf-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana3/annales/2016-2017-partiel-circuits-hf-oscillateurs.pdf')
NOM = '2016-2017-partiel-circuits-hf'
MARGE = 15
DPI = 200

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('ex1',     [(1, (140, 765, 1600, 828))]),
    ('ex1-q1',  [(1, (140, 832, 1290, 870))]),
    ('ex1-q2',  [(1, (140, 880, 1600, 930))]),
    ('ex1-q3',  [(1, (140, 940, 1500, 992))]),
    ('ex1-q4',  [(1, (140, 1002, 1600, 1053))]),
    ('ex1-q5',  [(1, (140, 1068, 1500, 1146))]),
    ('ex1-q6',  [(1, (140, 1157, 1600, 1240))]),
    ('ex2',     [(1, (110, 1325, 1600, 2155))]),
    ('ex2-q1',  [(2, (110, 200, 1600, 290))]),
    ('ex2-q2',  [(2, (110, 296, 1600, 417))]),
    ('ex2-q3',  [(2, (110, 425, 1600, 510))]),
    ('ex2-q4',  [(2, (110, 522, 1600, 606))]),
    ('ex2-q5',  [(2, (110, 615, 1600, 695))]),
    ('ex2-q6',  [(2, (110, 709, 1600, 796))]),
    ('ex2-q7',  [(2, (110, 806, 1600, 890))]),
    ('ex2-q8',  [(2, (110, 900, 1600, 952))]),
    ('ex2-q9',  [(2, (110, 963, 1600, 1058))]),
    ('ex2-q10', [(2, (110, 1080, 1600, 1124))]),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    g = np.clip((g - 40) / (225 - 40), 0, 1)   # fond du scan blanc, noirs francs
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


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in (1, 2)}
        for nom, morceaux in BOITES:
            (p, b), = morceaux
            ims[nom] = rogner(pages[p].crop(b))
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
