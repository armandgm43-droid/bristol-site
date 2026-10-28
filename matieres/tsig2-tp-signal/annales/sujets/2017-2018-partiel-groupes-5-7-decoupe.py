#!/usr/bin/env python3
"""Découpe du partiel de TP TS202 (TSIG2) 2017-2018, sujets des groupes 7 et 5, en images
(une par question).

Source : sources/tsig2/annales/2017-2018-partiel-groupes-5-7.pdf (4 pages, chacune = une
photo JPEG 1259 x 1679 px à 200 ppi ; pages 1-2 : groupe 7, pages 3-4 : groupe 5).
On extrait la photo de chaque page avec pdfimages, on aplanit le fond (division par une
estimation de l'éclairage), on efface les annotations manuscrites d'un étudiant à
l'encre bleue ou verte (pixels plus bleus que rouges, sauf dans la figure de la page 1
dont la courbe imprimée est bleue, voir PROTEGER) et les annotations noires (rectangles
BLANCHIR), puis on découpe. Les largeurs sont uniformisées à la fin (marge blanche à
droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig2-tp-signal/annales/sujets/2017-2018-partiel-groupes-5-7-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig2/annales/2017-2018-partiel-groupes-5-7.pdf')
NOM = '2017-2018-partiel-groupes-5-7'
MARGE = 15
LARGEUR_MAX = 1400

# Annotations manuscrites noires à blanchir : page -> [(x0, y0, x1, y1)].
BLANCHIR = {
    1: [],
    2: [(925, 674, 1235, 885),     # « RSB = Ps/(Pe a²) », « 10 log(...) = 20 »
        (910, 1118, 1015, 1162)],  # « 44 – »
    3: [(150, 1104, 176, 1202),    # accolade devant « S'agit-il… »
        (340, 1098, 680, 1110),    # soulignement de « une TFD à N=M=256 points »
        (995, 1172, 1030, 1198)],  # trait isolé
    4: [(55, 175, 425, 405),       # « RSB = Ps/(a² Pe) »… à gauche des formules
        (915, 165, 1045, 265)],    # griffonnage à droite
}
# Zones où l'encre bleue est imprimée (courbe de la figure) : pas d'effacement.
PROTEGER = {1: [(380, 780, 880, 1180)]}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans la photo extraite.
# ex1, ex2 : groupe 7 ; ex3, ex4 : groupe 5.
BOITES = [
    ('ex1',    [(1, (140, 625, 1125, 1468))]),
    ('ex1-q1', [(1, (155, 1474, 1125, 1600))]),
    ('ex1-q2', [(2, (100, 168, 1130, 350))]),
    ('ex1-q3', [(2, (100, 356, 1130, 470))]),
    ('ex2',    [(2, (110, 535, 1130, 1006))]),
    ('ex2-q1', [(2, (125, 1010, 1130, 1047))]),
    ('ex2-q2', [(2, (125, 1048, 1130, 1128))]),
    ('ex2-q3', [(2, (125, 1145, 1130, 1290))]),
    ('ex2-q4', [(2, (125, 1290, 1130, 1352))]),
    ('ex2-q5', [(2, (125, 1355, 1130, 1428))]),
    ('ex3',    [(3, (110, 600, 1130, 748))]),
    ('ex3-q1', [(3, (120, 788, 1130, 968))]),
    ('ex3-q2', [(3, (120, 972, 1130, 1203))]),
    ('ex3-q3', [(3, (120, 1208, 1130, 1372))]),
    # Exercice 4 : titre et définition (bas de la page 3), formules et contexte (page 4).
    ('ex4',    [(3, (130, 1412, 1130, 1550)), (4, (130, 180, 1130, 490))]),
    ('ex4-q1', [(4, (130, 496, 1130, 532))]),
    ('ex4-q2', [(4, (130, 532, 1130, 612))]),
    ('ex4-q3', [(4, (130, 628, 1130, 808))]),
    ('ex4-q4', [(4, (130, 808, 1130, 885))]),
]


def photo(page, tmp):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdfimages', '-png', '-f', str(page), '-l', str(page), PDF, base], check=True)
    return Image.open(base + '-000.png').convert('RGB')


def aplanir(im, page):
    """Fond blanc uniforme, encre bleue effacée, annotations blanchies, gris contrastés."""
    rgb = np.asarray(im, float)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    gris = 0.299 * R + 0.587 * G + 0.114 * B
    g = Image.fromarray(gris.clip(0, 255).astype(np.uint8))
    fond = np.asarray(g.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)), float)
    a = gris / np.maximum(fond, 1)
    # Encre bleue ou verte : le papier et l'impression sont neutres ou rougeâtres (B < R).
    encre = ((B - R) > 4) & (a < 0.93)
    encre = np.asarray(Image.fromarray((encre * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
    for x0, y0, x1, y1 in PROTEGER.get(page, []):
        encre[y0:y1, x0:x1] = False
    noir_imprime = (a < 0.35) & ((B - R) < 0)
    a[encre & ~noir_imprime] = 1.0
    for x0, y0, x1, y1 in BLANCHIR.get(page, []):
        a[y0:y1, x0:x1] = 1.0
    a = np.clip((a - 0.45) / (0.88 - 0.45), 0, 1) ** 1.3
    return Image.fromarray((a * 255).astype(np.uint8))


def rogner(im, seuil=160, min_px=2):
    """Rogne au contenu puis ajoute une marge blanche de MARGE px."""
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
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: aplanir(photo(p, tmp), p) for p in (1, 2, 3, 4)}
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
