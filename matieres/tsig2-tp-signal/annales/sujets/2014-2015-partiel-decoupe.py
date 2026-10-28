#!/usr/bin/env python3
"""Découpe du partiel de TP TS202 (TSIG2) 2014-2015 en images (une par question).

Source : sources/tsig2/annales/2014-2015-partiel.pdf (2 pages, chacune = une photo
JPEG 1259 x 1679 px à 200 ppi). On extrait la photo de chaque page avec pdfimages,
on aplanit le fond (division par une estimation de l'éclairage), on blanchit les
coches manuscrites d'un étudiant (rectangles BLANCHIR), puis on découpe.
L'en-tête du sujet (consignes d'envoi avec adresse électronique et mots de passe)
n'est volontairement pas reproduit.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig2-tp-signal/annales/sujets/2014-2015-partiel-decoupe.py [racine] [dossier_sortie]
Par défaut : racine = dossier courant, sortie = dossier de ce script.
Dépendances : poppler-utils (pdfimages), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/tsig2/annales/2014-2015-partiel.pdf')
NOM = '2014-2015-partiel'
MARGE = 15
LARGEUR_MAX = 1400

# Coches manuscrites (crayon noir) devant les questions de la page 2.
BLANCHIR = {
    1: [],
    2: [(200, 752, 257, 802), (200, 842, 245, 892), (200, 918, 246, 966),
        (200, 984, 245, 1036), (198, 1104, 245, 1157), (212, 1258, 253, 1312),
        (222, 1308, 266, 1358)],
}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées dans la photo extraite.
BOITES = [
    ('ex1',    [(1, (185, 690, 1070, 740))]),
    ('ex1-q1', [(1, (215, 742, 1070, 1160))]),
    ('ex1-q2', [(1, (215, 1172, 1070, 1236))]),
    ('ex1-q3', [(1, (215, 1252, 1070, 1416))]),
    ('ex1-q4', [(1, (215, 1434, 1070, 1545))]),
    ('ex1-q5', [(2, (225, 185, 1075, 412))]),
    ('ex1-q6', [(2, (225, 412, 1075, 495))]),
    ('ex2',    [(2, (205, 550, 1075, 752))]),
    ('ex2-q1', [(2, (205, 760, 1075, 825))]),
    ('ex2-q2', [(2, (205, 842, 1075, 905))]),
    ('ex2-q3', [(2, (205, 920, 1075, 965))]),
    ('ex2-q4', [(2, (205, 980, 1075, 1092))]),
    ('ex2-q5', [(2, (205, 1106, 1075, 1172))]),
    ('ex2-p2', [(2, (205, 1185, 1075, 1250))]),
    ('ex2-q6', [(2, (205, 1262, 1075, 1300))]),
    ('ex2-q7', [(2, (205, 1312, 1075, 1356))]),
]


def photo(page, tmp):
    base = os.path.join(tmp, f'p{page}')
    subprocess.run(['pdfimages', '-png', '-f', str(page), '-l', str(page), PDF, base], check=True)
    return Image.open(base + '-000.png').convert('L')


def aplanir(g, page):
    """Fond blanc uniforme, annotations blanchies, niveaux de gris contrastés."""
    gris = np.asarray(g, float)
    fond = np.asarray(g.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)), float)
    a = gris / np.maximum(fond, 1)
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
        pages = {p: aplanir(photo(p, tmp), p) for p in (1, 2)}
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
