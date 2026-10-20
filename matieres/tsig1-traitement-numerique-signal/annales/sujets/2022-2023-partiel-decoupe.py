#!/usr/bin/env python3
"""Découpage du partiel TSIG1 2022-2023 (trois photos) en images par question.

À lancer depuis la racine du projet Bristol :
    python3 matieres/tsig1-traitement-numerique-signal/annales/sujets/2022-2023-partiel-decoupe.py [dossier_sortie]
Dépendances : Pillow, numpy, opencv-python (pip install opencv-python-headless).

Étapes : orientation EXIF (photos prises tournées de 90°), correction de
perspective (homographie à partir de 4 points relevés sur chaque photo),
correction d'éclairage (division par le fond flouté), contraste renforcé,
découpe des boîtes (coordonnées dans l'image redressée), rognage des marges
blanches, largeur <= 1400 px, PNG 8 bits.
"""
import sys
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageOps

SRC = Path("sources/tsig1/annales")
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
ANNALE = "2022-2023-partiel"
ECHELLE = 0.5  # réduction appliquée à toutes les images
MARGE = 150  # marge (px) autour du quadrilatère redressé

# Quadrilatère source (HG, HD, BD, BG) dans la photo orientée (3024 x 4032),
# taille du rectangle d'arrivée (L, H) et du canevas (largeur, hauteur).
PAGES = {
    1: dict(quad=[[597, 250], [2629, 242], [2695, 3315], [105, 3315]],
            rect=(2500, 3400), canvas=(2800, 4400)),
    2: dict(quad=[[435, 323], [1782, 220], [1855, 3604], [10, 3548]],
            rect=(1850, 2650), canvas=(3200, 3300),
            # Courbure du papier : en haut de la page (exercice 3), la moitié
            # droite des lignes remonte d'environ 38 px ; on la redescend.
            courbure=dict(x0=1500, x1=2400, dy=38, y_plein=1470, y_nul=1550)),
    3: dict(quad=[[270, 202], [2722, 202], [2722, 2400], [136, 2400]],
            rect=(2586, 2260), canvas=(2900, 2900)),
}

# Boîtes dans la page redressée : nom -> (page, [zone, ...]). Une zone est
# (x0, y0, x1, y1) ou un dict {"b": (x0, y0, x1, y1), "rot": degrés (sens
# trigonométrique, autour du centre de la zone, pour les lignes encore
# inclinées par la courbure du papier), "masque": [(x0, y0, x1, y1), ...]
# (rectangles blanchis : annotations manuscrites d'une autre question)}.
# Plusieurs zones sont empilées verticalement.
BOITES = {
    "ex1": (1, [(100, 1320, 2750, 2298)]),
    "ex1-q1": (1, [(180, 2305, 1100, 2401)]),
    "ex1-q2": (1, [(180, 2401, 1100, 2495)]),
    "ex2": (1, [(100, 2560, 2750, 3040)]),
    "ex2-q1": (1, [(180, 3040, 1300, 3185)]),
    "ex2-q2": (1, [(180, 3195, 1300, 3340)]),
    "ex2-q3": (1, [(180, 3350, 1300, 3480)]),
    "ex2-q4": (1, [(180, 3490, 1300, 3620)]),
    "ex3": (2, [{"b": (100, 60, 3150, 935), "masque": [(250, 897, 1300, 935), (2200, 925, 3150, 935)]}]),
    "ex3-q1": (2, [{"b": (250, 900, 3100, 1090), "masque": [(1300, 900, 2200, 930), (800, 988, 3100, 1090)]}]),
    "ex3-q2": (2, [{"b": (250, 988, 3100, 1195), "masque": [(0, 988, 1000, 1092), (1000, 988, 2300, 1060)]}]),
    "ex3-q3": (2, [(250, 1195, 3100, 1328)]),
    "ex3-q4": (2, [{"b": (250, 1328, 1700, 1404), "masque": [(0, 1388, 1220, 1404)]}]),
    "ex3-q5": (2, [{"b": (250, 1388, 2700, 1475), "masque": [(1220, 1388, 2700, 1404)]}]),
    "ex4": (2, [(100, 1480, 2950, 2840)]),
    # Page 3 : lignes ondulées et serrées. Zone « ligne » : on ne garde que les
    # pixels à moins de « demi » px de la ligne médiane (interpolée entre les
    # points (x, y) relevés).
    "ex4-q1": (3, [{"b": (100, 100, 1000, 200), "ligne": [(275, 160), (525, 150), (775, 153)], "demi": 32, "x_queue": 240}]),
    "ex4-q2": (3, [{"b": (100, 170, 1000, 265), "ligne": [(275, 220), (525, 220), (775, 221)], "demi": 32, "x_queue": 240, "masque": [(100, 170, 240, 203)]}]),
    "ex4-q3": (3, [{"b": (100, 240, 1300, 345), "ligne": [(275, 282), (525, 286), (775, 298), (1025, 308)], "demi": 32, "x_queue": 240, "masque": [(100, 240, 240, 264)]}]),
    "ex4-q4": (3, [{"b": (100, 310, 1300, 410), "ligne": [(275, 358), (525, 360), (775, 360), (1025, 372)], "demi": 32, "x_queue": 240, "masque": [(100, 310, 240, 329)]}]),
    "ex4-q5": (3, [{"b": (100, 375, 1300, 475), "ligne": [(275, 421), (525, 421), (775, 436), (1025, 438)], "demi": 32, "x_queue": 240, "masque": [(100, 375, 240, 394)]}]),
    "ex4-q6": (3, [{"b": (100, 440, 2000, 560), "ligne": [(275, 495), (525, 493), (775, 498), (1025, 510), (1275, 517), (1525, 512), (1775, 517)], "demi": 33, "x_queue": 240, "masque": [(100, 440, 240, 462)]}]),
    "ex5": (3, [(100, 590, 2800, 1050)]),
    "ex6": (3, [{"b": (100, 1090, 1985, 1245), "masque": [(1500, 1237, 1985, 1245)]}]),
}


def redresse(num):
    p = PAGES[num]
    im = ImageOps.exif_transpose(Image.open(SRC / f"{ANNALE}-p{num}.jpg")).convert("L")
    a = np.array(im)
    w, h = p["rect"]
    dst = np.float32([[MARGE, MARGE], [MARGE + w, MARGE], [MARGE + w, MARGE + h], [MARGE, MARGE + h]])
    M = cv2.getPerspectiveTransform(np.float32(p["quad"]), dst)
    a = cv2.warpPerspective(a, M, p["canvas"], flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    if "courbure" in p:
        c = p["courbure"]
        hh, ww = a.shape
        xs = np.arange(ww, dtype=np.float32)
        ys = np.arange(hh, dtype=np.float32)
        fx = np.clip((xs - c["x0"]) / (c["x1"] - c["x0"]), 0, 1) * c["dy"]
        fy = np.clip((c["y_nul"] - ys) / (c["y_nul"] - c["y_plein"]), 0, 1)
        map_x = np.tile(xs, (hh, 1))
        map_y = ys[:, None] - fy[:, None] * fx[None, :]
        a = cv2.remap(a, map_x, map_y.astype(np.float32), cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)
    # Éclairage : fond estimé par dilatation (efface le texte) puis flou, à deux
    # échelles. Fond fin (noyau 41 px) partout, sauf dans les aplats sombres des
    # schémas (blocs grisés) où l'on garde le fond large (≈ 600 px) pour qu'ils
    # restent visibles.
    def fond_estime(k, f):
        petit = cv2.resize(a, None, fx=f, fy=f, interpolation=cv2.INTER_AREA)
        petit = cv2.dilate(petit, np.ones((k, k), np.uint8))
        petit = cv2.GaussianBlur(petit, (0, 0), k / 4)
        return cv2.resize(petit, (a.shape[1], a.shape[0]), interpolation=cv2.INTER_LINEAR).astype(np.float32)
    fin = fond_estime(21, 0.5)
    large = fond_estime(151, 0.25)
    aplat = cv2.dilate((fin < 0.65 * large).astype(np.uint8), np.ones((81, 81), np.uint8))
    fond = np.where(aplat > 0, large, fin)
    n = np.clip(a.astype(np.float32) / np.maximum(fond, 1) * 255.0, 0, 255)
    # Contraste : niveaux [60, 195] -> [0, 255] ; fond (et transparence du
    # verso) blanc.
    n = np.clip((n - 60.0) / (195.0 - 60.0) * 255.0, 0, 255)
    return n.astype(np.uint8)


def zone(page, z):
    if not isinstance(z, dict):
        z = {"b": z}
    x0, y0, x1, y1 = z["b"]
    a = page.copy()
    for (u0, v0, u1, v1) in z.get("masque", []):
        a[v0:v1, u0:u1] = 255
    if "ligne" in z:
        px, py = zip(*z["ligne"])
        xs = np.arange(a.shape[1])
        yc = np.interp(xs, px, py)
        ys = np.arange(a.shape[0])[:, None]
        # sous la ligne, tolérance plus grande à gauche (queue du « Q » initial)
        bas = np.where(xs < z.get("x_queue", 0), z["demi"] + 18, z["demi"])
        d = ys - yc[None, :]
        a[(d < -z["demi"]) | (d > bas[None, :])] = 255
    if z.get("rot"):
        M = cv2.getRotationMatrix2D(((x0 + x1) / 2, (y0 + y1) / 2), z["rot"], 1.0)
        a = cv2.warpAffine(a, M, (a.shape[1], a.shape[0]), flags=cv2.INTER_CUBIC, borderValue=255)
    return a[y0:y1, x0:x1]


def rogne(a, seuil=200, pad=15):
    enc = a < seuil
    # ignore les points isolés (poussières) : au moins 3 pixels encre par ligne/colonne
    rows = np.where(enc.sum(1) >= 3)[0]
    cols = np.where(enc.sum(0) >= 3)[0]
    if len(rows) == 0:
        return a
    y0, y1 = max(rows[0] - pad, 0), min(rows[-1] + pad + 1, a.shape[0])
    x0, x1 = max(cols[0] - pad, 0), min(cols[-1] + pad + 1, a.shape[1])
    return a[y0:y1, x0:x1]


def sauve(a, nom):
    # Même échelle pour toutes les images (texte de même taille d'une question
    # à l'autre), largeur plafonnée à 1400 px.
    im = Image.fromarray(a)
    e = min(ECHELLE, 1400 / im.width)
    im = im.resize((round(im.width * e), round(im.height * e)), Image.LANCZOS)
    im = im.quantize(colors=16, dither=Image.Dither.NONE)
    im.save(OUT / f"{nom}.png", optimize=True)


def main():
    pages = {n: redresse(n) for n in PAGES}
    if "--pages" in sys.argv:
        for n, a in pages.items():
            Image.fromarray(a).save(OUT / f"_page{n}.png")
        return
    for nom, (num, boites) in BOITES.items():
        morceaux = [rogne(zone(pages[num], z)) for z in boites]
        largeur = max(m.shape[1] for m in morceaux)
        pile = np.vstack([np.pad(m, ((0, 0), (0, largeur - m.shape[1])), constant_values=255) for m in morceaux])
        sauve(pile, f"{ANNALE}-{nom}")


if __name__ == "__main__":
    main()
