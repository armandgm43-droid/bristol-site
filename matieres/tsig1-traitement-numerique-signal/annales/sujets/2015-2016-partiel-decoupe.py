#!/usr/bin/env python3
"""Découpe du partiel TSIG1 (TS201) du 30/11/2015 en images (une par question).

Source : sources/tsig1/annales/2015-2016-partiel.pdf (2 pages, chacune = une photo
JPEG 1259 x 1679 px à 200 ppi). On extrait la photo de chaque page avec pdfimages,
on aplanit le fond (division par une estimation de l'éclairage), on efface les
annotations manuscrites à l'encre bleue (pixels plus bleus que rouges) et quelques
annotations au crayon (rectangles blanchis, voir BLANCHIR), puis on découpe.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig1-traitement-numerique-signal/annales/sujets/2015-2016-partiel-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig1/annales/2015-2016-partiel.pdf')
NOM = '2015-2016-partiel'
MARGE = 15

# Annotations d'étudiant non bleues à blanchir : page -> [(x0, y0, x1, y1)].
BLANCHIR = {
    1: [(268, 712, 425, 736),    # « n=-1 n=0 n=1 » sous x(n)
        (543, 708, 760, 740),    # « n=0 n=1 n=2 » sous h(n)
        (812, 1343, 868, 1402),  # « = z » sous H(e^{j2πf})
        (702, 698, 730, 712),    # reste du « 2 » manuscrit après l'accolade
        (670, 830, 1100, 905),   # traits et points autour du titre de l'exercice 2
        (700, 932, 1000, 968)],  # traits après « 13 Hz »
    2: [],
}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans la photo extraite.
BOITES = [
    ('ex1',    [(1, (60, 600, 1230, 800))]),
    ('ex2',    [(1, (60, 835, 1230, 980))]),
    ('ex2-q1', [(1, (60, 986, 1230, 1027))]),
    ('ex2-q2', [(1, (60, 1027, 1230, 1094))]),
    ('ex2-q3', [(1, (60, 1094, 1230, 1135))]),
    ('ex3',    [(1, (60, 1195, 1230, 1237))]),
    ('ex3-q1', [(1, (60, 1238, 1230, 1399))]),
    ('ex3-q2', [(1, (60, 1399, 1230, 1442))]),
    ('ex3-q3', [(1, (60, 1448, 1230, 1515))]),
    ('ex4',    [(2, (60, 68, 1230, 221))]),
    ('ex4-q1', [(2, (60, 222, 1230, 254))]),
    ('ex4-q2', [(2, (60, 254, 1230, 285))]),
    ('ex4-q3', [(2, (60, 285, 1230, 316))]),
    ('ex4-q4', [(2, (60, 316, 1230, 410))]),
    ('ex4-q5', [(2, (60, 410, 1230, 442))]),
    ('ex4-q6', [(2, (60, 442, 1230, 476))]),
    # Exercice 5 : texte puis schéma, empilés (le grand blanc intermédiaire est retiré).
    ('ex5',    [(2, (60, 525, 1150, 690)), (2, (60, 780, 1150, 1160))]),
]


def photo(page, tmp):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdfimages', '-png', '-f', str(page), '-l', str(page), PDF, base], check=True)
    return Image.open(base + '-000.png').convert('RGB')


def aplanir(im, page):
    """Fond blanc uniforme, encre bleue effacée, niveaux de gris contrastés."""
    rgb = np.asarray(im, float)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    gris = 0.299 * R + 0.587 * G + 0.114 * B
    g = Image.fromarray(gris.clip(0, 255).astype(np.uint8))
    fond = np.asarray(g.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)), float)
    a = gris / np.maximum(fond, 1)
    # Encre bleue : le papier et l'impression sont neutres ou rougeâtres (B < R).
    encre = ((B - R) > 4) & (a < 0.93)
    encre = np.asarray(Image.fromarray((encre * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
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


def enregistrer(im, chemin):
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)


def main():
    os.makedirs(SORTIE, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: aplanir(photo(p, tmp), p) for p in (1, 2)}
        for nom, morceaux in BOITES:
            ims = [rogner(pages[p].crop(b)) for p, b in morceaux]
            im = empiler(ims) if len(ims) > 1 else ims[0]
            chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
            enregistrer(im, chemin)
            print(chemin, im.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
