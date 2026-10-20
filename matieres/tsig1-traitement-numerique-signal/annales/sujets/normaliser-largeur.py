"""Uniformise la largeur des images d'une même annale (marge blanche ajoutée à droite),
pour que le texte de toutes les questions s'affiche à la même échelle sur le site.
À lancer depuis ce dossier après les scripts <annale>-decoupe.py : python3 normaliser-largeur.py"""
import glob, os, re
from collections import defaultdict
from PIL import Image

groupes = defaultdict(list)
for f in glob.glob("*.png"):
    m = re.match(r"(\d{4}-\d{4}-(?:partiel|examen))-", os.path.basename(f))
    if m:
        groupes[m.group(1)].append(f)
for annale, fichiers in groupes.items():
    wmax = max(Image.open(f).width for f in fichiers)
    for f in fichiers:
        im = Image.open(f)
        if im.width < wmax:
            fond = 255 if im.mode in ("L", "P") else (255, 255, 255)
            im2 = Image.new(im.mode if im.mode != "P" else "L", (wmax, im.height), fond)
            im2.paste(im.convert(im2.mode), (0, 0))
            im2.save(f, optimize=True)
    print(annale, len(fichiers), "images, largeur", wmax)
