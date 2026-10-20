#!/usr/bin/env python3
"""Découpe du partiel TSIG1 (TS201) du 13/12/2017 en images (une par question).

Source : sources/tsig1/annales/2017-2018-partiel.pdf (3 pages, chacune = une photo
JPEG 1259 x 1679 px à 200 ppi). On extrait la photo de chaque page avec pdfimages,
on aplanit le fond (division par une estimation de l'éclairage), on passe en
niveaux de gris contrastés, on redresse légèrement si besoin, puis on découpe.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig1-traitement-numerique-signal/annales/sujets/2017-2018-partiel-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig1/annales/2017-2018-partiel.pdf')
NOM = '2017-2018-partiel'
MARGE = 15

# (fichier, [(page, (x0, y0, x1, y1), angle en degrés), ...]) ; coordonnées dans la
# photo extraite (1259 x 1679), angle de redressement (rotation PIL, sens trigo).
# Plusieurs morceaux = empilés verticalement (énoncé à cheval sur deux pages).
BOITES = [
    ('ex1',    [(1, (95, 545, 1170, 1152), -0.6)]),
    ('ex1-q1', [(1, (190, 1168, 700, 1200), 0)]),
    ('ex1-q2', [(1, (190, 1200, 700, 1230), 0)]),
    ('ex1-q3', [(1, (190, 1230, 700, 1262), 0)]),
    ('ex2',    [(1, (120, 1395, 1165, 1603), 0), (2, (85, 30, 1175, 392), -0.6)]),
    ('ex2-q1', [(2, (170, 412, 720, 462), 0)]),
    ('ex2-q2', [(2, (170, 472, 720, 522), 0)]),
    ('ex3',    [(2, (95, 655, 1185, 1382), 0)]),
    ('ex3-q1', [(2, (180, 1428, 1060, 1461), 0)]),
    ('ex3-q2', [(2, (180, 1461, 1060, 1490), 0)]),
    ('ex3-q3', [(2, (180, 1490, 1060, 1520), 0)]),
    ('ex3-q4', [(2, (180, 1520, 1060, 1558), 0)]),
    ('ex4',    [(3, (80, 85, 1140, 550), 0)]),
    ('ex4-q1', [(3, (140, 550, 1145, 622), 0)]),
    ('ex4-q2', [(3, (140, 624, 1145, 692), 0)]),
    ('ex4-q3', [(3, (140, 693, 1145, 762), 0)]),
    ('ex4-q4', [(3, (140, 764, 1145, 794), 0)]),
    ('ex4-q5', [(3, (140, 794, 1145, 826), 0)]),
]


# Taches isolées du scan à effacer (page, boîte) : point parasite après « suit : ».
EFFACER = [(1, (845, 1572, 868, 1592))]


def photo(page, tmp):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdfimages', '-png', '-f', str(page), '-l', str(page), PDF, base], check=True)
    return Image.open(base + '-000.png')


def aplanir(im):
    """Fond blanc uniforme : division par l'éclairage estimé, puis niveaux."""
    g = im.convert('L')
    w, h = g.size
    fond = (g.resize((w // 8, h // 8), Image.BILINEAR)
             .filter(ImageFilter.MaxFilter(7)).filter(ImageFilter.GaussianBlur(3))
             .resize((w, h), Image.BILINEAR))
    a = np.asarray(g, float) / np.maximum(np.asarray(fond, float), 1)
    a = np.clip((a - 0.35) / (0.82 - 0.35), 0, 1)
    return Image.fromarray((a * 255).astype(np.uint8))


def morceau(page_im, boite, angle):
    x0, y0, x1, y1 = boite
    if angle:
        p = 40  # marge pour la rotation autour du centre de la boîte
        grand = page_im.crop((x0 - p, y0 - p, x1 + p, y1 + p))
        grand = grand.rotate(angle, resample=Image.BICUBIC, fillcolor=255)
        return grand.crop((p, p, p + x1 - x0, p + y1 - y0))
    return page_im.crop(boite)


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


def enregistrer(im, chemin):
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: aplanir(photo(p, tmp)) for p in (1, 2, 3)}
        for p, b in EFFACER:
            pages[p].paste(255, b)
        for nom, morceaux in BOITES:
            ims = [rogner(morceau(pages[p], b, a)) for p, b, a in morceaux]
            im = empiler(ims) if len(ims) > 1 else ims[0]
            chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
            enregistrer(im, chemin)
            print(chemin, im.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
