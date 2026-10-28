#!/usr/bin/env python3
"""Découpe du partiel TS227 2018-2019 en images (une par question).

Source : sources/ts227/annales/2018-2019-partiel-p1.jpg, -p2.jpg, -p3.jpg (photos au
téléphone, 1080 x 1920 px, sans annotation). Chaque photo est lue avec Pillow et passée
en niveaux de gris : fond aplani (division par une estimation de l'éclairage) et
redressement par un cisaillement vertical dont la pente varie avec la hauteur (PENTES,
mesurées sur les lignes de texte ; la feuille est photographiée en perspective).
La résolution des photos est faible (environ 130 ppp) : les images sont agrandies d'un
facteur 1,5 avant le rognage pour garder une taille de texte comparable aux autres
annales. Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/ts227-communications-numeriques/annales/sujets/2018-2019-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : Pillow, numpy.
"""
import os, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PHOTO = os.path.join(RACINE, 'sources/ts227/annales/2018-2019-partiel-p{}.jpg')
ECHELLE = 1.5
NOM = '2018-2019-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Pente du texte (dy/dx, positive si la ligne descend vers la droite) en fonction de y.
PENTES = {
    1: [(450, 0.003), (550, 0.006), (650, 0.007), (750, 0.012), (850, 0.015), (950, 0.015),
        (1050, 0.019), (1150, 0.021), (1250, 0.022), (1350, 0.026)],
    2: [(350, 0.007), (450, 0.008), (550, 0.016), (650, 0.027), (850, 0.027), (1050, 0.026),
        (1150, 0.024), (1350, 0.025)],
    3: [(350, -0.003), (450, -0.003), (550, -0.007)],
}
X_CENTRE = 570

# Annotations à blanchir en plus de l'encre colorée : page -> [(x0, y0, x1, y1)]
# (coordonnées après redressement).
BLANCHIR = {1: [], 2: [], 3: []}

BOITES = [
    ('notations', [(1, (195, 630, 945, 788))]),
    ('ex1',       [(1, (195, 811, 945, 845))]),
    ('ex1-q1',    [(1, (195, 854, 945, 881))]),
    ('ex1-q2',    [(1, (195, 885, 945, 912))]),
    ('ex1-q3',    [(1, (195, 915, 945, 962))]),
    ('ex1-q4',    [(1, (195, 966, 945, 992))]),
    ('ex1-q5',    [(1, (195, 996, 945, 1040))]),
    ('ex1-q6',    [(1, (195, 1047, 945, 1073))]),
    ('ex1-q7',    [(1, (195, 1077, 945, 1124))]),
    ('ex1-q8',    [(1, (195, 1127, 945, 1154))]),
    ('ex1-q9',    [(1, (195, 1157, 945, 1204))]),
    ('ex1-q10',   [(1, (195, 1208, 945, 1234))]),
    ('ex1-q11',   [(1, (195, 1238, 945, 1264))]),
    ('ex1-q12',   [(1, (195, 1268, 945, 1315))]),
    ('ex1-q13',   [(1, (195, 1319, 945, 1369))]),
    # Exercice : titre et énoncé, puis la figure 1 (au-dessus sur la page).
    ('ex2',       [(2, (165, 781, 905, 922)), (2, (170, 352, 905, 760))]),
    ('ex2-q14',   [(2, (165, 933, 905, 979))]),
    ('ex2-q15',   [(2, (165, 990, 905, 1128))]),
    ('ex2-q16',   [(2, (165, 1139, 905, 1278))]),
    ('ex2-q17',   [(2, (160, 1289, 905, 1316))]),
    ('ex2-q18',   [(2, (160, 1327, 905, 1355))]),
    ('ex2-q19',   [(3, (155, 336, 915, 514))]),
    ('ex2-q20',   [(3, (155, 521, 915, 596))]),
]


def page(num, tmp):
    return Image.open(PHOTO.format(num)).convert('RGB')


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


def agrandir(im):
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
            parts = [rogner(agrandir(pages[p].crop(b))) for p, b in morceaux]
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
