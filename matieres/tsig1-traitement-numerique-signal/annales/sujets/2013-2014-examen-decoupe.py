"""Découpe du sujet de l'examen du 14/03/2014 (TS201, 2e session) en une image par question.

Source : sources/tsig1/td/recueil-td-2023.pdf, « SUJET 2013 », pages 12-13 du PDF (vectoriel).
Usage : python 2013-2014-examen-decoupe.py [racine du projet Bristol]   (défaut : répertoire courant)
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
    "2013-2014-examen-ex1": [(12, 360, 440)],
    "2013-2014-examen-ex2": [(12, 462, 592)],
    "2013-2014-examen-ex2-qa": [(12, 602, 618.9)],
    "2013-2014-examen-ex2-qb": [(12, 618.9, 632.65)],
    "2013-2014-examen-ex2-qc": [(12, 632.65, 646.5)],
    "2013-2014-examen-ex2-qd": [(12, 646.5, 660.25)],
    "2013-2014-examen-ex2-qe": [(12, 660.25, 676)],
    "2013-2014-examen-ex3": [(12, 700, 717), (13, 68, 162)],
    "2013-2014-examen-ex4": [(13, 198, 214.2)],
    "2013-2014-examen-ex4-q1": [(13, 214.2, 242.8)],
    "2013-2014-examen-ex4-q2": [(13, 242.8, 279)],
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
