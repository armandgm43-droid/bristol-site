#!/usr/bin/env python3
"""Découpe du partiel TS227 2017-2018 en images (une par question).

Source : sources/ts227/annales/2017-2018-partiel.pdf (2 pages ; chaque page est une
photo JPEG d'une feuille imprimée, sans annotation). Pages rendues à 200 dpi avec
pdftoppm, puis passées en niveaux de gris : fond aplani (division par une estimation de
l'éclairage) et redressement par un cisaillement vertical dont la pente varie avec la
hauteur (PENTES, mesurées sur les lignes de texte). Le sujet s'arrête au bas de la
page 2 (code Matlab « % Emetteur (à faire...) ») : la suite n'a pas été photographiée.
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/ts227-communications-numeriques/annales/sujets/2017-2018-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/ts227/annales/2017-2018-partiel.pdf')
NOM = '2017-2018-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Pente du texte (dy/dx, positive si la ligne descend vers la droite) en fonction de y.
PENTES = {
    1: [(450, -0.011), (550, -0.008), (650, -0.008), (750, -0.003), (850, -0.003),
        (950, -0.001), (1150, -0.001), (1250, 0.002), (1450, 0.002), (1550, 0.006)],
    2: [(350, 0.002), (550, 0.002), (650, 0.005), (750, 0.007), (950, 0.008),
        (1050, 0.009), (1150, 0.011), (1250, 0.012), (1650, 0.012)],
}
X_CENTRE = 815

# Annotations à blanchir en plus de l'encre colorée : page -> [(x0, y0, x1, y1)]
# (coordonnées après redressement).
BLANCHIR = {1: [], 2: []}

BOITES = [
    ('notations', [(1, (320, 738, 1320, 1008))]),
    ('ex1',       [(1, (320, 1040, 1320, 1083))]),
    ('ex1-q1',    [(1, (320, 1095, 1320, 1155))]),
    ('ex1-q2',    [(1, (320, 1157, 1320, 1188))]),
    ('ex1-q3',    [(1, (320, 1190, 1320, 1222))]),
    ('ex1-q4',    [(1, (320, 1224, 1320, 1254))]),
    ('ex1-q5',    [(1, (320, 1257, 1320, 1289))]),
    ('ex1-q6',    [(1, (320, 1291, 1320, 1342))]),
    ('ex1-q7',    [(1, (320, 1347, 1320, 1403))]),
    ('ex1-q8',    [(1, (320, 1406, 1320, 1437))]),
    ('ex1-q9',    [(1, (320, 1439, 1320, 1494))]),
    ('ex1-q10',   [(1, (320, 1496, 1320, 1527))]),
    ('ex1-q11',   [(1, (320, 1529, 1320, 1583))]),
    ('ex1-q12',   [(1, (320, 1586, 1320, 1618))]),
    ('ex1-q13',   [(2, (320, 362, 1320, 455)), (2, (320, 458, 1320, 522))]),   # définition de s_l + q. 13
    ('ex1-q14',   [(2, (320, 524, 1320, 589))]),
    ('ex1-q15',   [(2, (320, 591, 1320, 681)), (2, (320, 954, 1320, 1140))]),  # q. 15 + formule de Bennett
    ('ex1-q16',   [(2, (320, 683, 1320, 745))]),
    ('ex1-q17',   [(2, (320, 747, 1320, 889))]),
    ('ex1-q18',   [(2, (320, 892, 1320, 950))]),
    ('ex2',       [(2, (320, 1168, 1320, 1210))]),
    ('ex2-q1',    [(2, (320, 1222, 1320, 1692))]),
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
    a = np.clip((a - 0.45) / (0.85 - 0.45), 0, 1) ** 1.3
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
