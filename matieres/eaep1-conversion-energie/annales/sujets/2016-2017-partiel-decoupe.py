#!/usr/bin/env python3
"""Découpe du partiel EA207 (EAEP1) du 06/01/2017 en images (une par question).

Source : sources/eaep1/annales/2016-2017-partiel.pdf (2 pages, chacune = une photo
JPEG 1259 x 1679 px à 200 ppi). On extrait la photo de chaque page avec pdfimages,
on aplanit le fond (division par une estimation de l'éclairage), on efface les
quelques traces d'encre bleue (pixels plus bleus que rouges), puis on découpe.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eaep1-conversion-energie/annales/sujets/2016-2017-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eaep1/annales/2016-2017-partiel.pdf')
NOM = '2016-2017-partiel'
MARGE = 15
LARGEUR_MAX = 1400

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans la photo extraite.
BOITES = [
    ('ex1',     [(1, (70, 372, 1130, 778))]),
    ('ex1-q1',  [(1, (70, 782, 1130, 813))]),
    ('ex1-q2',  [(1, (70, 817, 1130, 849))]),
    ('ex1-q3',  [(1, (70, 853, 1130, 884))]),
    ('ex1-q4',  [(1, (70, 889, 1130, 921))]),
    ('ex1-q5',  [(1, (70, 926, 1130, 958))]),
    ('ex1-q6',  [(1, (70, 961, 1130, 1048))]),
    # q7 : paragraphe d'hypothèses qui la précède + question.
    ('ex1-q7',  [(1, (70, 1055, 1130, 1186))]),
    ('ex1-q8',  [(1, (70, 1188, 1130, 1219))]),
    ('ex1-q9',  [(1, (70, 1224, 1130, 1286))]),
    ('ex1-q10', [(1, (70, 1289, 1130, 1347))]),
    ('ex1-q11', [(1, (70, 1351, 1130, 1411))]),
    # q12 : paragraphe de notations + question, à cheval sur les deux pages.
    ('ex1-q12', [(1, (70, 1417, 1130, 1622)), (2, (80, 40, 1130, 115))]),
    ('ex1-q13', [(2, (80, 117, 1130, 152))]),
    ('ex1-q14', [(2, (80, 154, 1130, 189))]),
    ('ex1-q15', [(2, (80, 191, 1130, 226))]),
    ('ex1-q16', [(2, (80, 227, 1130, 287))]),
    ('ex1-q17', [(2, (80, 291, 1130, 327))]),
    ('ex2',     [(2, (80, 340, 1135, 447))]),
    ('ex2-q1',  [(2, (80, 449, 1135, 512))]),
    ('ex2-q2',  [(2, (80, 514, 1135, 577))]),
    ('ex2-q3',  [(2, (80, 579, 1135, 667))]),
    # q4 : paragraphe thermique qui la précède + question.
    ('ex2-q4',  [(2, (80, 672, 1135, 907))]),
    # q5 : texte puis réseau de courbes K(tp) (servant aussi aux q6 et q7).
    ('ex2-q5',  [(2, (95, 910, 676, 1078)), (2, (684, 914, 1136, 1330))]),
    ('ex2-q6',  [(2, (95, 1082, 676, 1172))]),
    ('ex2-q7',  [(2, (95, 1174, 676, 1292))]),
    ('ex3',     [(2, (80, 1327, 1135, 1480))]),
    ('ex3-q1',  [(2, (80, 1484, 1135, 1520))]),
    ('ex3-q2',  [(2, (80, 1523, 1135, 1582))]),
    ('ex3-q3',  [(2, (80, 1584, 1135, 1622))]),
]


def photo(page, tmp):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdfimages', '-png', '-f', str(page), '-l', str(page), PDF, base], check=True)
    return Image.open(base + '-000.png').convert('RGB')


def aplanir(im):
    """Fond blanc uniforme, encre bleue effacée, niveaux de gris contrastés."""
    rgb = np.asarray(im, float)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    gris = 0.299 * R + 0.587 * G + 0.114 * B
    g = Image.fromarray(gris.clip(0, 255).astype(np.uint8))
    fond = np.asarray(g.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)), float)
    a = gris / np.maximum(fond, 1)
    encre = ((B - R) > 12) & (a < 0.93)
    encre = np.asarray(Image.fromarray((encre * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
    a[encre] = 1.0
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
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: aplanir(photo(p, tmp)) for p in (1, 2)}
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
