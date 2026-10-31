#!/usr/bin/env python3
"""Découpe des énoncés des TD 1 à 3 de TSIG1 en images (une par question).

Source : sources/tsig1/td/recueil-td-2023.pdf (recueil de TD v2, 23 p., PDF
vectoriel) : TD 1 p. 3-6, TD 2 p. 7-8, TD 3 p. 9-10, annexe p. 11. Les sujets
d'examen du recueil (p. 12-23) sont découpés par les scripts de annales/sujets/.
Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris ; boîtes en points
PDF (page, y0, y1), origine en haut à gauche, relevées avec
`pdftotext -bbox-layout` ; plusieurs boîtes = morceaux empilés. Même colonne
(X0, X1) pour toutes les images, donc même échelle à l'écran (comme les
scripts des annales TSIG1).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/tsig1-traitement-numerique-signal/td/sujets/decoupe-td.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow.
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageOps

PDF = "sources/tsig1/td/recueil-td-2023.pdf"
DPI = 200
X0, X1 = 60, 550  # colonne de texte (72 à 525 pt) et cadres arrondis du TD 1 (63 à 547 pt)
MARGE = 15            # px de blanc conservés en haut et en bas
SEUIL = 200           # niveau de gris en dessous duquel un pixel est du contenu

BOITES = {
    # TD 1 — Systèmes discrets et représentation en fréquence
    "td01-ex1":    [(3, 212, 506.1)],
    "td01-ex1-q1": [(3, 506.1, 634)],
    "td01-ex2":    [(3, 640, 714), (4, 64, 89.6)],
    "td01-ex2-q1": [(4, 89.6, 112.6)],
    "td01-ex2-q2": [(4, 112.6, 132)],
    "td01-ex3":    [(4, 138, 198)],
    "td01-ex3-q1": [(4, 198, 326)],
    "td01-ex4":    [(4, 344, 425)],
    "td01-ex4-q1": [(4, 425, 473)],
    "td01-ex4-q2": [(4, 474, 716), (5, 66, 312)],
    "td01-ex4-q3": [(5, 312, 482)],
    "td01-ex5":    [(5, 487, 589)],
    "td01-ex5-q1": [(5, 589, 609)],
    "td01-ex6":    [(5, 609.5, 647)],
    "td01-ex6-qa": [(5, 647, 692.5)],
    "td01-ex6-qb": [(5, 692.5, 763), (6, 70, 89.5)],
    "td01-ex6-qc": [(6, 89.5, 171)],
    "td01-ex6-qd": [(6, 171, 229)],
    "td01-ex7":    [(6, 235, 292)],
    "td01-ex7-q1": [(6, 292, 312.5)],
    "td01-ex7-q2": [(6, 312.5, 350)],
    "td01-ex7-q3": [(6, 350, 433)],
    "td01-ex8":    [(6, 440, 587)],
    "td01-ex8-q1": [(6, 587, 621)],
    # TD 2 — Transformée en z et équation aux différences
    "td02-ex1":    [(7, 200, 221)],
    "td02-ex1-q1": [(7, 221, 281)],
    "td02-ex1-q2": [(7, 281, 328.5)],
    "td02-ex1-q3": [(7, 328.5, 348)],
    "td02-ex2":    [(7, 354, 420)],
    "td02-ex2-q1": [(7, 420, 481)],
    "td02-ex3":    [(7, 488, 551)],
    "td02-ex3-q1": [(7, 551, 572.4)],
    "td02-ex3-q2": [(7, 572.4, 592.2)],
    "td02-ex3-q3": [(7, 592.2, 612)],
    "td02-ex3-q4": [(7, 612, 631.8)],
    "td02-ex3-q5": [(7, 631.8, 651.6)],
    "td02-ex3-q6": [(7, 651.6, 671.3)],
    "td02-ex3-q7": [(7, 671.3, 704.5)],
    "td02-ex4":    [(7, 704.5, 744.5)],
    "td02-ex4-q1": [(7, 744.5, 764)],
    "td02-ex5":    [(8, 68, 108.7)],
    "td02-ex5-q1": [(8, 108.7, 128.5)],
    "td02-ex6":    [(8, 128.5, 168)],
    "td02-ex6-q1": [(8, 168, 188)],
    # TD 3 — Placement pôles/zéros et RII
    "td03-ex1":     [(9, 208, 312)],
    "td03-ex1-q1":  [(9, 312, 327.6)],
    "td03-ex1-q1a": [(9, 327.6, 341.3)],
    "td03-ex1-q1b": [(9, 341.3, 355.15)],
    "td03-ex1-q1c": [(9, 355.15, 372)],
    "td03-ex1-q2":  [(9, 380, 448)],
    "td03-ex1-q2a": [(9, 448, 465.3)],
    "td03-ex1-q2b": [(9, 465.3, 563)],
    "td03-ex1-q2c": [(9, 563, 600)],
    "td03-ex2":     [(9, 605, 628)],
    "td03-ex2-q1":  [(9, 628, 721)],
    "td03-ex2-q2":  [(10, 64, 142)],
    "td03-ex2-q3":  [(10, 142, 186)],
    "td03-ex2-q4":  [(10, 186, 274)],
    "td03-annexe":  [(11, 74, 545)],
}


def rendre(racine, page, dossier):
    base = os.path.join(dossier, f"p{page}")
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-r", str(DPI), "-gray", "-png", "-singlefile",
                        "-f", str(page), "-l", str(page), os.path.join(racine, PDF), base], check=True)
    return Image.open(base + ".png").convert("L")


def rogner(im):
    """Rogne le blanc en haut et en bas seulement (largeur fixe), puis remet MARGE px."""
    masque = im.point(lambda v: 255 if v < SEUIL else 0)
    boite = masque.getbbox()
    if boite is None:
        return im
    _, y0, _, y1 = boite
    im = im.crop((0, y0, im.width, y1))
    return ImageOps.expand(im, border=(0, MARGE), fill=255)


def main():
    racine = sys.argv[1] if len(sys.argv) > 1 else "."
    sortie = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
    k = DPI / 72
    with tempfile.TemporaryDirectory() as tmp:
        for nom, morceaux in BOITES.items():
            parts = []
            for page, y0, y1 in morceaux:
                im = rendre(racine, page, tmp)
                parts.append(rogner(im.crop((round(X0 * k), round(y0 * k), round(X1 * k), round(y1 * k)))))
            larg = max(p.width for p in parts)
            img = Image.new("L", (larg, sum(p.height for p in parts)), 255)
            y = 0
            for p in parts:
                img.paste(p, (0, y))
                y += p.height
            img = img.point(lambda v: 255 if v > 235 else v)  # fond bien blanc
            img.save(os.path.join(sortie, nom + ".png"), optimize=True)
            print(nom, img.size)


if __name__ == "__main__":
    main()
