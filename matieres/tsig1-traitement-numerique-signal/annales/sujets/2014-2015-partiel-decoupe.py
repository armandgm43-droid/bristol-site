"""Découpe du sujet du partiel du 28/11/2014 (TS201, 1re session) en une image par question.

Source : sources/tsig1/td/recueil-td-2023.pdf, « SUJET 2014 », pages 14-15 du PDF (vectoriel), dont le
contenu est identique au scan sources/tsig1/annales/2014-2015-partiel.pdf (comparaison faite le 2026-10-20) ;
la version vectorielle est plus nette et sans annotations manuscrites.
Usage : python 2014-2015-partiel-decoupe.py [racine du projet Bristol]   (défaut : répertoire courant)
Les images sont écrites à côté de ce script. Nécessite pdftoppm (poppler) et Pillow.
Boîtes en points PDF (x0, y0, x1, y1), origine en haut à gauche ; plusieurs boîtes = morceaux empilés.
"""
import os
import subprocess
import sys
import tempfile

from PIL import Image, ImageOps

PDF = "sources/tsig1/td/recueil-td-2023.pdf"
DPI = 200
X0, X1 = 66.4, 530.8  # colonne de texte (71,8 à 525,4 pt) + 15 px ; largeur commune = même échelle à l'écran
BOITES = {
    "2014-2015-partiel-ex1": [(14, 337, 419)],
    "2014-2015-partiel-ex1-q1": [(14, 421, 438.9)],
    "2014-2015-partiel-ex1-q2": [(14, 438.9, 460)],
    "2014-2015-partiel-ex1-q3": [(14, 460, 497)],
    "2014-2015-partiel-ex2": [(14, 507, 714)],
    "2014-2015-partiel-ex3": [(14, 724, 742), (15, 69, 193)],
    "2014-2015-partiel-ex3-q1": [(15, 200, 220)],
    "2014-2015-partiel-ex3-q2": [(15, 228, 248)],
    "2014-2015-partiel-ex3-q3": [(15, 256, 276)],
    "2014-2015-partiel-ex3-q4": [(15, 283.5, 303.5)],
    "2014-2015-partiel-ex3-q5": [(15, 311, 331)],
}
MARGE = 15  # px de blanc conservés autour du contenu
SEUIL = 200  # niveau de gris en dessous duquel un pixel est du contenu


def rendre(racine, page, dossier):
    base = os.path.join(dossier, f"p{page}")
    if not os.path.exists(base + ".png"):
        subprocess.run(["pdftoppm", "-r", str(DPI), "-gray", "-png", "-singlefile",
                        "-f", str(page), "-l", str(page), os.path.join(racine, PDF), base], check=True)
    return Image.open(base + ".png").convert("L")


def rogner(im):
    """Rogne le blanc en haut et en bas seulement (largeur fixe), puis remet MARGE px."""
    masque = im.point(lambda v: 255 if v < SEUIL else 0)
    _, y0, _, y1 = masque.getbbox()
    im = im.crop((0, y0, im.width, y1))
    return ImageOps.expand(im, border=(0, MARGE), fill=255)


def main():
    racine = sys.argv[1] if len(sys.argv) > 1 else "."
    sortie = os.path.dirname(os.path.abspath(__file__))
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
            if img.width > 1400:
                img = img.resize((1400, round(img.height * 1400 / img.width)), Image.LANCZOS)
            img.save(os.path.join(sortie, nom + ".png"), optimize=True)
            print(nom, img.size)


if __name__ == "__main__":
    main()
