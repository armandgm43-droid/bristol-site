#!/usr/bin/env python3
"""Découpe du partiel EA207 (EAEP1) du 22/12/2017 en images (une par question).

Source : sources/eaep1/annales/2017-2018-partiel.pdf (2 pages, chacune = une photo
JPEG 1259 x 1679 px à 200 ppi). On extrait la photo de chaque page avec pdfimages,
on aplanit le fond (division par une estimation de l'éclairage), on efface les
annotations d'étudiant à l'encre bleue (chronogramme
à droite de la figure 1, mot en marge, retouches) (pixels plus bleus que rouges), puis on découpe.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eaep1-conversion-energie/annales/sujets/2017-2018-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eaep1/annales/2017-2018-partiel.pdf')
NOM = '2017-2018-partiel'
MARGE = 15
LARGEUR_MAX = 1400

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans la photo extraite.
# Un seul problème (parties A à D) : énoncé général « ex1 », en-tête de la partie D
# « ex1-d », questions numérotées comme dans le sujet (1 à 22).
BOITES = [
    # Titre, présentation et figure 1 (le chronogramme manuscrit à droite est exclu).
    ('ex1',     [(1, (95, 400, 1125, 640)), (1, (95, 640, 912, 832))]),
    ('ex1-q1',  [(1, (100, 862, 1125, 920))]),
    ('ex1-q2',  [(1, (100, 924, 1125, 957))]),
    ('ex1-q3',  [(1, (100, 961, 1125, 1021))]),
    ('ex1-q4',  [(1, (100, 1024, 1125, 1057))]),
    ('ex1-q5',  [(1, (100, 1061, 1125, 1152))]),
    ('ex1-q6',  [(1, (100, 1154, 1125, 1237))]),
    ('ex1-q7',  [(1, (100, 1240, 1125, 1274))]),
    ('ex1-q8',  [(1, (100, 1279, 1125, 1447))]),
    ('ex1-q9',  [(1, (100, 1503, 1125, 1537))]),
    ('ex1-q10', [(1, (100, 1539, 1125, 1597))]),
    ('ex1-q11', [(2, (60, 96, 1090, 187))]),
    ('ex1-q12', [(2, (60, 196, 1090, 307))]),
    ('ex1-q13', [(2, (60, 313, 1090, 397))]),
    ('ex1-q14', [(2, (60, 403, 1090, 492))]),
    ('ex1-q15', [(2, (60, 498, 1090, 557))]),
    ('ex1-q16', [(2, (60, 563, 1090, 622))]),
    ('ex1-d',   [(2, (60, 648, 1090, 1067))]),
    ('ex1-q17', [(2, (60, 1073, 1090, 1107))]),
    ('ex1-q18', [(2, (60, 1109, 1090, 1224))]),
    ('ex1-q19', [(2, (60, 1228, 1090, 1344))]),
    ('ex1-q20', [(2, (60, 1348, 1090, 1462))]),
    ('ex1-q21', [(2, (60, 1468, 1090, 1582))]),
    ('ex1-q22', [(2, (60, 1586, 1090, 1620))]),
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
    encre = ((B - R) > 6) & (a < 0.93)
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
