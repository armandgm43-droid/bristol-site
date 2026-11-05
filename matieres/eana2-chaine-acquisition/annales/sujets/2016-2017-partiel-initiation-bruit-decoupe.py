#!/usr/bin/env python3
"""Découpe de l'examen d'initiation aux bruits en électronique (EA222, rangé avec EANA2)
de l'année 2016-2017 (date non indiquée sur le sujet) en images (une par question).

Source : sources/eana2/annales/2016-2017-partiel-initiation-bruit.pdf (2 pages, chacune = une photo
JPEG 1259 x 1679 px à 200 ppi). On extrait la photo de chaque page avec pdfimages,
on aplanit le fond (division par une estimation de l'éclairage), on efface les
annotations d'étudiant à l'encre bleue (sources de bruit
entourées sur la figure de l'exercice II, calcul en marge) (pixels plus bleus que rouges), puis on découpe.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana2-chaine-acquisition/annales/sujets/2016-2017-partiel-initiation-bruit-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana2/annales/2016-2017-partiel-initiation-bruit.pdf')
NOM = '2016-2017-partiel-initiation-bruit'
MARGE = 15
LARGEUR_MAX = 1400

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans la photo extraite.
# L'exercice II du sujet n'a pas de question 2 : les numéros du sujet sont conservés.
BOITES = [
    # Consigne et formules fournies, puis titre de l'exercice I.
    ('ex1',    [(1, (55, 238, 1100, 582)), (1, (60, 593, 1150, 628))]),
    ('ex1-q1', [(1, (60, 644, 1150, 987))]),
    # Exercice II : titre puis figure (servant aux deux questions).
    ('ex2',    [(1, (60, 1003, 1150, 1038)), (1, (60, 1180, 1032, 1600))]),
    ('ex2-q1', [(1, (60, 1052, 1150, 1147))]),
    ('ex2-q3', [(1, (60, 1150, 1150, 1182))]),
    ('ex3',    [(2, (25, 183, 1172, 907))]),
    ('ex3-q1', [(2, (45, 976, 1165, 1017))]),
    ('ex3-q2', [(2, (45, 1032, 1165, 1068))]),
    ('ex3-q3', [(2, (45, 1082, 1165, 1147))]),
    ('ex3-q4', [(2, (45, 1158, 1165, 1227))]),
    ('ex3-q5', [(2, (45, 1238, 1165, 1307))]),
    ('ex3-q6', [(2, (45, 1322, 1165, 1362))]),
    ('ex3-q7', [(2, (45, 1382, 1165, 1442))]),
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
