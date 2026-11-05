#!/usr/bin/env python3
"""Découpe du partiel EN208 « Technologie des circuits intégrés numériques »
2019-2020 (S. Renaud) en images : énoncé commun, en-tête de chaque partie, une
image par question.

Source : sources/numc1/annales/2019-2020-partiel.pdf (scan couleur, 3 pages).
Pages rendues à 200 dpi avec pdftoppm, en couleur, puis passées en niveaux de gris.

Nettoyage :
- page 2 : le « A » de « NAND » (ligne 4 de la partie 2), repassé à l'encre bleue,
  est en partie effacé avec elle (il ressemble à un « O ») ;
- toutes les pages : encre colorée effacée (pixels saturés et leur voisinage), fond
  éclairci (le verso transparaît légèrement) ;
- page 3 (figure 2), couverte d'annotations d'un étudiant (chronogrammes en
  couleur, « ouvert », « fermé », « passant », « X1 = 0 », « H = 0 », « Y = 1 »,
  « H = 1 », schéma griffonné sous la figure) : seuls sont gardés les traits
  horizontaux et verticaux du schéma, les plots carrés et le contenu de rectangles
  qui entourent les symboles et les étiquettes imprimés (liste GARDER) ; les deux
  traits de crayon qui barrent les inverseurs sont effacés le long de leur tracé
  (liste TRAITS ; les côtés obliques des triangles en gardent une petite coupure) et quelques restes isolés blanchis (liste BLANC). Le surlignage
  gris le long des drains de P2 et P1 n'a pas pu être séparé du trait imprimé : le
  fil y paraît plus épais.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/numc1-technologie-circuits-numeriques/annales/sujets/2019-2020-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/numc1/annales/2019-2020-partiel.pdf')
NOM = '2019-2020-partiel'
PAGES = (1, 2, 3)
MARGE = 15
DPI = 200
ECART = 25
LARGEUR_MAX = 1400

X0, X1 = 110, 1500
BOITES = [
    ('intro',  [(1, (X0, 520, X1, 690))]),
    ('ex1',    [(1, (X0, 755, X1, 1765))]),
    ('ex1-q1', [(1, (X0, 1815, X1, 1860))]),
    ('ex1-q2', [(1, (X0, 1927, X1, 2180))]),
    ('ex1-q3', [(2, (X0, 167, X1, 245))]),
    ('ex1-q4', [(2, (X0, 319, X1, 404))]),
    ('ex1-q5', [(2, (X0, 470, X1, 594))]),
    ('ex1-q6', [(2, (X0, 661, X1, 708))]),
    ('ex2',    [(2, (X0, 859, X1, 1138)), (3, (200, 110, 1460, 880))]),
    ('ex2-q1', [(2, (X0, 1200, X1, 1470))]),
    ('ex2-q2', [(2, (X0, 1536, X1, 1622))]),
    ('ex2-q3', [(2, (X0, 1687, X1, 1847))]),
]

# Page 3 : rectangles (x0, y0, x1, y1) dont le contenu sombre est conservé.
GARDER = [(635, 120, 690, 150), (625, 230, 670, 265), (665, 215, 745, 265), (855, 215, 980, 270),
          (975, 230, 1025, 265), (385, 245, 505, 305), (405, 320, 505, 410), (245, 345, 300, 385),
          (620, 330, 720, 385), (795, 410, 835, 435), (1135, 390, 1230, 500), (1125, 510, 1210, 570),
          (1360, 340, 1425, 378), (1300, 440, 1360, 472), (245, 530, 305, 568), (405, 505, 505, 595),
          (385, 590, 505, 655), (620, 515, 720, 575), (790, 570, 830, 595), (895, 520, 1010, 700),
          (625, 640, 745, 690), (625, 740, 705, 800), (920, 740, 990, 800), (770, 840, 900, 875)]
TRAITS = [[(403, 392), (445, 360), (492, 328)],
          [(378, 592), (413, 560), (447, 530), (480, 505), (522, 481)]]
# Page 2 : le « A » de « NAND » est recouvert d'encre bleue ; masque de couleur
# restreint (sans dilatation, saturation forte) dans ce rectangle.
NAND_P2 = (1100, 1085, 1270, 1140)
BLANC = {3: [(860, 100, 900, 145), (1288, 462, 1302, 492), (903, 618, 925, 648)]}


def runs(m, n, axe):
    m = m.astype(np.int32)
    if axe == 1:
        m = m.T
    c = np.cumsum(np.pad(m, ((1, 0), (0, 0))), axis=0)
    plein = (c[n:] - c[:-n]) == n
    out = np.zeros_like(m, bool)
    for k in range(n):
        out[k:k + plein.shape[0]] |= plein
    return out.T if axe == 1 else out


def distance(shape, pts):
    yy, xx = np.mgrid[0:shape[0], 0:shape[1]]
    d = np.full(shape, 1e9)
    for (ax, ay), (bx, by) in zip(pts[:-1], pts[1:]):
        vx, vy = bx - ax, by - ay
        t = np.clip(((xx - ax) * vx + (yy - ay) * vy) / (vx * vx + vy * vy), 0, 1)
        d = np.minimum(d, np.hypot(xx - ax - t * vx, yy - ay - t * vy))
    return d


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-png', PDF, base], check=True)
    a = np.asarray(Image.open(base + '.png').convert('RGB'), float)
    g = a.mean(axis=2)
    sat = a.max(axis=2) - a.min(axis=2)
    couleur = np.asarray(Image.fromarray(((sat > 25) * 255).astype(np.uint8))
                         .filter(ImageFilter.MaxFilter(5))) > 0
    if num == 2:
        x0, y0, x1, y1 = NAND_P2
        couleur[y0:y1, x0:x1] = sat[y0:y1, x0:x1] > 30
    g[couleur] = 255
    if num == 3:
        sombre = g < 140
        garder = runs(sombre, 14, 0) | runs(sombre, 14, 1)
        garder |= np.asarray(Image.fromarray((sombre * 255).astype(np.uint8))
                             .filter(ImageFilter.MinFilter(5)).filter(ImageFilter.MaxFilter(5))) > 0
        for x0, y0, x1, y1 in GARDER:
            garder[y0:y1, x0:x1] |= sombre[y0:y1, x0:x1]
        for pts in TRAITS:
            garder &= ~((distance(g.shape, pts) <= 3.5) & ~(runs(sombre, 11, 0) | runs(sombre, 11, 1)))
        g = np.where(garder, g, 255)
    for x0, y0, x1, y1 in BLANC.get(num, []):
        g[y0:y1, x0:x1] = 255
    g = np.clip((g - 40) / (200 - 40), 0, 1)
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
