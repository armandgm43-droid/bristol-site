#!/usr/bin/env python3
"""Découpe du partiel AU205 « Commande à temps discret » du 22 mai 2018 (session 1)
en images (énoncé commun, en-têtes de partie, une image par question ou sous-question).

Source : sources/auto1/annales/2017-2018-partiel-temps-discret.pdf (photographies
de 2 pages insérées dans un document Word). Pages rendues à 200 dpi avec pdftoppm
(1654 x 2339 px), en niveaux de gris. Le fond (gris, éclairage inégal, verso visible
par transparence) est normalisé : chaque pixel est divisé par une estimation locale du
fond (filtre max puis flou), puis le contraste est étiré.
Aucune annotation manuscrite.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/auto1-commande-systemes-lineaires/annales/sujets/2017-2018-partiel-temps-discret-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/auto1/annales/2017-2018-partiel-temps-discret.pdf')
NOM = '2017-2018-partiel-temps-discret'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400
ZONE = 11   # hauteur (px) de la zone de chevauchement entre lignes voisines

# (fichier, page, (x0, y0, x1, y1)[, bord]) ; coordonnées à 200 dpi.
# bord = 'haut' ou 'bas' : les lignes 6 c et 6 d se chevauchent (jambages) ; on efface
# les tracés qui touchent ce bord du cadre (ils appartiennent à la ligne voisine).
BOITES = [
    ('enonce',  1, (255, 680, 1420, 1098)),
    ('ex1',     1, (255, 1126, 1420, 1156)),
    ('ex1-q1',  1, (255, 1156, 1420, 1252)),
    ('ex1-q2',  1, (255, 1252, 1420, 1284)),
    ('ex1-q2a', 1, (255, 1284, 1420, 1314)),
    ('ex1-q2b', 1, (255, 1314, 1420, 1385)),
    ('ex1-q2c', 1, (255, 1385, 1420, 1416)),
    ('ex1-q3',  1, (255, 1416, 1420, 1447)),
    ('ex1-q4',  1, (255, 1447, 1420, 1480)),
    ('ex2',     1, (255, 1503, 1420, 1532)),
    ('ex2-q5',  1, (255, 1532, 1420, 1658)),
    ('ex2-q5a', 1, (255, 1678, 1420, 1714)),
    ('ex2-q5b', 1, (255, 1714, 1420, 1746)),
    ('ex2-q5c', 1, (255, 1746, 1420, 1806)),
    ('ex2-q6',  2, (255, 320, 1420, 495)),
    ('ex2-q6a', 2, (255, 495, 1420, 537)),
    ('ex2-q6b', 2, (255, 537, 1420, 602)),
    ('ex2-q6c', 2, (255, 602, 1420, 677), 'bas'),
    ('ex2-q6d', 2, (255, 662, 1420, 730), 'haut'),
    ('ex2-q7',  2, (255, 730, 1420, 762)),
    ('ex2-q8',  2, (255, 762, 1420, 800)),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    im = Image.open(base + '.png').convert('L')
    fond = im.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(25))
    g = np.asarray(im, float) / np.maximum(np.asarray(fond, float), 1)
    g = np.clip((g - 0.45) / (0.80 - 0.45), 0, 1)   # fond blanc, verso effacé
    return Image.fromarray((g * 255).astype(np.uint8))


def nettoyer_bord(im, bord, seuil=160):
    """Efface les tracés (composantes connexes sombres) qui touchent le bord indiqué."""
    b = im.point(lambda v: 0 if v < seuil else 255)
    y = 0 if bord == 'haut' else im.height - 1
    for x in range(im.width):
        if b.getpixel((x, y)) == 0:
            ImageDraw.floodfill(b, (x, y), 128)
    if bord == 'bas':
        # Dans la zone de chevauchement (ZONE dernières lignes), on ne garde que les
        # tracés qui se prolongent au-dessus (jambages de la ligne elle-même).
        y0 = im.height - 1 - ZONE
        for x in range(im.width):
            if b.getpixel((x, y0)) == 0:
                ImageDraw.floodfill(b, (x, y0), 64)
        z = np.asarray(b).copy()
        z[y0:][z[y0:] == 0] = 128
        b = Image.fromarray(z)
    a = np.asarray(im).copy()
    a[np.asarray(b) == 128] = 255
    return Image.fromarray(a)


def rogner(im, seuil=160, min_px=2):
    """Rogne au contenu puis ajoute une marge blanche."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in sorted({b[1] for b in BOITES})}
        for nom, p, b, *bord in BOITES:
            im = pages[p].crop(b)
            if bord:
                im = nettoyer_bord(im, bord[0])
            ims[nom] = rogner(im)
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
