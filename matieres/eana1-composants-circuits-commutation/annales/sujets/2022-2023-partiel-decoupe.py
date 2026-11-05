#!/usr/bin/env python3
"""Découpe du partiel EA 205 (EANA1) du 3 janvier 2023 en images (une par
exercice et une par question ou sous-question).

Source : sources/eana1/annales/2022-2023-partiel-p1.jpg et -p2.jpg (photos 4032 x 3024,
orientation EXIF « 90° »). Chaque photo est remise droite (EXIF), réduite à 1500 x 2000 px,
redressée par une transformation perspective, aplanie (division par une estimation de
l'éclairage), puis découpée. Quadrilatères de référence (COINS), qui sont des rectangles
sur le papier : page 1, bords gauche et droit du cadre d'en-tête prolongés, bord haut du
cadre et fil horizontal du schéma de l'exercice II ; page 2, bords gauche et droit de la
feuille, ligne de base « Avec T1 = 10 ms… » et bord bas de la feuille. Hauteur des
rectangles cibles choisie pour conserver les proportions des caractères (estimation).
Le soulignement ondulé de « Vout(t) » (exercice I) est imprimé : conservé. Aucune
annotation manuscrite. Sous-questions a), b)… des exercices I et II : exN-qa, exN-qb… ;
questions numérotées de l'exercice III : ex3-q1… Largeurs uniformisées à la fin.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana1-composants-circuits-commutation/annales/sujets/2022-2023-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : Pillow, numpy.
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageOps

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
JPG = os.path.join(RACINE, 'sources/eana1/annales/2022-2023-partiel-p{}.jpg')
NOM = '2022-2023-partiel'
MARGE = 15
LARGEUR_MAX = 1400

# Coins des rectangles de référence dans la photo réduite (haut gauche, haut droit,
# bas gauche, bas droit) et leur position après redressement (image 1500 x 2000).
COINS = {1: [(152, 72), (1313, 113), (10.8, 1210.7), (1411.9, 1216.3)],
         2: [(141.7, 348.2), (1397, 344.3), (-18.6, 1805.9), (1533, 1855)]}
CIBLES = {1: [(150, 60), (1400, 60), (150, 1160), (1400, 1160)],
          2: [(130, 330), (1330, 330), (130, 1590), (1330, 1590)]}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans l'image redressée.
# Zones blanchies dans l'image redressée, page 1 : ombre du bord gauche de la feuille ;
# bas de parenthèses des lignes a) et d) de l'exercice II, visibles en haut des découpes b) et e).
BLANC = {1: [(0, 1100, 205, 2000), (540, 1374, 1100, 1387), (540, 1460, 1100, 1472)], 2: []}

BOITES = [
    ('ex1',    [(1, (150, 340, 1400, 738))]),
    ('ex1-qa', [(1, (150, 743, 1400, 772))]),
    ('ex1-qb', [(1, (150, 772, 1400, 798))]),
    ('ex1-qc', [(1, (150, 798, 1400, 828))]),
    ('ex1-qd', [(1, (150, 829, 1400, 859))]),
    ('ex1-qe', [(1, (150, 860, 1400, 886))]),
    ('ex1-qf', [(1, (150, 887, 1400, 915))]),
    ('ex2',    [(1, (150, 938, 1400, 1332))]),
    ('ex2-qa', [(1, (150, 1345, 1400, 1374))]),
    ('ex2-qb', [(1, (150, 1375, 1400, 1403))]),
    ('ex2-qc', [(1, (150, 1404, 1400, 1431))]),
    ('ex2-qd', [(1, (150, 1432, 1400, 1460))]),
    ('ex2-qe', [(1, (150, 1461, 1400, 1492))]),
    ('ex3',    [(2, (185, 55, 1300, 340))]),
    ('ex3-q1', [(2, (185, 358, 1300, 486))]),
    ('ex3-q2', [(2, (185, 486, 1300, 610))]),
    ('ex3-q3', [(2, (185, 610, 1300, 808))]),
    ('ex3-q4', [(2, (185, 808, 1300, 905))]),
    ('ex3-q5', [(2, (185, 905, 1300, 930))]),
    ('ex3-q6', [(2, (185, 930, 1300, 954))]),
    ('ex3-q7', [(2, (185, 954, 1300, 978))]),
    ('ex3-q8', [(2, (185, 978, 1300, 1335))]),
    ('ex3-q9', [(2, (185, 1368, 1300, 1398))]),
    ('ex3-q10', [(2, (185, 1398, 1300, 1428))]),
]


def coeffs(cibles, coins):
    """Coefficients de Image.PERSPECTIVE (point de sortie -> point d'entrée)."""
    A, b = [], []
    for (x, y), (u, v) in zip(cibles, coins):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); b.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); b.append(v)
    return np.linalg.solve(np.array(A, float), np.array(b, float)).tolist()


def photo(page):
    im = ImageOps.exif_transpose(Image.open(JPG.format(page))).convert('RGB')
    im = im.resize((1500, 2000), Image.LANCZOS)
    return im.transform((1500, 2000), Image.PERSPECTIVE, coeffs(CIBLES[page], COINS[page]),
                        Image.BICUBIC, fillcolor=(255, 255, 255))


def aplanir(im):
    """Fond blanc uniforme, encre bleue effacée, niveaux de gris contrastés."""
    rgb = np.asarray(im, float)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    gris = 0.299 * R + 0.587 * G + 0.114 * B
    g = Image.fromarray(gris.clip(0, 255).astype(np.uint8))
    # Fond estimé sur une image réduite 4 fois (fenêtre max de 60 px à pleine échelle).
    petit = g.resize((g.width // 4, g.height // 4), Image.BILINEAR)
    petit = petit.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(8))
    fond = np.asarray(petit.resize(g.size, Image.BILINEAR), float)
    a = gris / np.maximum(fond, 1)
    a = np.clip((a - 0.45) / (0.82 - 0.45), 0, 1) ** 1.3
    return Image.fromarray((a * 255).astype(np.uint8))


def nettoyer_haut(im, seuil=160):
    """Blanchit les traits qui touchent le bord haut de la découpe : ce sont les bas
    de caractères (parenthèses, jambages) de la ligne précédente, les lignes du sujet
    étant très serrées. Les boîtes des questions sont placées pour que leur propre
    texte ne touche pas ce bord."""
    a = np.asarray(im)
    b = Image.fromarray(np.where(a < seuil, 0, 255).astype(np.uint8))
    for x in np.where(a[0] < seuil)[0]:
        if b.getpixel((int(x), 0)) == 0:
            ImageDraw.floodfill(b, (int(x), 0), 128)
    out = a.copy()
    out[np.asarray(b) == 128] = 255
    return Image.fromarray(out)


def rogner(im, seuil=160, min_px=2):
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
        out.paste(i, (0, y)); y += i.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    pages = {p: aplanir(photo(p)) for p in (1, 2)}
    for p, zones in BLANC.items():
        for z in zones:
            pages[p].paste(255, z)
    for nom, morceaux in BOITES:
        parts = [rogner(nettoyer_haut(pages[p].crop(b)) if '-q' in nom else pages[p].crop(b))
                 for p, b in morceaux]
        ims[nom] = empiler(parts) if len(parts) > 1 else parts[0]
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
