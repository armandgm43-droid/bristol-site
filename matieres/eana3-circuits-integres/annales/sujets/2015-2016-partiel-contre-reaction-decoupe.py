#!/usr/bin/env python3
"""Découpe du partiel EA211 « Contre-réaction » du 9/11/2015 (contre-réaction de mode
commun, Y. Deval et F. Rivet) en images : énoncé commun, en-tête de chaque partie,
une image par question.

Source : sources/eana3/annales/2015-2016-partiel-contre-reaction.pdf (scan, 3 pages).
Pages rendues à 200 dpi avec pdftoppm (1700 x 2339 px), en niveaux de gris.
Les annotations au crayon d'un étudiant sur la figure 5 (p. 3 : « Av = gm rds »,
« Av = -gm rds », un trait courbe autour de M et M3, « ie », « ve ») sont effacées.
Une image peut assembler plusieurs morceaux (empilés verticalement), par exemple
une question à cheval sur deux pages. Les largeurs sont uniformisées à la fin
(marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2015-2016-partiel-contre-reaction-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana3/annales/2015-2016-partiel-contre-reaction.pdf')
NOM = '2015-2016-partiel-contre-reaction'
PAGES = (1, 2, 3)
MARGE = 15
DPI = 200
ECART = 25        # espace entre deux morceaux empilés
LARGEUR_MAX = 1400

X0, X1 = 165, 1495
# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('intro',   [(1, (X0, 528, X1, 1812))]),
    ('ex1',     [(1, (X0, 1838, X1, 1882))]),
    ('ex1-q1',  [(1, (X0, 1896, X1, 2136)), (2, (X0, 190, X1, 644))]),
    ('ex2',     [(2, (X0, 645, X1, 2132)), (3, (X0, 190, X1, 888))]),
    ('ex2-q2',  [(3, (X0, 893, X1, 938))]),
    ('ex2-q3',  [(3, (X0, 944, X1, 1033))]),
    ('ex2-q4',  [(3, (X0, 1046, X1, 1090))]),
    ('ex2-q5',  [(3, (X0, 1095, X1, 1191))]),
    ('ex2-q6',  [(3, (X0, 1196, X1, 1242))]),
    ('ex2-q7',  [(3, (X0, 1248, X1, 1291))]),
    ('ex3',     [(3, (X0, 1316, X1, 1361))]),
    ('ex3-q8',  [(3, (X0, 1376, X1, 1521))]),
    ('ex3-q9',  [(3, (X0, 1525, X1, 1672))]),
    ('ex4',     [(3, (X0, 1689, X1, 1850))]),
    ('ex4-q10', [(3, (X0, 1854, X1, 1951))]),
]

# Annotations manuscrites à effacer, page 3.
BLANC = {3: [(1052, 292, 1262, 356),                       # « Av = gm rds »
             (948, 634, 1044, 664), (1051, 634, 1065, 664), # « Av = -gm rds »
             (1073, 634, 1091, 664), (1099, 634, 1150, 664),
             (1420, 1316, 1495, 1361)]}                     # trait en marge
CRAYON = {3: [(600, 262, 1270, 700)]}                      # traits fins autour de M, M3


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
