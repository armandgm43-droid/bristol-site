#!/usr/bin/env python3
"""Découpe des énoncés des TD d'EARF1 en images (une par question).

Sources : sources/earf1/td/td01-gnuradio-modulations.pdf (10 p.),
td02-modulateurs.pdf (3 p.), td03-demodulateurs.pdf (3 p.) : PDF vectoriels.
Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris ; coordonnées
(y0, y1) en pixels à 200 dpi, relevées avec `pdftotext -bbox-layout`.
Une image peut assembler plusieurs morceaux (empilés verticalement).
Les largeurs sont uniformisées par TD (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/earf1-modulations-communications/td/sujets/decoupe-td.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
DPI = 200
MARGE = 15
X0, X1 = 150, 1560   # bande horizontale du texte (rognée ensuite au contenu)

TD = {
    'td01': ('td01-gnuradio-modulations.pdf', {
        'td01-rappels':  [(2, 1480, 1945)],
        'td01-ex1':      [(3, 190, 700)],
        'td01-ex1-q1':   [(4, 288, 382)],
        'td01-ex1-q2':   [(4, 514, 562)],
        'td01-ex1-q3':   [(4, 758, 1452)],
        'td01-ex1-q4':   [(4, 1523, 1817)],
        'td01-ex2':      [(6, 286, 336)],
        'td01-ex2-q1':   [(6, 366, 413)],
        'td01-ex2-q2':   [(6, 596, 706)],
        'td01-ex2-q3':   [(6, 839, 1131)],
        'td01-ex2-q4':   [(6, 1235, 1346), (6, 1571, 1619), (6, 1814, 1861)],
        'td01-ex3':      [(7, 190, 632), (8, 351, 546)],
        'td01-ex3-q1':   [(8, 576, 686)],
        'td01-ex3-q2':   [(8, 832, 986)],
        'td01-ex3-q3':   [(8, 1187, 1540)],
        'td01-ex3-q4':   [(8, 1612, 1704)],
        'td01-ex3-q5':   [(8, 1900, 2102)],
        'td01-ex3-q6':   [(10, 192, 744)],
        'td01-ex4':      [(10, 870, 1066)],
        'td01-ex4-q1':   [(10, 1095, 1249)],
        'td01-ex4-q2':   [(10, 1412, 1728)],
        'td01-ex4-q3':   [(10, 1751, 1862)],
    }),
    'td02': ('td02-modulateurs.pdf', {
        'td02-ex1':      [(1, 555, 1680)],
        'td02-ex1-q1':   [(1, 1737, 1889)],
        'td02-ex1-q2':   [(1, 1887, 1978)],
        'td02-ex1-q3':   [(2, 192, 538)],
        'td02-ex1-q4':   [(2, 554, 804)],
        'td02-ex1-q5':   [(2, 816, 908)],
        'td02-ex1-app':  [(2, 948, 1144)],
        'td02-ex1-q6':   [(2, 1154, 1261)],
        'td02-ex1-q7':   [(2, 1276, 1368)],
        'td02-ex1-q8':   [(2, 1381, 1518)],
        'td02-ex2':      [(2, 1659, 1884), (3, 190, 597)],
        'td02-ex2-q1':   [(3, 630, 722)],
        'td02-ex2-q2':   [(3, 736, 784)],
        'td02-ex2-q3':   [(3, 796, 932)],
        'td02-ex3':      [(3, 1074, 1210)],
        'td02-ex3-q1':   [(3, 1223, 1315)],
        'td02-ex3-q2':   [(3, 1328, 1376)],
        'td02-ex3-q3':   [(3, 1388, 1524)],
        'td02-ex3-q4':   [(3, 1537, 1585)],
        'td02-ex3-q5':   [(3, 1598, 1646)],
    }),
    'td03': ('td03-demodulateurs.pdf', {
        'td03-ex1':      [(1, 555, 1439)],
        'td03-ex1-q1':   [(1, 1452, 1544)],
        'td03-ex1-q2':   [(1, 1557, 1605)],
        'td03-ex1-q3':   [(1, 1618, 1710)],
        'td03-ex1-q4':   [(1, 1722, 1814)],
        'td03-ex1-ook':  [(1, 1855, 1991), (2, 185, 578)],
        'td03-ex1-q5':   [(2, 584, 676)],
        'td03-ex1-q6':   [(2, 690, 782)],
        'td03-ex1-q7':   [(2, 794, 842)],
        'td03-ex2':      [(2, 940, 1490)],
        'td03-ex2-q1':   [(2, 1524, 1572)],
        'td03-ex2-q2':   [(2, 1585, 1700)],
        'td03-ex2-q3':   [(2, 1707, 1800), (3, 185, 526)],
        'td03-ex2-q4':   [(2, 1812, 1904)],
        'td03-ex2-q5':   [(3, 532, 580)],
        'td03-ex2-q6':   [(3, 576, 624)],
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
        pdf = os.path.join(RACINE, 'sources/earf1/td', fichier)
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
