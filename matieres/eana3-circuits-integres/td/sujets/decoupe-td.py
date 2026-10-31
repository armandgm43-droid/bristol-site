#!/usr/bin/env python3
"""Découpe des énoncés des TD d'EANA3 en images (une par question).

Sources : sources/eana3/td/*.pdf (PDF vectoriels, texte extractible).
Pages rendues à 200 dpi avec pdftoppm, en niveaux de gris ; coordonnées
en pixels à 200 dpi, relevées avec `pdftotext -bbox-layout`.
Un morceau est (page, y0, y1) sur la bande horizontale par défaut
(X0, X1), ou (page, y0, y1, x0, x1) pour une page en colonnes.
Une image peut assembler plusieurs morceaux (empilés verticalement).
Les largeurs sont uniformisées par TD (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/td/sujets/decoupe-td.py [racine] [dossier_sortie] [td…]
Sans liste de TD, tous les TD sont découpés.
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
CHOIX = sys.argv[3:]
DPI = 200
MARGE = 15
X0, X1 = 150, 1560   # bande horizontale du texte (rognée ensuite au contenu)

TD = {
    'td01': ('td01-ou-est-la-contre-reaction.pdf', {
        'td01-ex1':      [(1, 640, 1580)],
        'td01-ex1-q1':   [(1, 1585, 1847)],
        'td01-ex1-q2':   [(1, 1852, 1897)],
        'td01-ex1-q3':   [(1, 1903, 1948)],
        'td01-ex1-q4':   [(1, 1953, 2003)],
        'td01-ex1-q5':   [(2, 190, 345)],
        'td01-ex1-q6':   [(2, 368, 523)],
        'td01-ex1-q7':   [(2, 537, 630)],
        'td01-ex1-q8':   [(2, 640, 893)],
    }),
    'td02': ('td02-circuit-pour-l-espace.pdf', {
        'td02-ex1':      [(1, 690, 2010), (2, 190, 990)],
        'td02-ex1-fig2': [(2, 1040, 1680)],
        'td02-ex1-p1':   [(2, 1765, 1970), (3, 190, 815, 150, 845)],
        'td02-ex1-q1':   [(3, 190, 296, 845, 1560)],
        'td02-ex1-q2':   [(3, 300, 610, 845, 1560)],
        'td02-ex1-q3':   [(3, 614, 836, 845, 1560), (3, 838, 890)],
        'td02-ex1-q4':   [(3, 892, 1040)],
        'td02-ex1-q5':   [(3, 1097, 1558)],
        'td02-ex1-q6':   [(3, 1565, 1608)],
        'td02-ex1-q7':   [(3, 1612, 1680)],
        'td02-ex1-q8':   [(3, 1683, 1733)],
        'td02-ex1-p3':   [(4, 200, 1566)],
        'td02-ex1-q9':   [(4, 1570, 1622)],
        'td02-ex1-q10':  [(4, 1625, 1775)],
    }),
    'td03': ('td03-modulation-amplitude.pdf', {
        'td03-ex1':         [(1, 590, 1850)],
        'td03-ex1-rappels': [(3, 815, 1492)],
        'td03-ex1-p1':      [(1, 1895, 2120)],
        'td03-ex1-q1':      [(2, 200, 350)],
        'td03-ex1-q2':      [(2, 355, 610)],
        'td03-ex1-q3':      [(2, 612, 658)],
        'td03-ex1-q4':      [(2, 662, 870)],
        'td03-ex1-bornes':  [(2, 875, 1086)],
        'td03-ex1-q5':      [(2, 1090, 1190)],
        'td03-ex1-q6':      [(2, 1192, 1352)],
        'td03-ex1-q7':      [(2, 1354, 1460)],
        'td03-ex1-p2':      [(2, 1478, 2140)],
        'td03-ex1-q8':      [(3, 190, 362)],
        'td03-ex1-q9':      [(3, 364, 513)],
        'td03-ex1-q10':     [(3, 515, 762)],
    }),
    'td-add-vdd': ('td-add-vdd-is-not-your-bff.pdf', {
        'td-add-vdd-ex1':      [(1, 600, 2145)],
        'td-add-vdd-ex1-q1':   [(2, 190, 406)],
        'td-add-vdd-ex1-q2':   [(2, 412, 515)],
        'td-add-vdd-ex1-q3':   [(2, 535, 900)],
        'td-add-vdd-ex1-q4':   [(2, 955, 999)],
        'td-add-vdd-ex1-q5':   [(2, 1005, 1110)],
        'td-add-vdd-ex1-suite': [(2, 1114, 1161)],
        'td-add-vdd-ex1-q6':   [(2, 1165, 1310)],
        'td-add-vdd-ex1-q7':   [(2, 1316, 1465)],
        'td-add-vdd-ex1-p3':   [(2, 1485, 1645)],
        'td-add-vdd-ex1-fig2': [(2, 1650, 1995, 892, 1560)],
        'td-add-vdd-ex1-q8':   [(2, 1648, 1792, 150, 890)],
        'td-add-vdd-ex1-q9':   [(2, 1798, 1996, 150, 890)],
        'td-add-vdd-ex1-q10':  [(2, 2000, 2045)],
    }),
    'td03-2026': ('td03-2026-bandgap-brokaw.pdf', {
        'td03-2026-ex1':       [(1, 590, 2115)],
        'td03-2026-ex1-npn':   [(2, 1490, 1960)],
        'td03-2026-ex1-q1':    [(2, 190, 296)],
        'td03-2026-ex1-q2':    [(2, 299, 498)],
        'td03-2026-ex1-q3':    [(2, 505, 553)],
        'td03-2026-ex1-q4':    [(2, 556, 661)],
        'td03-2026-ex1-q5':    [(2, 664, 770)],
        'td03-2026-ex1-q6':    [(2, 773, 870)],
        'td03-2026-ex1-gain':  [(2, 925, 1025)],
        'td03-2026-ex1-q7':    [(2, 1030, 1130)],
        'td03-2026-ex1-bruit': [(2, 1183, 1278)],
        'td03-2026-ex1-q8':    [(2, 1285, 1382)],
        'td03-2026-ex1-q9':    [(2, 1386, 1433)],
        'td03-2026-ex1-q10':   [(2, 1437, 1484)],
    }),
    'td04': ('td04-oscillateur-resistance-negative.pdf', {
        'td04-ex1':      [(1, 655, 1995)],
        'td04-ex1-p1':   [(2, 190, 785)],
        'td04-ex1-q1':   [(2, 832, 1016)],
        'td04-ex1-q2':   [(2, 1016, 1100)],
        'td04-ex1-q3':   [(2, 1108, 1311)],
        'td04-ex1-q4':   [(2, 1311, 1355)],
        'td04-ex1-q5':   [(2, 1362, 1607)],
        'td04-ex1-q6':   [(2, 1607, 1648)],
        'td04-ex1-q7':   [(2, 1648, 1732)],
    }),
    'td06': ('td06-oscillateur-aop.pdf', {
        'td06-ex1':      [(1, 612, 1405)],
        'td06-ex1-pa':   [(1, 1405, 2090)],
        'td06-ex1-q1':   [(2, 190, 280)],
        'td06-ex1-q2':   [(2, 280, 360)],
        'td06-ex1-q3':   [(2, 360, 440)],
        'td06-ex1-q4':   [(2, 440, 489)],
        'td06-ex1-q5':   [(2, 492, 662)],
        'td06-ex1-q6':   [(2, 662, 712)],
    }),
    'td-add-anneau': ('td-add-oscillateur-anneau.pdf', {
        'td-add-anneau-ex1':         [(1, 705, 1452)],
        'td-add-anneau-ex1-q1':      [(1, 1476, 1521)],
        'td-add-anneau-ex1-q2':      [(1, 1521, 1563)],
        'td-add-anneau-ex1-q3':      [(1, 1563, 1652)],
        'td-add-anneau-ex2':         [(2, 190, 1045)],
        'td-add-anneau-ex2-q1':      [(2, 1100, 1190)],
        'td-add-anneau-ex2-q2':      [(2, 1190, 1290)],
        'td-add-anneau-ex2-rappels': [(2, 1310, 1875)],
        'td-add-anneau-ex2-cml':     [(2, 1935, 2030), (3, 185, 932)],
        'td-add-anneau-ex2-q3':      [(3, 985, 1080)],
        'td-add-anneau-ex2-q4':      [(3, 1080, 1165)],
        'td-add-anneau-ex2-q5':      [(3, 1165, 1253)],
        'td-add-anneau-ex2-q6':      [(3, 1253, 1337)],
        'td-add-anneau-ex2-q7':      [(3, 1337, 1512)],
    }),
    # Recueil de sujets de Y. Deval (PDF Word) : ex1 = 2021, ex2 = 2022, ex3 = 2025, ex4 = 2026.
    'td04-2026': ('td04-2026-recueil-sujets-deval.pdf', {
        'td04-2026-ex1':          [(1, 555, 1436)],
        'td04-2026-ex1-fig2':     [(1, 1470, 2016)],
        'td04-2026-ex1-q1':       [(1, 2026, 2066)],
        'td04-2026-ex1-q2':       [(1, 2078, 2117)],
        'td04-2026-ex1-q3':       [(2, 196, 234)],
        'td04-2026-ex1-q4':       [(2, 245, 806)],
        'td04-2026-ex1-q5':       [(2, 820, 927)],
        'td04-2026-ex1-q6':       [(2, 955, 995)],
        'td04-2026-ex1-q7':       [(2, 1025, 1108)],
        'td04-2026-ex1-q8':       [(2, 1142, 1280)],
        'td04-2026-ex1-annexe':   [(2, 1345, 1946)],
        'td04-2026-ex2':          [(3, 555, 1498)],
        'td04-2026-ex2-fig2':     [(3, 1534, 2092)],
        'td04-2026-ex2-q1':       [(3, 2100, 2140)],
        'td04-2026-ex2-q2':       [(4, 198, 234)],
        'td04-2026-ex2-q3':       [(4, 248, 386)],
        'td04-2026-ex2-q4':       [(4, 398, 970)],
        'td04-2026-ex2-q5':       [(4, 985, 1078)],
        'td04-2026-ex2-q6':       [(4, 1108, 1146)],
        'td04-2026-ex2-q7':       [(4, 1176, 1258)],
        'td04-2026-ex2-q8':       [(4, 1294, 1430)],
        'td04-2026-ex2-annexe':   [(4, 1495, 2101)],
        'td04-2026-ex3':          [(5, 630, 1682), (5, 2038, 2146)],
        'td04-2026-ex3-q1':       [(5, 1690, 1870)],
        'td04-2026-ex3-q2':       [(5, 1869, 1968)],
        'td04-2026-ex3-q3':       [(5, 1971, 2010)],
        'td04-2026-ex3-q4':       [(6, 192, 339)],
        'td04-2026-ex3-q5':       [(6, 340, 406)],
        'td04-2026-ex3-q6':       [(6, 406, 490)],
        'td04-2026-ex3-q7':       [(6, 491, 528)],
        'td04-2026-ex3-q8':       [(6, 537, 654)],
        'td04-2026-ex3-q9':       [(6, 655, 746)],
        'td04-2026-ex3-q10':      [(6, 756, 872)],
        'td04-2026-ex3-annexe':   [(6, 1022, 1678)],
        'td04-2026-ex4':          [(7, 486, 2129)],
        'td04-2026-ex4-i-q1':     [(8, 200, 298)],
        'td04-2026-ex4-i-q2':     [(8, 316, 394)],
        'td04-2026-ex4-i-q3':     [(8, 412, 490)],
        'td04-2026-ex4-i-q4':     [(8, 510, 587)],
        'td04-2026-ex4-i-q5':     [(8, 606, 743)],
        'td04-2026-ex4-i-q6':     [(8, 763, 800)],
        'td04-2026-ex4-i-q7':     [(8, 818, 895)],
        'td04-2026-ex4-i-q8':     [(8, 915, 985)],
        'td04-2026-ex4-i-q9':     [(8, 1010, 1126)],
        'td04-2026-ex4-i-q10':    [(8, 1144, 1221)],
        'td04-2026-ex4-ii':       [(8, 1255, 2144)],
        'td04-2026-ex4-ii-ampli': [(9, 200, 721)],
        'td04-2026-ex4-ii-q1':    [(9, 738, 872)],
        'td04-2026-ex4-ii-q2':    [(9, 889, 967)],
        'td04-2026-ex4-ii-q3':    [(9, 986, 1025)],
        'td04-2026-ex4-ii-q4':    [(9, 1042, 1180)],
        'td04-2026-ex4-ii-q5':    [(9, 1196, 1273)],
        'td04-2026-ex4-ii-retour': [(9, 1290, 1820)],
        'td04-2026-ex4-ii-q6':    [(9, 1836, 1875)],
        'td04-2026-ex4-ii-q7':    [(9, 1892, 2010)],
        'td04-2026-ex4-ii-q8':    [(9, 2026, 2105)],
        'td04-2026-ex4-ii-q9':    [(10, 200, 457)],
        'td04-2026-ex4-ii-q10':   [(10, 476, 630)],
        'td04-2026-ex4-annexe':   [(10, 738, 1008)],
    }),
    'td05': ('td05-reference-tension-cmos.pdf', {
        'td05-ex1':      [(1, 615, 2110), (2, 198, 300)],
        'td05-ex1-q1':   [(2, 315, 385)],
        'td05-ex1-q2':   [(2, 398, 501)],
        'td05-ex1-q3':   [(2, 518, 551)],
        'td05-ex1-q4':   [(2, 566, 768)],
        'td05-ex1-q5':   [(2, 782, 817)],
        'td05-ex1-q6':   [(2, 832, 868)],
        'td05-ex1-q7':   [(2, 883, 952)],
        'td05-ex1-miroir': [(2, 966, 1070)],
        'td05-ex1-q8':   [(2, 1085, 1120)],
        'td05-ex1-temperature': [(2, 1135, 1405)],
        'td05-ex1-q9':   [(2, 1420, 1470)],
        'td05-ex1-q10':  [(2, 1482, 1520)],
    }),
    # FIN-TD
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
        if CHOIX and td not in CHOIX:
            continue
        pdf = os.path.join(RACINE, 'sources/eana3/td', fichier)
        ims = {}
        with tempfile.TemporaryDirectory() as tmp:
            pages = {}
            for nom, morceaux in boites.items():
                parts = []
                for m in morceaux:
                    p, y0, y1 = m[:3]
                    x0, x1 = m[3:] if len(m) == 5 else (X0, X1)
                    if p not in pages:
                        pages[p] = page(pdf, p, tmp)
                    parts.append(rogner(pages[p].crop((x0, y0, x1, y1))))
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
