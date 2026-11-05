#!/usr/bin/env python3
"""Découpe des énoncés des TD d'EAEP1 en images (une par question).

Source : sources/eaep1/td/td-sepic-2024-vinassa.pdf (1 p., PDF vectoriel).
Page rendue à 200 dpi avec pdftoppm, en niveaux de gris ; coordonnées
(y0, y1) en pixels à 200 dpi, relevées avec `pdftotext -bbox-layout`.
Les paragraphes de transition de l'énoncé sont rattachés à la question
qui les suit (q3, q10). Largeurs uniformisées (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eaep1-conversion-energie/td/sujets/decoupe-td.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
DPI = 200
MARGE = 15
X0, X1 = 150, 1560

TD = {
    'td01': ('td-sepic-2024-vinassa.pdf', {
        'td01-enonce': [(1, 150, 715)],
        'td01-q1':     [(1, 720, 768)],
        'td01-q2':     [(1, 768, 890)],
        'td01-q3':     [(1, 890, 1060)],
        'td01-q4':     [(1, 1060, 1143)],
        'td01-q5':     [(1, 1143, 1265)],
        'td01-q6':     [(1, 1265, 1313)],
        'td01-q7':     [(1, 1313, 1433)],
        'td01-q8':     [(1, 1433, 1520)],
        'td01-q9':     [(1, 1520, 1607)],
        'td01-q10':    [(1, 1607, 1740)],
        'td01-q11':    [(1, 1740, 1780)],
        'td01-q12':    [(1, 1780, 1875)],
        'td01-q13':    [(1, 1875, 1960)],
        'td01-q14':    [(1, 1960, 2075)],
        'td01-q15':    [(1, 2075, 2190)],
    }),
}


def page(pdf, num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', pdf, base], check=True)
    return Image.open(base + '.png').convert('L')


def rogner(im, seuil=200, min_px=1):
    a = np.asarray(im) < seuil
    lignes = np.where(a.sum(axis=1) >= min_px)[0]
    cols = np.where(a.sum(axis=0) >= min_px)[0]
    if len(lignes) == 0:
        return im
    return im.crop((cols[0], lignes[0], cols[-1] + 1, lignes[-1] + 1))


def empiler(morceaux, ecart=12):
    w = max(m.width for m in morceaux)
    h = sum(m.height for m in morceaux) + ecart * (len(morceaux) - 1)
    out = Image.new('L', (w, h), 255)
    y = 0
    for m in morceaux:
        out.paste(m, (0, y))
        y += m.height + ecart
    return out


def main():
    os.makedirs(SORTIE, exist_ok=True)
    for td, (fichier, boites) in TD.items():
        pdf = os.path.join(RACINE, 'sources/eaep1/td', fichier)
        ims = {}
        with tempfile.TemporaryDirectory() as tmp:
            pages = {}
            for nom, morceaux in boites.items():
                parts = []
                for p, y0, y1 in morceaux:
                    if p not in pages:
                        pages[p] = page(pdf, p, tmp)
                    parts.append(rogner(pages[p].crop((X0, y0, X1, y1))))
                im = empiler(parts)
                out = Image.new('L', (im.width + 2 * MARGE, im.height + 2 * MARGE), 255)
                out.paste(im, (MARGE, MARGE))
                ims[nom] = out
        wmax = max(i.width for i in ims.values())
        for nom, im in ims.items():
            fond = Image.new('L', (wmax, im.height), 255)
            fond.paste(im, (0, 0))
            chemin = os.path.join(SORTIE, f'{nom}.png')
            fond.quantize(colors=16, dither=Image.Dither.NONE).save(chemin, optimize=True)
            print(chemin, fond.size)


if __name__ == '__main__':
    main()
