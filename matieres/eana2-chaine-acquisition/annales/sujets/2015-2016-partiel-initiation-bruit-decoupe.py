#!/usr/bin/env python3
"""Découpe de l'examen d'initiation aux bruits en électronique (EA222, rangé avec EANA2)
de l'année 2015-2016 (date non indiquée sur le sujet) en images (une par question).

Source : sources/eana2/annales/2015-2016-partiel-initiation-bruit.pdf (2 pages, chacune = une photo
JPEG 1259 x 1679 px à 200 ppi). On extrait la photo de chaque page avec pdfimages,
on aplanit le fond (division par une estimation de l'éclairage), on efface les
annotations d'étudiant à l'encre bleue (sources de bruit
entourées sur la figure de l'exercice II, calcul en marge) (pixels plus bleus que rouges), puis on découpe.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana2-chaine-acquisition/annales/sujets/2015-2016-partiel-initiation-bruit-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana2/annales/2015-2016-partiel-initiation-bruit.pdf')
NOM = '2015-2016-partiel-initiation-bruit'
MARGE = 15
LARGEUR_MAX = 1400

# Restes d'annotations manuscrites à blanchir : page -> [(x0, y0, x1, y1)].
BLANCHIR = {2: [(822, 1345, 960, 1500)]}   # calcul en marge des questions 4 et 5 de l'ex. III

# Fils de la figure de l'exercice II effacés avec les cercles manuscrits qui les
# recouvraient (« e1 », « eS », « e2 ») : retracés à l'identique (page 1, épaisseur 3 px).
RETRACER = {1: [((263, 1232), (372, 1232)), ((188, 1337), (188, 1471)), ((263, 1337), (263, 1471))]}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans la photo extraite.
BOITES = [
    ('ex1',    [(1, (60, 262, 1150, 302))]),
    ('ex1-q1', [(1, (60, 328, 1150, 785))]),
    ('ex1-q2', [(1, (60, 803, 1150, 892))]),
    # Exercice II : titre puis figure (servant aux deux questions).
    ('ex2',    [(1, (60, 948, 1150, 988)), (1, (70, 1172, 1022, 1578))]),
    ('ex2-q1', [(1, (60, 998, 1150, 1072))]),
    ('ex2-q2', [(1, (60, 1088, 1150, 1162))]),
    ('ex3',    [(2, (40, 185, 1148, 882))]),
    ('ex3-q1', [(2, (50, 945, 1135, 990))]),
    ('ex3-q2', [(2, (50, 1046, 1135, 1122))]),
    ('ex3-q3', [(2, (50, 1182, 1135, 1250))]),
    ('ex3-q4', [(2, (50, 1306, 1135, 1372))]),
    ('ex3-q5', [(2, (50, 1430, 1135, 1474))]),
    ('ex3-q6', [(2, (50, 1535, 1135, 1602))]),
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
    encre = ((B - R) > 5) & (a < 0.93)
    encre = np.asarray(Image.fromarray((encre * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(7))) > 0
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
    for p, im in pages.items():
        d = ImageDraw.Draw(im)
        for b in BLANCHIR.get(p, []):
            d.rectangle(b, fill=255)
        for a, b in RETRACER.get(p, []):
            d.line([a, b], fill=0, width=3)
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
