#!/usr/bin/env python3
"""Découpe du partiel EA210 « Circuits HF et oscillateurs » du 14/11/2017 en images
(une par question) : amplificateur à grand gain en technologie CMOS (trois montages).

Source : sources/eana3/annales/2017-2018-partiel-circuits-hf-oscillateurs.pdf (photo
d'une feuille, 1 page, image native de 1386 x 1848 px). Page rendue à 200 dpi avec
pdftoppm (1654 x 2339 px), en niveaux de gris. L'éclairage de la photo est inégal : le
fond est estimé par un filtre maximum sur l'image réduite, puis divisé (aplatissement),
avant de ramener les niveaux au noir et au blanc. Le soulignement au stylo d'un étudiant
(« mais nous ne la négligerons pas pour les PMOS ») est effacé (EFFACER). Une image peut
être formée de plusieurs morceaux empilés verticalement (en-tête : énoncé puis figure des
trois montages). Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2017-2018-partiel-circuits-hf-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana3/annales/2017-2018-partiel-circuits-hf-oscillateurs.pdf')
NOM = '2017-2018-partiel-circuits-hf'
MARGE = 15
DPI = 200
NOIR, BLANC = 0.30, 0.80       # niveaux (rapport au fond) ramenés au noir et au blanc

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('ex1',        [(1, (285, 665, 1320, 888)), (1, (490, 1485, 1150, 1850))]),
    ('ex1-q1-1',   [(1, (290, 895, 1320, 932))]),
    ('ex1-q1-2',   [(1, (290, 945, 1320, 1058)), (1, (290, 1068, 1320, 1135))]),
    ('ex1-q1-3',   [(1, (290, 1148, 1320, 1213))]),
    ('ex1-q1-4-1', [(1, (290, 1225, 1320, 1311))]),
    ('ex1-q1-4-2', [(1, (290, 1311, 1320, 1337))]),
    ('ex1-q1-4-3', [(1, (290, 1337, 1320, 1363))]),
    ('ex1-q1-4-4', [(1, (290, 1363, 1320, 1420))]),
    ('ex1-q1-4-5', [(1, (290, 1420, 1320, 1447))]),
    ('ex1-q1-4-6', [(1, (290, 1447, 1320, 1476))]),
]

# Rectangles remis en blanc (annotations manuscrites) ; coordonnées à 200 dpi.
EFFACER = {
    1: [(915, 845, 1320, 860), (285, 878, 365, 890)],
}


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    im = Image.open(base + '.png').convert('L')
    petit = im.resize((im.width // 8, im.height // 8), Image.BILINEAR)
    fond = petit.filter(ImageFilter.MaxFilter(5)).filter(ImageFilter.GaussianBlur(1))
    fond = np.asarray(fond.resize(im.size, Image.BILINEAR), float)
    g = np.asarray(im, float) / np.maximum(fond, 1)
    g = np.clip((g - NOIR) / (BLANC - NOIR), 0, 1)
    for x0, y0, x1, y1 in EFFACER.get(num, []):
        g[y0:y1, x0:x1] = 1
    return Image.fromarray((g * 255).astype(np.uint8))


def rogner(im, seuil=160, min_px=2):
    """Rogne au contenu puis ajoute une marge blanche."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def empiler(morceaux):
    """Empile verticalement des morceaux rognés, alignés à gauche."""
    if len(morceaux) == 1:
        return morceaux[0]
    out = Image.new('L', (max(m.width for m in morceaux), sum(m.height for m in morceaux)), 255)
    y = 0
    for m in morceaux:
        out.paste(m, (0, y))
        y += m.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in sorted({p for _, ms in BOITES for p, _ in ms})}
        for nom, morceaux in BOITES:
            ims[nom] = empiler([rogner(pages[p].crop(b)) for p, b in morceaux])
    wmax = min(1400, max(i.width for i in ims.values()))
    for nom, im in ims.items():
        if im.width > 1400:
            im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
        fond = Image.new('L', (wmax, im.height), 255)
        fond.paste(im, (0, 0))
        chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
        fond.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)
        print(chemin, fond.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
