#!/usr/bin/env python3
"""Découpe du partiel TS227 2015-2016 en images (une par question).

Source : sources/ts227/annales/2015-2016-partiel.pdf (3 pages ; chaque page est une
photo JPEG d'une feuille imprimée). Pages rendues à 200 dpi avec pdftoppm, en couleur
pour repérer les annotations d'un étudiant, puis passées en niveaux de gris :
- le fond est aplani (division par une estimation de l'éclairage) ;
- l'encre bleue (points d'interrogation, « 1/2 », « δ(t - nTs) », formule ajoutée à la
  question 12) et le surligneur rose sont effacés ;
- la photo n'est pas plane : chaque page est redressée par un cisaillement vertical dont
  la pente varie avec la hauteur (PENTES, mesurées sur les lignes de texte).
Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/ts227-communications-numeriques/annales/sujets/2015-2016-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/ts227/annales/2015-2016-partiel.pdf')
NOM = '2015-2016-partiel'
MARGE = 15
DPI = 200
LARGEUR_MAX = 1400

# Pente du texte (dy/dx, positive si la ligne descend vers la droite) en fonction de y.
PENTES = {
    1: [(0, 0.008), (2339, 0.008)],
    2: [(350, -0.024), (450, -0.025), (550, -0.015), (750, -0.012), (950, -0.010),
        (1050, -0.008), (1450, -0.008), (1600, -0.004)],
    3: [(350, 0.028), (450, 0.025), (550, 0.022), (650, 0.010), (750, 0.010), (850, -0.001)],
}
X_CENTRE = 815

# Annotations à blanchir en plus de l'encre colorée : page -> [(x0, y0, x1, y1)]
# (coordonnées après redressement).
BLANCHIR = {
    1: [],
    2: [(1165, 735, 1220, 795),     # « 1/2 » à côté de la question 9
        (660, 860, 900, 896),       # restes de « δ(t - nTs) » sous la question 10
        (1005, 1203, 1340, 1295),   # formule ajoutée à droite de la question 12
        (680, 1200, 1015, 1225),    # trait au-dessus de la somme (question 12)
        (290, 1135, 359, 1215)],    # « ?( » dans la marge de la question 12
    3: [],
}

# (fichier, [(page, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi après redressement.
BOITES = [
    ('notations', [(1, (355, 775, 1280, 970))]),
    ('ex1',       [(1, (355, 995, 1280, 1040))]),
    ('ex1-q1',    [(1, (362, 1048, 1280, 1110))]),
    ('ex1-q2',    [(1, (362, 1118, 1280, 1180))]),
    ('ex1-q3',    [(1, (362, 1188, 1280, 1250)), (1, (380, 1563, 1280, 1588))]),  # + note 1
    ('ex1-q4',    [(1, (362, 1258, 1280, 1345))]),
    ('ex1-q5',    [(1, (362, 1352, 1280, 1435)), (1, (380, 1588, 1280, 1612))]),  # + note 2
    ('ex1-q6',    [(1, (362, 1448, 1280, 1555))]),
    ('ex1-q7',    [(2, (315, 355, 1290, 420))]),
    ('ex1-q8',    [(2, (320, 440, 1290, 500))]),
    ('ex2',       [(2, (320, 530, 1290, 735))]),
    ('ex2-q9',    [(2, (340, 750, 1290, 785))]),
    ('ex2-q10',   [(2, (350, 795, 1290, 880))]),
    ('ex2-q11',   [(2, (360, 900, 1290, 1080)), (2, (355, 1095, 1290, 1130))]),   # filtre g_alpha + q. 11
    ('ex2-q12',   [(2, (355, 1145, 1290, 1495))]),
    ('ex2-q13',   [(2, (355, 1505, 1290, 1540))]),
    ('ex2-q14',   [(2, (355, 1555, 1290, 1595))]),
    ('ex2-q15',   [(2, (355, 1605, 1290, 1665)), (3, (350, 400, 1290, 490))]),    # définition de la bande + q. 15
    ('ex2-q16',   [(3, (355, 505, 1290, 780))]),
    ('ex2-q17',   [(3, (370, 790, 1290, 850))]),
    ('ex2-q18',   [(3, (370, 860, 1290, 945)), (3, (375, 960, 1290, 1075))]),     # modèle r_l[n] + q. 18
    ('ex2-q19',   [(3, (375, 1090, 1290, 1145))]),
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
