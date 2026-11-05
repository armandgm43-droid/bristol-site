#!/usr/bin/env python3
"""Découpe de l'examen « Synthèse VHDL - NUMC1 » du 7 janvier 2026 (1re session)
en images : énoncé commun, en-tête de chaque partie et de chaque section, une
image par question.

Source : sources/numc1/annales/2025-2026-partiel.pdf (scan couleur, 4 pages).
Pages rendues à 200 dpi avec pdftoppm, en couleur, puis passées en niveaux de gris ;
fond éclairci (le verso transparaît).

Annotations d'un étudiant effacées : surlignage orange (page 1, encre colorée) ;
cercles de stylo autour des numéros 2.2 (page 1), 2.3 (page 2), 1.7 (page 3) et
3.4 (page 4) : dans un rectangle autour de chaque cercle, les pixels gris qui ne
touchent pas un trait noir imprimé sont blanchis, puis les points isolés (liste
CERCLES ; de petites traces peuvent rester, et ces numéros sont un peu amincis) ;
mot « BONUS » et accolade au crayon dans la marge gauche de la page 4 (rectangle
blanchi). Traits de crayon dans les coins des pages : hors des découpes.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/numc1-technologie-circuits-numeriques/annales/sujets/2025-2026-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/numc1/annales/2025-2026-partiel.pdf')
NOM = '2025-2026-partiel'
PAGES = (1, 2, 3, 4)
MARGE = 15
DPI = 200
ECART = 25
LARGEUR_MAX = 1400

X0, X1 = 145, 1560
BOITES = [
    ('intro',     [(1, (X0, 245, X1, 548))]),
    ('ex1',       [(1, (X0, 638, X1, 790)), (1, (X0, 858, X1, 1242)), (2, (200, 600, X1, 1395))]),
    ('ex1-q1',    [(1, (X0, 1297, X1, 1513))]),
    ('ex1-q2',    [(1, (X0, 1556, X1, 1880)), (2, (240, 1498, 820, 1940))]),
    ('ex1-q2-1',  [(1, (X0, 1906, X1, 1962))]),
    ('ex1-q2-2',  [(1, (X0, 1980, X1, 2188))]),
    ('ex1-q2-3',  [(2, (X0, 215, X1, 504))]),
    ('ex2',       [(3, (X0, 165, X1, 1170))]),
    ('ex2-s1',    [(3, (X0, 1208, X1, 1332))]),
    ('ex2-q1-1',  [(3, (X0, 1332, X1, 1376))]),
    ('ex2-q1-2',  [(3, (X0, 1406, X1, 1504))]),
    ('ex2-q1-3',  [(3, (X0, 1504, X1, 1546))]),
    ('ex2-q1-4',  [(3, (X0, 1546, X1, 1631))]),
    ('ex2-q1-5',  [(3, (X0, 1631, X1, 1721))]),
    ('ex2-q1-6',  [(3, (X0, 1720, X1, 1808))]),
    ('ex2-q1-7',  [(3, (X0, 1807, X1, 1895))]),
    ('ex2-s2',    [(3, (X0, 1980, X1, 2026))]),
    ('ex2-q2-1',  [(3, (X0, 2088, X1, 2186))]),
    ('ex2-q2-2',  [(4, (X0, 182, X1, 305))]),
    ('ex2-q2-3',  [(4, (X0, 306, X1, 433))]),
    ('ex2-q2-4',  [(4, (X0, 434, X1, 481))]),
    ('ex2-q2-5',  [(4, (X0, 484, X1, 528))]),
    ('ex2-s3',    [(4, (X0, 608, X1, 850))]),
    ('ex2-q3-1',  [(4, (X0, 882, X1, 972))]),
    ('ex2-q3-2',  [(4, (X0, 968, X1, 1058))]),
    ('ex2-q3-3',  [(4, (X0, 1055, X1, 1180))]),
    ('ex2-q3-4',  [(4, (X0, 1179, X1, 1245))]),
]

CERCLES = {1: [(180, 1980, 320, 2065)], 2: [(170, 215, 330, 300)],
           3: [(250, 1785, 380, 1868)], 4: [(205, 1165, 345, 1248)]}
BLANC = {4: [(0, 540, 147, 1290)]}


def effacer_cercle(g, boite, gris=55, noir=40):
    """Blanchit les pixels gris qui ne bordent pas un trait noir imprimé, puis les points isolés."""
    x0, y0, x1, y1 = boite
    z = g[y0:y1, x0:x1]
    pres_noir = np.asarray(Image.fromarray(z.clip(0, 255).astype(np.uint8))
                           .filter(ImageFilter.MinFilter(3)), float) < noir
    z[(z >= gris) & ~pres_noir] = 255
    sombre = (z < 128).astype(np.uint8) * 255
    voisins = np.asarray(Image.fromarray(sombre).filter(ImageFilter.BoxBlur(2)), float) * 25 / 255
    z[(z < 128) & (voisins < 4)] = 255


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-png', PDF, base], check=True)
    a = np.asarray(Image.open(base + '.png').convert('RGB'), float)
    g = a.mean(axis=2)
    g[(a.max(axis=2) - a.min(axis=2)) > 40] = 255          # surligneur et encre colorée
    for b in CERCLES.get(num, []):
        effacer_cercle(g, b)
    for x0, y0, x1, y1 in BLANC.get(num, []):
        g[y0:y1, x0:x1] = 255
    g = np.clip((g - 40) / (170 - 40), 0, 1)
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
