#!/usr/bin/env python3
"""Découpe du partiel AU201 « Commande linéaire et approches linéarisantes » (6 janvier 2015) en images (une par question).

Source : sources/auto1/annales/2014-2015-partiel-commande-lineaire.pdf (photo de 2 pages, éclairage non uniforme). Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris.
Fond aplati (division par le fond lissé), puis contraste rehaussé.
Les largeurs sont uniformisées à la fin (marge blanche à droite), PNG 16 niveaux de gris.

Usage (depuis la racine du projet Bristol) :
    python3 matieres/auto1-commande-systemes-lineaires/annales/sujets/2014-2015-partiel-commande-lineaire-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/auto1/annales/2014-2015-partiel-commande-lineaire.pdf')
NOM = '2014-2015-partiel-commande-lineaire'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400
APLATIR = True      # True : photo, on divise par le fond lissé (éclairage non uniforme)
NOIR, BLANC = 90, 205   # niveaux ramenés au noir et au blanc

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
# Plusieurs morceaux sont empilés verticalement (question à cheval sur deux pages).
BOITES = [
    ('enonce', [(1, (300, 610, 1400, 1002))]),
    ('ex1',    [(1, (300, 1025, 1400, 1302))]),
    ('ex2',    [(1, (300, 1326, 1400, 1532))]),
    ('ex2-q1', [(1, (300, 1552, 1400, 1690))]),
    ('ex2-q2', [(2, (300, 345, 1400, 660))]),
    ('ex2-q3', [(2, (300, 677, 1400, 716))]),
    ('ex2-q4', [(2, (300, 735, 1400, 802))]),
    ('ex3',    [(2, (300, 820, 1400, 882))]),
    ('ex3-q1', [(2, (300, 905, 1400, 966))]),
    ('ex3-q2', [(2, (300, 990, 1400, 1057))]),
    ('ex3-q3', [(2, (300, 1074, 1400, 1140))]),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    im = Image.open(base + '.png').convert('L')
    g = np.asarray(im, float)
    if APLATIR:
        petit = im.resize((im.width // 8, im.height // 8))
        fond = petit.filter(ImageFilter.MaxFilter(9)).filter(ImageFilter.GaussianBlur(4))
        fond = np.asarray(fond.resize(im.size, Image.BILINEAR), float)
        g = 255 * g / np.maximum(fond, 1)
    g = np.clip((g - NOIR) / (BLANC - NOIR), 0, 1)
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
    if len(morceaux) == 1:
        return morceaux[0]
    w = max(m.width for m in morceaux)
    out = Image.new('L', (w, sum(m.height for m in morceaux)), 255)
    y = 0
    for m in morceaux:
        out.paste(m, (0, y)); y += m.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        nums = sorted({p for _, ms in BOITES for p, _ in ms})
        pages = {p: page(p, tmp) for p in nums}
        for nom, morceaux in BOITES:
            ims[nom] = empiler([rogner(pages[p].crop(b)) for p, b in morceaux])
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
