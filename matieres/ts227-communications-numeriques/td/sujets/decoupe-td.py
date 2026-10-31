#!/usr/bin/env python3
"""Découpe de l'énoncé du TD de TS227 en images (une par question).

Source : sources/ts227/support/TD_TS_227.pdf (« Transmissions en bande de base »,
2020/2021, 4 p.) : PDF vectoriel. Un seul TD, publié sous td/td01-transmissions-bande-de-base.qmd.
Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris ; coordonnées
(y0, y1) en pixels à 200 dpi, relevées avec `pdftotext -bbox-layout`.
Une image peut assembler plusieurs morceaux (empilés verticalement).
Les largeurs sont uniformisées par TD (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/ts227-communications-numeriques/td/sujets/decoupe-td.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
DPI = 200
MARGE = 15
X0, X1 = 180, 1500   # bande horizontale du texte (rognée ensuite au contenu)

TD = {
    'td01': ('TD_TS_227.pdf', {
        'td01-architecture': [(1, 718, 1458)],
        'td01-ex1':      [(1, 1502, 1642)],
        'td01-ex1-q1':   [(1, 1646, 1721)],
        'td01-ex1-q2':   [(1, 1724, 1827)],
        'td01-ex1-q3':   [(1, 1831, 1904)],
        'td01-ex1-q4':   [(2, 282, 353)],
        'td01-ex1-q5':   [(2, 356, 426)],
        'td01-ex1-q6':   [(2, 427, 499)],
        'td01-ex2':      [(2, 543, 970)],
        'td01-ex2-q1':   [(2, 980, 1053)],
        'td01-ex2-q2':   [(2, 1053, 1093)],
        'td01-ex2-q3':   [(2, 1093, 1131)],
        'td01-ex2-q4':   [(2, 1132, 1177)],
        'td01-ex2-q5':   [(2, 1177, 1219)],
        'td01-ex2-q6':   [(2, 1220, 1256)],
        'td01-ex2-q7':   [(2, 1257, 1308)],
        'td01-ex2-q8':   [(2, 1309, 1348)],
        'td01-ex2-q9':   [(2, 1349, 1419)],
        'td01-ex2-q10':  [(2, 1420, 1652)],
        'td01-ex2-q11':  [(2, 1665, 1932)],
        'td01-ex3':      [(3, 275, 590)],
        'td01-ex3-q1':   [(3, 665, 736)],
        'td01-ex3-q2':   [(3, 741, 816)],
        'td01-ex3-q3':   [(3, 818, 857)],
        'td01-ex3-q4':   [(3, 862, 931)],
        'td01-ex4':      [(3, 978, 1284)],
        'td01-ex4-q1':   [(3, 1290, 1363)],
        'td01-ex4-q2':   [(3, 1364, 1446)],
        'td01-ex4-q3':   [(3, 1447, 1494)],
        'td01-ex4-q4':   [(3, 1495, 1568)],
        'td01-ex4-q5':   [(3, 1571, 1674)],
        'td01-ex4-q6':   [(3, 1680, 1716)],
        'td01-ex4-q7':   [(3, 1721, 1801)],
        'td01-ex5':      [(4, 282, 886)],
        'td01-ex5-q1':   [(4, 890, 930)],
        'td01-ex5-q2':   [(4, 935, 971)],
        'td01-ex5-q3':   [(4, 976, 1047)],
        'td01-ex5-q4':   [(4, 1052, 1091)],
        'td01-ex5-q5':   [(4, 1094, 1169)],
        'td01-ex5-q6':   [(4, 1170, 1243)],
        'td01-ex5-q7':   [(4, 1246, 1288)],
        'td01-ex5-q8':   [(4, 1289, 1329)],
        'td01-ex5-q9':   [(4, 1332, 1374)],
        'td01-ex5-q10':  [(4, 1375, 1416)],
        'td01-ex5-q11':  [(4, 1417, 1489)],
        'td01-ex5-q12':  [(4, 1490, 1598)],
        'td01-ex5-q13':  [(4, 1604, 1674)],
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
        pdf = os.path.join(RACINE, 'sources/ts227/support', fichier)
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
