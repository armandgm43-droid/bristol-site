#!/usr/bin/env python3
"""Découpe du partiel EA211 « Contre-réaction » du 17/11/2017 (amplificateur large
bande, F. Rivet) en images : énoncé commun, en-tête de chaque partie, une image par
question.

Source : sources/eana3/annales/2017-2018-partiel-contre-reaction.pdf (photo d'une
feuille, 2 pages). Pages rendues à 200 dpi avec pdftoppm (1654 x 2339 px), en niveaux
de gris ; le fond inégal de la photo est corrigé (division par le fond estimé, flou
d'un filtre max). Les annotations d'un étudiant (soulignement ondulé de « sauf pour
M3 ... transistors », cercle autour de M3 sur la figure 1) sont effacées : le stylo,
gris, est blanchi là où il ne touche pas un trait imprimé noir.
Une image peut assembler plusieurs morceaux (empilés verticalement). Les largeurs
sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2017-2018-partiel-contre-reaction-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana3/annales/2017-2018-partiel-contre-reaction.pdf')
NOM = '2017-2018-partiel-contre-reaction'
PAGES = (1, 2)
MARGE = 15
DPI = 200
ECART = 25        # espace entre deux morceaux empilés
LARGEUR_MAX = 1400

X0, X1 = 250, 1400
# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('intro',   [(1, (X0, 628, X1, 1505))]),
    ('ex1',     [(1, (X0, 1555, X1, 1602))]),
    ('ex1-q1',  [(1, (X0, 1604, X1, 1752))]),
    ('ex1-q2',  [(2, (X0, 300, X1, 475))]),
    ('ex1-q3',  [(2, (X0, 476, X1, 518))]),
    ('ex1-q4',  [(2, (X0, 519, X1, 560))]),
    ('ex1-q5',  [(2, (X0, 562, X1, 600))]),
    ('ex1-q6',  [(2, (X0, 602, X1, 767))]),
    ('ex2',     [(2, (X0, 783, X1, 831))]),
    ('ex2-q7',  [(2, (X0, 837, X1, 992))]),
    ('ex2-q8',  [(2, (X0, 996, X1, 1033))]),
    ('ex2-q9',  [(2, (X0, 1036, X1, 1112))]),
    ('ex2-q10', [(2, (X0, 1114, X1, 1151))]),
    ('ex2-q11', [(2, (X0, 1153, X1, 1264))]),
]

# Annotations au stylo (zones traitées par effacer_crayon), page 1.
CRAYON = {1: [(400, 978, 1400, 1003), (300, 1024, 450, 1042), (835, 1145, 1000, 1268)]}


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    im = Image.open(base + '.png').convert('L')
    g = np.asarray(im, float)
    fond = np.asarray(im.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(30)), float)
    g = np.clip((g / np.maximum(fond, 1) - 0.35) / (0.85 - 0.35), 0, 1) * 255
    for b in CRAYON.get(num, []):
        effacer_crayon(g, b, gris=60, noir=40)
    return Image.fromarray(g.astype(np.uint8))


def effacer_crayon(g, boite, gris=100, noir=50):
    """Blanchit les pixels gris (crayon) qui ne bordent pas un trait imprimé noir."""
    x0, y0, x1, y1 = boite
    zone = g[y0:y1, x0:x1]
    proche_noir = np.asarray(Image.fromarray(zone.astype(np.uint8)).filter(ImageFilter.MinFilter(7)), float) < noir
    zone[(zone >= gris) & ~proche_noir] = 255


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
