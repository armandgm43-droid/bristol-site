#!/usr/bin/env python3
"""Découpe du partiel EA210 « Circuits HF et oscillateurs » du 7/01/2014 en images
(une par question) : partie I (charges actives, reprise à l'exercice II de 2016-2017),
partie II (oscillateur en anneau), partie III (inverseur à retard paramétrable).

Source : sources/eana3/annales/2013-2014-partiel-circuits-hf-oscillateurs.pdf (scan
couleur, 3 pages). Pages rendues à 200 dpi avec pdftoppm (environ 1620 x 2165 px), en
niveaux de gris ; le point blanc est abaissé pour effacer le texte du verso visible par
transparence. Une image peut être formée de plusieurs morceaux empilés verticalement
(question 10 : énoncé puis figure 5). Les annotations manuscrites d'un étudiant (flèches
tracées sur les figures 4 et 5) sont effacées par des rectangles blancs (EFFACER), placés
à côté des traits imprimés. Les largeurs sont uniformisées à la fin (marge
blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2013-2014-partiel-circuits-hf-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana3/annales/2013-2014-partiel-circuits-hf-oscillateurs.pdf')
NOM = '2013-2014-partiel-circuits-hf'
MARGE = 15
DPI = 200
NOIR, BLANC = 40, 200          # niveaux ramenés au noir et au blanc

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('ex1',          [(1, (150, 725, 1480, 1520))]),
    ('ex1-q1',       [(1, (150, 1550, 1480, 1632))]),
    ('ex1-q2',       [(1, (150, 1655, 1480, 1772))]),
    ('ex1-q3',       [(1, (150, 1795, 1480, 1985))]),
    ('ex1-q3-bonus', [(1, (150, 2005, 1480, 2085))]),
    ('ex2',          [(2, (165, 160, 1480, 745))]),
    ('ex2-q4',       [(2, (165, 800, 1480, 1540))]),
    ('ex2-q5',       [(2, (165, 1628, 1480, 1668))]),
    ('ex2-q6',       [(2, (165, 1680, 1480, 1752))]),
    ('ex2-q6-1',     [(2, (165, 1765, 1480, 1808))]),
    ('ex2-q6-2',     [(2, (165, 1815, 1480, 1862))]),
    ('ex2-q6-3',     [(2, (165, 1866, 1480, 1912))]),
    ('ex2-q7',       [(2, (165, 1918, 1480, 1965))]),
    ('ex3',          [(3, (165, 150, 870, 770))]),
    ('ex3-q8',       [(3, (880, 265, 1460, 425))]),
    ('ex3-q9',       [(3, (880, 515, 1460, 715))]),
    ('ex3-rappel',   [(3, (155, 790, 1500, 1190))]),
    ('ex3-q10',      [(3, (180, 1205, 1480, 1290)), (3, (180, 1480, 710, 1970))]),
    ('ex3-q11',      [(3, (180, 1315, 1480, 1355))]),
    ('ex3-q12',      [(3, (180, 1382, 1480, 1460))]),
    ('ex3-q13',      [(3, (745, 1482, 1465, 1640))]),
    ('ex3-q14',      [(3, (745, 1665, 1465, 1790))]),
    ('ex3-q15',      [(3, (745, 1812, 1465, 2005))]),
]

# Rectangles remis en blanc (annotations manuscrites), par page ; coordonnées à 200 dpi.
EFFACER = {
    3: [(256, 383, 268, 400), (268, 383, 310, 427),     # flèche vers l'émetteur de Q101
        (397, 385, 426, 428), (426, 385, 452, 404),     # flèche vers l'émetteur de Q102
        (343, 1665, 354, 1690), (358, 1665, 373, 1690)],  # pointe de flèche sur le collecteur de Q1
}


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    g = np.clip((g - NOIR) / (BLANC - NOIR), 0, 1)
    for x0, y0, x1, y1 in EFFACER.get(num, []):
        g[y0:y1, x0:x1] = 1
    return Image.fromarray((g * 255).astype(np.uint8))


def rogner(im, seuil=160, min_px=2):
    """Rogne au contenu puis ajoute une marge blanche."""
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    serre = im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))
    out = Image.new('L', (serre.width + 2 * MARGE, serre.height + 2 * MARGE), 255)
    out.paste(serre, (MARGE, MARGE))
    return out


def empiler(morceaux):
    """Empile verticalement des morceaux rognés, alignés à gauche."""
    if len(morceaux) == 1:
        return morceaux[0]
    out = Image.new('L', (max(m.width for m in morceaux), sum(m.height for m in morceaux)), 255)
    y = 0
    for m in morceaux:
        out.paste(m, (0, y))
        y += m.height
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    ims = {}
    with tempfile.TemporaryDirectory() as tmp:
        pages = {p: page(p, tmp) for p in sorted({p for _, ms in BOITES for p, _ in ms})}
        for nom, morceaux in BOITES:
            ims[nom] = empiler([rogner(pages[p].crop(b)) for p, b in morceaux])
    wmax = min(1400, max(i.width for i in ims.values()))
    for nom, im in ims.items():
        if im.width > 1400:
            im = im.resize((1400, round(im.height * 1400 / im.width)), Image.LANCZOS)
        fond = Image.new('L', (wmax, im.height), 255)
        fond.paste(im, (0, 0))
        chemin = os.path.join(SORTIE, f'{NOM}-{nom}.png')
        fond.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)
        print(chemin, fond.size, os.path.getsize(chemin), 'octets')


if __name__ == '__main__':
    main()
