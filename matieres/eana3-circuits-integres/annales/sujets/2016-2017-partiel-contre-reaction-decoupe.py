#!/usr/bin/env python3
"""Découpe du partiel EA211 « Contre-réaction » du 9/11/2016 (adaptation d'impédance
par dégénérescence inductive, F. Rivet et N. Verrascina) en images : énoncé commun,
en-tête de chaque partie, une image par question.

Source : sources/eana3/annales/2016-2017-partiel-contre-reaction.pdf (photo
convertie en PDF, 2 pages). Pages rendues à 200 dpi avec pdftoppm (environ
1650 x 2339 px), en niveaux de gris. Aucune annotation manuscrite sur ce sujet.
Une image peut assembler plusieurs morceaux (empilés verticalement). Les largeurs
sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2016-2017-partiel-contre-reaction-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana3/annales/2016-2017-partiel-contre-reaction.pdf')
NOM = '2016-2017-partiel-contre-reaction'
PAGES = (1, 2)
MARGE = 15
DPI = 200
ECART = 25        # espace entre deux morceaux empilés
LARGEUR_MAX = 1400

X0, X1 = 150, 1500
# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('intro',   [(1, (X0, 560, X1, 2150))]),
    ('ex1',     [(2, (X0, 165, X1, 218))]),
    ('ex1-q1',  [(2, (X0, 234, X1, 490))]),
    ('ex1-q2',  [(2, (X0, 494, X1, 542))]),
    ('ex1-q3',  [(2, (X0, 546, X1, 640))]),
    ('ex1-q4',  [(2, (X0, 648, X1, 796))]),
    ('ex1-q5',  [(2, (X0, 801, X1, 850))]),
    ('ex2',     [(2, (X0, 915, X1, 975))]),
    ('ex2-q6',  [(2, (X0, 980, X1, 1232))]),
    ('ex2-q7',  [(2, (X0, 1240, X1, 1335)), (2, (X0, 1384, X1, 1468))]),
    ('ex2-q8',  [(2, (X0, 1500, X1, 1600))]),
    ('ex3',     [(2, (X0, 1664, X1, 1720))]),
    ('ex3-q9',  [(2, (X0, 1731, X1, 1885))]),
    ('ex3-q10', [(2, (X0, 1886, X1, 2030))]),
]

BLANC = {}
CRAYON = {}


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    for b in CRAYON.get(num, []):
        effacer_crayon(g, b)
    for x0, y0, x1, y1 in BLANC.get(num, []):
        g[y0:y1, x0:x1] = 255
    g = np.clip((g - 40) / (225 - 40), 0, 1)   # fond du scan blanc, noirs francs
    return Image.fromarray((g * 255).astype(np.uint8))


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
