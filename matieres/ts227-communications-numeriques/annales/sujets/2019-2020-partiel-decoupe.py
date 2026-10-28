#!/usr/bin/env python3
"""Découpe du partiel TS227 2019-2020 en images (une par question).

Source : sources/ts227/annales/2019-2020-partiel.pdf (scan couleur à 300 ppp, 3 pages,
sans annotation ; le verso transparaît légèrement). Pages rendues à 200 dpi avec
pdftoppm, puis passées en niveaux de gris : fond aplani (division par une estimation de
l'éclairage) et seuil qui efface la transparence du verso. Le scan est droit : pas de
redressement (pentes nulles). Les largeurs sont uniformisées à la fin (marge blanche à
droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/ts227-communications-numeriques/annales/sujets/2019-2020-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/ts227/annales/2019-2020-partiel.pdf')
NOM = '2019-2020-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Pente du texte (dy/dx, positive si la ligne descend vers la droite) en fonction de y.
PENTES = {1: [(0, 0.0), (2339, 0.0)], 2: [(0, 0.0), (2339, 0.0)], 3: [(0, 0.0), (2339, 0.0)]}
X_CENTRE = 815

# Annotations à blanchir en plus de l'encre colorée : page -> [(x0, y0, x1, y1)]
# (coordonnées après redressement).
BLANCHIR = {1: [], 2: [], 3: []}

BOITES = [
    ('ex1',       [(1, (225, 752, 1420, 803))]),
    ('ex1-q1',    [(1, (225, 823, 1420, 888))]),
    ('ex1-q2',    [(1, (225, 917, 1420, 983)), (1, (250, 1888, 1420, 1917))]),   # + note 1
    ('ex1-q3',    [(1, (225, 1011, 1420, 1118)), (1, (250, 1917, 1420, 1946))]), # + note 2
    ('ex1-q4',    [(1, (225, 1140, 1420, 1213))]),
    ('ex1-q5',    [(1, (225, 1234, 1420, 1305))]),
    ('ex1-q6',    [(1, (225, 1329, 1420, 1461))]),
    ('ex2',       [(1, (225, 1515, 1420, 1623))]),
    ('ex2-q7',    [(1, (225, 1644, 1420, 1749))]),
    ('ex2-q8',    [(1, (225, 1773, 1420, 1877))]),
    ('ex2-q9',    [(2, (225, 272, 1420, 548)), (2, (225, 829, 1420, 1064))]),    # + formule de Bennett
    ('ex2-q10',   [(2, (225, 571, 1420, 644))]),
    ('ex2-q11',   [(2, (225, 666, 1420, 799))]),
    # Exercice 2 : titre, énoncé, figure 1 (page 3), figures 2 et 3 (page 3).
    ('ex3',       [(2, (225, 1114, 1420, 1590)), (3, (225, 345, 1530, 996)),
                   (3, (260, 1192, 1530, 1840))]),
    ('ex3-q12',   [(2, (225, 1617, 1420, 1688))]),
    ('ex3-q13',   [(2, (225, 1713, 1420, 1817))]),
]


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-png', PDF, base], check=True)
    return Image.open(base + '.png').convert('RGB')


def nettoyer(im):
    """Fond blanc uniforme, encre bleue et surligneur rose effacés, niveaux de gris."""
    rgb = np.asarray(im, float)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    gris = 0.299 * R + 0.587 * G + 0.114 * B
    rose = ((R - G) > 15) & ((R - B) > 10)
    gris[rose] = np.maximum(np.maximum(R, G), B)[rose]
    g = Image.fromarray(gris.clip(0, 255).astype(np.uint8))
    fond = np.asarray(g.filter(ImageFilter.MaxFilter(31)).filter(ImageFilter.GaussianBlur(30)), float)
    a = gris / np.maximum(fond, 1)
    a[rose & (a > 0.7)] = 1.0          # voile laissé par le surligneur
    encre = ((B - R) > 12) & (a < 0.9)
    encre = np.asarray(Image.fromarray((encre * 255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))) > 0
    a[encre] = 1.0
    a = np.clip((a - 0.40) / (0.80 - 0.40), 0, 1) ** 1.3
    return Image.fromarray((a * 255).astype(np.uint8))


def redresser(im, points):
    """Cisaillement vertical : la ligne de pente s(y) devient horizontale."""
    a = np.asarray(im, float)
    H, W = a.shape
    ys, ss = zip(*points)
    s = np.interp(np.arange(H), ys, ss)                  # pente pour chaque ligne
    dx = np.arange(W) - X_CENTRE
    src = np.arange(H)[:, None] + s[:, None] * dx[None, :]
    y0 = np.clip(np.floor(src).astype(int), 0, H - 2)
    t = np.clip(src - y0, 0, 1)
    cols = np.arange(W)[None, :]
    out = a[y0, cols] * (1 - t) + a[y0 + 1, cols] * t
    out[(src < 0) | (src > H - 1)] = 255
    return Image.fromarray(out.clip(0, 255).astype(np.uint8))


def preparer(num, tmp):
    im = redresser(nettoyer(page(num, tmp)), PENTES[num])
    a = np.asarray(im).copy()
    for x0, y0, x1, y1 in BLANCHIR.get(num, []):
        a[y0:y1, x0:x1] = 255
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


def empiler(ims):
    w = max(i.width for i in ims)
    out = Image.new('L', (w, sum(i.height for i in ims)), 255)
    y = 0
    for i in ims:
        out.paste(i, (0, y))
        y += i.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: preparer(p, tmp) for p in PENTES}
        if os.environ.get('PAGES_DIR'):              # contrôle : pages nettoyées entières
            for p, im in pages.items():
                im.save(os.path.join(os.environ['PAGES_DIR'], f'{NOM}-page{p}.png'))
        ims = {}
        for nom, morceaux in BOITES:
            parts = [rogner(pages[p].crop(b)) for p, b in morceaux]
            ims[nom] = empiler(parts) if len(parts) > 1 else parts[0]
    if not ims:
        return
    for nom, im in ims.items():
        if im.width > LARGEUR_MAX:
            ims[nom] = im.resize((LARGEUR_MAX, round(im.height * LARGEUR_MAX / im.width)), Image.LANCZOS)
    wmax = max(i.width for i in ims.values())
    for nom, im in ims.items():
        fond = Image.new('L', (wmax, im.height), 255)
        fond.paste(im, (0, 0))
        chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
        fond.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)
        print(chemin, fond.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
