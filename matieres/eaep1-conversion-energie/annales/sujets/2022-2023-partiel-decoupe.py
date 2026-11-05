#!/usr/bin/env python3
"""Découpe du partiel EA207 (EAEP1) du 10/01/2023 en images (une par question).

Source : sources/eaep1/annales/2022-2023-partiel-p1.jpg et -p2.jpg (photos 4032 x 3024,
orientation EXIF « 90° »). Chaque photo est remise droite (EXIF), réduite à 1500 x 2000 px,
redressée par une transformation perspective (quatre coins du texte, voir COINS), aplanie
(division par une estimation de l'éclairage), puis découpée. Les soulignements d'un
étudiant (stylo) sont conservés. Les largeurs sont uniformisées à la fin.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eaep1-conversion-energie/annales/sujets/2022-2023-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : Pillow, numpy.
"""
import os, sys
import numpy as np
from PIL import Image, ImageFilter, ImageOps

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
JPG = os.path.join(RACINE, 'sources/eaep1/annales/2022-2023-partiel-p{}.jpg')
NOM = '2022-2023-partiel'
MARGE = 15
LARGEUR_MAX = 1400

# Coins du texte dans la photo réduite (haut gauche, haut droit, bas gauche, bas droit)
# et leur position après redressement (image 1460 x 2000).
COINS = {1: [(224.8, 328.7), (1360, 418), (125.4, 1868), (1375, 1861.6)],
         2: [(270, 82), (1370, 140), (170, 1645), (1470, 1630)]}
CIBLES = {1: [(130, 330), (1330, 330), (130, 1870), (1330, 1870)],
          2: [(130, 90), (1330, 90), (130, 1640), (1330, 1640)]}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans l'image redressée.
# Numéros de questions du sujet : Q1 à Q9 (cours), puis 1 à 16 en continu (parties A, B, C).
BOITES = [
    ('ex1',     [(1, (118, 262, 600, 302))]),
    ('ex1-q1',  [(1, (118, 304, 1345, 382))]),
    ('ex1-q2',  [(1, (118, 386, 1345, 426))]),
    ('ex1-q3',  [(1, (118, 429, 1345, 506))]),
    ('ex1-q4',  [(1, (118, 509, 1345, 586))]),
    ('ex1-q5',  [(1, (118, 589, 1345, 630))]),
    ('ex1-q6',  [(1, (118, 633, 1345, 707))]),
    ('ex1-q7',  [(1, (118, 710, 1345, 786))]),
    ('ex1-q8',  [(1, (118, 789, 1345, 864))]),
    ('ex1-q9',  [(1, (118, 867, 1345, 942))]),
    ('ex2',     [(1, (110, 962, 1345, 1602))]),
    ('ex2-q1',  [(1, (110, 1613, 1345, 1648))]),
    ('ex2-q2',  [(1, (110, 1652, 1345, 1772))]),
    ('ex2-q3',  [(1, (110, 1777, 1345, 1888))]),
    ('ex2-q4',  [(2, (110, 68, 1345, 142))]),
    ('ex2-q5',  [(2, (110, 147, 1345, 226))]),
    ('ex2-q6',  [(2, (110, 229, 1345, 372))]),
    ('ex2-q7',  [(2, (110, 374, 1345, 422))]),
    ('ex2-q8',  [(2, (110, 424, 1345, 602))]),
    ('ex2-q9',  [(2, (110, 606, 1345, 787))]),
    ('ex2-q10', [(2, (110, 790, 1345, 867))]),
    ('ex3',     [(2, (110, 898, 1345, 1080))]),
    ('ex3-q11', [(2, (110, 1088, 1345, 1127))]),
    ('ex3-q12', [(2, (110, 1130, 1345, 1202))]),
    ('ex3-q13', [(2, (110, 1205, 1345, 1247))]),
    ('ex4',     [(2, (110, 1283, 1336, 1497))]),
    ('ex4-q14', [(2, (110, 1499, 1336, 1541))]),
    ('ex4-q15', [(2, (110, 1544, 1336, 1617))]),
    ('ex4-q16', [(2, (110, 1622, 1336, 1727))]),
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
    return im.transform((1460, 2000), Image.PERSPECTIVE, coeffs(CIBLES[page], COINS[page]),
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
    # Les soulignements d'un étudiant (stylo bleu-noir) ne se distinguent pas de
    # l'impression par la couleur sur ces photos : ils sont conservés.
    a = np.clip((a - 0.45) / (0.82 - 0.45), 0, 1) ** 1.3
    return Image.fromarray((a * 255).astype(np.uint8))


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
    for nom, morceaux in BOITES:
        parts = [rogner(pages[p].crop(b)) for p, b in morceaux]
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
