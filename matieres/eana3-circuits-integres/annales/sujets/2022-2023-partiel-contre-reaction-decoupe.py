#!/usr/bin/env python3
"""Découpe du partiel EA211 « Circuits contre-réactionnés » du 16/11/2022 (« Un
circuit immunisé », F. Rivet) en images : énoncé commun, en-tête de chaque partie,
une image par question.

Sources : sources/eana3/annales/2022-2023-partiel-contre-reaction-p1.jpg et -p2.jpg
(photos 4032 x 3024 px, feuille couchée). Chaque photo est tournée d'un quart de
tour dans le sens horaire (3024 x 4032 px), passée en niveaux de gris, et son fond
inégal est corrigé (division par le fond estimé, contraste relevé pour les passages
pâles). La photo n'est pas redressée (légère perspective). Mise en page sur deux
colonnes (figure à gauche, questions à droite) : une image peut assembler plusieurs
morceaux empilés verticalement. Tous les morceaux sont réduits du même facteur
(0,58), puis les largeurs sont uniformisées (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2022-2023-partiel-contre-reaction-decoupe.py [racine] [dossier_sortie]
Dépendances : Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
JPG = os.path.join(RACINE, 'sources/eana3/annales/2022-2023-partiel-contre-reaction-p{}.jpg')
NOM = '2022-2023-partiel-contre-reaction'
PAGES = (1, 2)
MARGE = 15
ECART = 30        # espace entre deux morceaux empilés
LARGEUR_MAX = 1400
ECHELLE = 0.58     # même réduction pour tous les morceaux (texte à la même échelle)

G, D = 240, 2630           # pleine largeur
G2 = 120                   # bord gauche du bas de la page 2 (feuille de biais)
FG, FD = 270, 1530         # colonne de gauche (figures, page 1)
QG, QD = 1540, 2600        # colonne de droite (questions)
FD2, QG2 = 1640, 1645      # limite des colonnes, page 2
# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées sur la photo tournée.
BOITES = [
    ('intro',   [(1, (G, 880, D, 1470)), (1, (FG, 1570, FD, 3280))]),
    ('ex1',     [(1, (QG, 1580, QD, 1760))]),
    ('ex1-q1',  [(1, (QG, 1785, QD, 2530))]),
    ('ex1-q2',  [(1, (QG, 2540, QD, 3348)), (1, (G, 3346, D, 3540))]),
    ('ex1-q3',  [(2, (G, 250, D, 315))]),
    ('ex1-q4',  [(2, (G, 320, D, 460))]),
    ('ex1-q5',  [(2, (G, 465, D, 535))]),
    ('ex2',     [(2, (G, 630, 1300, 715)), (2, (G, 740, FD2, 1670)), (2, (G, 1800, FD2, 2555))]),
    ('ex2-q6',  [(2, (QG2, 730, QD, 1215))]),
    ('ex2-q7',  [(2, (QG2, 1220, QD, 1725))]),
    ('ex2-q8',  [(2, (QG2, 2000, QD, 2370))]),
    ('ex3',     [(2, (G2, 2695, 1300, 2790))]),
    ('ex3-q9',  [(2, (G2, 2815, D, 3145))]),
    ('ex3-q10', [(2, (G2, 3150, D, 3365))]),
]

CRAYON = {}


def page(num, tmp):
    im = Image.open(JPG.format(num)).convert('L').rotate(-90, expand=True)
    g = np.asarray(im, float)
    fond = np.asarray(im.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.GaussianBlur(50)), float)
    n = np.clip((g / np.maximum(fond, 1) - 0.45) / (0.93 - 0.45), 0, 1) ** 1.5
    return Image.fromarray((n * 255).astype(np.uint8))


def effacer_crayon(g, boite, gris=100, noir=50):
    """Blanchit les pixels gris (crayon) qui ne bordent pas un trait imprimé noir."""
    x0, y0, x1, y1 = boite
    zone = g[y0:y1, x0:x1]
    proche_noir = np.asarray(Image.fromarray(zone.astype(np.uint8)).filter(ImageFilter.MinFilter(7)), float) < noir
    zone[(zone >= gris) & ~proche_noir] = 255


def reduire(im):
    return im.resize((round(im.width * ECHELLE), round(im.height * ECHELLE)), Image.LANCZOS)


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
    h = sum(m.height for m in morceaux) + ECART * (len(morceaux) - 1)
    out = Image.new('L', (w, h), 255)
    y = 0
    for m in morceaux:
        out.paste(m, (0, y))
        y += m.height + ECART
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in PAGES}
        for nom, morceaux in BOITES:
            ims[nom] = empiler([rogner(reduire(pages[p].crop(b))) for p, b in morceaux])
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
