#!/usr/bin/env python3
"""Découpe du partiel EN208 « Technologie des circuits intégrés numériques » du
12/01/2017 (S. Renaud) en images : énoncé commun, en-tête de chaque partie, une
image par question.

Source : sources/numc1/annales/2016-2017-partiel.pdf (photocopie photographiée,
2 pages). Pages rendues à 200 dpi avec pdftoppm (environ 1659 x 2334 px), en
niveaux de gris.

Annotations manuscrites effacées (page 2, figure 2) : les lettres « P » et « N »
écrites dans la marge gauche du schéma (rectangles blanchis) et les quatre traits
de stylo qui barrent les PMOS A, B, D et le NMOS C (pixels proches du tracé
blanchis, sauf ceux qui appartiennent à un trait horizontal ou vertical du
schéma imprimé ; les pointes de flèche des transistors peuvent être légèrement
écornées).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/numc1-technologie-circuits-numeriques/annales/sujets/2016-2017-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/numc1/annales/2016-2017-partiel.pdf')
NOM = '2016-2017-partiel'
PAGES = (1, 2)
MARGE = 15
DPI = 200
ECART = 25
LARGEUR_MAX = 1400

X0, X1 = 130, 1530
BOITES = [
    ('intro',  [(1, (X0, 570, X1, 745))]),
    ('ex1',    [(1, (X0, 815, X1, 1210))]),
    ('ex1-q1', [(1, (X0, 1232, X1, 2118))]),
    ('ex2',    [(2, (X0, 100, X1, 1460))]),
    ('ex2-q1', [(2, (X0, 1528, X1, 1572))]),
    ('ex2-q2', [(2, (X0, 1605, X1, 1650))]),
    ('ex2-q3', [(2, (X0, 1683, X1, 1726))]),
    ('ex2-q4', [(2, (X0, 1760, X1, 1972))]),
    ('ex2-q5', [(2, (X0, 2014, X1, 2094))]),
]

# Rectangles blanchis : page -> [(x0, y0, x1, y1)]
BLANC = {2: [(225, 815, 300, 897), (236, 1133, 300, 1207)]}
# Traits de stylo (lignes brisées) : page -> [[(x, y), ...], ...]
TRAITS = {2: [
    [(406, 803), (424, 820), (442, 838), (452, 852), (462, 872), (488, 905)],
    [(590, 757), (625, 800), (660, 842)],
    [(715, 805), (740, 820), (770, 850), (800, 887)],
    [(638, 1008), (655, 1030), (670, 1050), (686, 1069), (700, 1087), (710, 1100)],
]}
DEMI_LARGEUR = 6.0


def runs(m, n, axe):
    """Pixels de m appartenant à une suite d'au moins n pixels alignés selon axe."""
    m = m.astype(np.int32)
    if axe == 1:
        m = m.T
    c = np.cumsum(np.pad(m, ((1, 0), (0, 0))), axis=0)
    plein = (c[n:] - c[:-n]) == n
    out = np.zeros_like(m, bool)
    for k in range(n):
        out[k:k + plein.shape[0]] |= plein
    return out.T if axe == 1 else out


def effacer_trait(g, pts):
    xs = [p[0] for p in pts]; ys = [p[1] for p in pts]
    x0, x1 = min(xs) - 8, max(xs) + 8
    y0, y1 = min(ys) - 8, max(ys) + 8
    zone = g[y0:y1, x0:x1]
    sombre = zone < 150
    garder = runs(sombre, 11, 0) | runs(sombre, 11, 1)
    yy, xx = np.mgrid[y0:y1, x0:x1]
    d = np.full(zone.shape, 1e9)
    for (ax, ay), (bx, by) in zip(pts[:-1], pts[1:]):
        vx, vy = bx - ax, by - ay
        t = np.clip(((xx - ax) * vx + (yy - ay) * vy) / (vx * vx + vy * vy), 0, 1)
        d = np.minimum(d, np.hypot(xx - ax - t * vx, yy - ay - t * vy))
    zone[(d <= DEMI_LARGEUR) & ~garder] = 255


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float).copy()
    for x0, y0, x1, y1 in BLANC.get(num, []):
        g[y0:y1, x0:x1] = 255
    for pts in TRAITS.get(num, []):
        effacer_trait(g, pts)
    g = np.clip((g - 40) / (215 - 40), 0, 1)
    return Image.fromarray((g * 255).astype(np.uint8))


def rogner(im, seuil=160, min_px=2):
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
        if os.environ.get('PAGES_DIR'):
            for p, im in pages.items():
                im.save(os.path.join(os.environ['PAGES_DIR'], f'{NOM}-page{p}.png'))
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
