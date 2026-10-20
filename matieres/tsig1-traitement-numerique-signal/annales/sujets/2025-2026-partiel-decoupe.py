#!/usr/bin/env python3
"""Découpage du partiel TSIG1 2025-2026 (scan PDF, 2 pages) en images par question.

À lancer depuis la racine du projet Bristol :
    python3 matieres/tsig1-traitement-numerique-signal/annales/sujets/2025-2026-partiel-decoupe.py [dossier_sortie]
Dépendances : pdftoppm (poppler), Pillow, numpy.

Étapes : rendu à 200 dpi en niveaux de gris, contraste renforcé (le verso,
visible par transparence, devient blanc), découpe des boîtes, rognage des
marges blanches, PNG 8 bits.
"""
import subprocess
import sys
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image

PDF = Path("sources/tsig1/annales/2025-2026-partiel.pdf")
OUT = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parent
ANNALE = "2025-2026-partiel"
DPI = 200

# nom -> liste de zones (page, (x0, y0, x1, y1)) en pixels à 200 dpi ;
# plusieurs zones sont empilées verticalement (énoncé à cheval sur deux pages).
X0, X1 = 140, 1535
BOITES = {
    "ex1": [(1, (X0, 720, X1, 862))],
    "ex1-q1": [(1, (X0, 882, X1, 924))],
    "ex1-q2": [(1, (X0, 924, X1, 964))],
    "ex1-q3": [(1, (X0, 964, X1, 1020))],
    "ex2": [(1, (X0, 1045, X1, 1495))],
    "ex3": [(1, (X0, 1520, X1, 1715))],
    "ex3-q1": [(1, (X0, 1724, X1, 1767))],
    "ex3-q2": [(1, (X0, 1767, X1, 1806))],
    "ex3-q3": [(1, (X0, 1806, X1, 1845))],
    "ex3-q4": [(1, (X0, 1845, X1, 1884))],
    "ex3-q5": [(1, (X0, 1884, X1, 1918))],
    "ex3-q6": [(1, (X0, 1918, X1, 1960))],
    "ex3-q7": [(1, (X0, 1960, X1, 2000))],
    "ex4": [(1, (X0, 2048, X1, 2150)), (2, (X0, 120, X1, 215))],
    "ex4-q1": [(2, (X0, 250, X1, 290))],
    "ex4-q2": [(2, (X0, 290, X1, 455))],
    "ex5": [(2, (X0, 488, X1, 1366))],
    "ex6": [(2, (X0, 1376, X1, 1420))],
    "ex6-q1": [(2, (X0, 1438, X1, 1518))],
    "ex6-q2": [(2, (X0, 1518, X1, 1596))],
}


def pages():
    with tempfile.TemporaryDirectory() as d:
        subprocess.run(["pdftoppm", "-r", str(DPI), "-gray", "-png", str(PDF), f"{d}/p"], check=True)
        res = {}
        for f in sorted(Path(d).glob("p-*.png")):
            a = np.array(Image.open(f).convert("L"), dtype=np.float32)
            # Contraste : niveaux [70, 200] -> [0, 255].
            a = np.clip((a - 70.0) / (200.0 - 70.0) * 255.0, 0, 255)
            res[int(f.stem.split("-")[1])] = a.astype(np.uint8)
        return res


def rogne(a, seuil=200, pad=15, horizontal=True):
    enc = a < seuil
    rows = np.where(enc.sum(1) >= 2)[0]
    cols = np.where(enc.sum(0) >= 2)[0]
    if len(rows) == 0:
        return a
    y0, y1 = max(rows[0] - pad, 0), min(rows[-1] + pad + 1, a.shape[0])
    if not horizontal:
        return a[y0:y1]
    x0, x1 = max(cols[0] - pad, 0), min(cols[-1] + pad + 1, a.shape[1])
    return a[y0:y1, x0:x1]


def sauve(a, nom):
    im = Image.fromarray(a)
    if im.width > 1400:
        im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
    im = im.quantize(colors=16, dither=Image.Dither.NONE)
    im.save(OUT / f"{nom}.png", optimize=True)


def main():
    pg = pages()
    for nom, zones in BOITES.items():
        # rognage vertical de chaque zone, puis rognage global : les zones
        # empilées gardent leur alignement horizontal (formule centrée).
        morceaux = [rogne(pg[p][y0:y1, x0:x1], horizontal=False) for p, (x0, y0, x1, y1) in zones]
        sauve(rogne(np.vstack(morceaux)), f"{ANNALE}-{nom}")


if __name__ == "__main__":
    main()
