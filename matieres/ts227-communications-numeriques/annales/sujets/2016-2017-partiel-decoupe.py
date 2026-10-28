#!/usr/bin/env python3
"""Découpe du partiel TS227 2016-2017 en images (une par question).

Source : sources/ts227/annales/2016-2017-partiel.pdf (scan noir et blanc, 3 pages).
Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris. Les annotations manuscrites
d'un étudiant (calculs au bas de la page 2, « 5 = Tb », « 2 f(n) », trait sous ±3σ…)
sont effacées par des rectangles blancs (BLANCHIR) ; les zones griffonnées sous la
question 3 ne sont pas reprises. Les largeurs sont uniformisées à la fin (marge
blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/ts227-communications-numeriques/annales/sujets/2016-2017-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/ts227/annales/2016-2017-partiel.pdf')
NOM = '2016-2017-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400
PAGES = (1, 2, 3)

# Annotations manuscrites à blanchir : page -> [(x0, y0, x1, y1)] (coordonnées à 200 dpi).
BLANCHIR = {
    1: [(1305, 1808, 1400, 1821)],          # trait sous « ±3σ » (question 8)
    2: [(1275, 985, 1365, 1046),            # « 5 = Tb » à côté de la figure 2
        (1345, 1705, 1470, 1756),           # « 2 f(n) » à côté de la question 2
        (1270, 1890, 1330, 1945)],          # début d'un axe dessiné à côté de la question 3
    3: [],
}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; morceaux empilés dans l'ordre.
BOITES = [
    ('notations', [(1, (230, 785, 1430, 1125))]),
    # Partie 1 : titre, phrase d'introduction et figure 1 (page 2).
    ('ex1',       [(1, (230, 1170, 1430, 1215)), (1, (230, 1238, 1430, 1274)),
                   (2, (490, 288, 1180, 745))]),
    ('ex1-q1',    [(1, (230, 1279, 1430, 1346))]),
    ('ex1-q2',    [(1, (230, 1352, 1430, 1389))]),
    ('ex1-q3',    [(1, (230, 1391, 1430, 1461))]),
    ('ex1-q4',    [(1, (230, 1466, 1430, 1501))]),
    ('ex1-q5',    [(1, (230, 1506, 1430, 1544))]),
    ('ex1-q6',    [(1, (230, 1546, 1430, 1647)), (1, (230, 1652, 1430, 1722))]),  # définition de s_l + q. 6
    ('ex1-q7',    [(1, (230, 1728, 1430, 1768))]),
    ('ex1-q8',    [(1, (230, 1770, 1430, 1843))]),
    ('ex1-q9',    [(1, (230, 1845, 1430, 1880))]),
    # Exercice : titre et énoncé, figure 2 (page 2, au-dessus), figure 3 (page 3).
    ('ex2',       [(2, (240, 1230, 1420, 1556)), (2, (470, 783, 1200, 1188)),
                   (3, (240, 300, 1270, 725))]),
    ('ex2-q1',    [(2, (240, 1562, 1420, 1702))]),
    ('ex2-q2',    [(2, (240, 1704, 1420, 1752))]),
    ('ex2-q3',    [(2, (240, 1753, 1420, 1945))]),
    ('ex2-q4',    [(3, (240, 778, 1420, 848))]),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    g = np.clip((g - 40) / (225 - 40), 0, 1)
    for x0, y0, x1, y1 in BLANCHIR.get(num, []):
        g[y0:y1, x0:x1] = 1.0
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


def empiler(ims):
    w = max(i.width for i in ims)
    out = Image.new('L', (w, sum(i.height for i in ims)), 255)
    y = 0
    for i in ims:
        out.paste(i, (0, y))
        y += i.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in PAGES}
        if os.environ.get('PAGES_DIR'):              # contrôle : pages nettoyées entières
            for p, im in pages.items():
                im.save(os.path.join(os.environ['PAGES_DIR'], f'{NOM}-page{p}.png'))
        ims = {}
        for nom, morceaux in BOITES:
            parts = [rogner(pages[p].crop(b)) for p, b in morceaux]
            ims[nom] = empiler(parts) if len(parts) > 1 else parts[0]
    for nom, im in ims.items():
        if im.width > LARGEUR_MAX:
            ims[nom] = im.resize((LARGEUR_MAX, round(im.height * LARGEUR_MAX / im.width)), Image.LANCZOS)
    wmax = max(i.width for i in ims.values())
    for nom, im in ims.items():
        fond = Image.new('L', (wmax, im.height), 255)
        fond.paste(im, (0, 0))
        chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
        fond.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)
        print(chemin, fond.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
