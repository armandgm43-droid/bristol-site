#!/usr/bin/env python3
"""Découpe du partiel EANA3 du 24/10/2025 en images (une par question) : partie de
Y. Deval (référence de tension bipolaire stable en température, pages 1-2) et partie de
F. Rivet (« Une référence des circuits intégrés », bandgap de Brokaw vu en contre-réaction,
pages 3-4).

Source : sources/eana3/annales/2025-2026-partiel.pdf (scan, 4 pages). Pages rendues à
200 dpi avec pdftoppm (1642 x 2324 px), en niveaux de gris ; le point blanc est abaissé pour
effacer le texte du verso visible par transparence. Annotations manuscrites d'un étudiant
effacées (EFFACER) : « vbe2 » et « vbe1 » au crayon sur la figure 1 de Y. Deval (seuls les
gris du crayon sont blanchis, les traits imprimés noirs sont gardés), cercles autour des
numéros des questions 9 et 10 (page 2) ; la ligne « ifb = βF vo » en haut de la page 4 est
laissée hors des cadres. Une image peut être formée de plusieurs morceaux empilés
verticalement. Les largeurs sont uniformisées à la fin (marge blanche à droite).

Usage (depuis la racine du projet Bristol) :
    python3 matieres/eana3-circuits-integres/annales/sujets/2025-2026-partiel-decoupe.py [racine] [dossier_sortie]
Dépendances : poppler-utils (pdftoppm), Pillow, numpy.
"""
import os, subprocess, sys, tempfile
import numpy as np
from PIL import Image

RACINE = sys.argv[1] if len(sys.argv) > 1 else '.'
SORTIE = sys.argv[2] if len(sys.argv) > 2 else os.path.dirname(os.path.abspath(__file__))
PDF = os.path.join(RACINE, 'sources/eana3/annales/2025-2026-partiel.pdf')
NOM = '2025-2026-partiel'
MARGE = 15
DPI = 200
NOIR, BLANC = 40, 215

# (fichier, [(page du PDF, (x0, y0, x1, y1)), ...]) ; coordonnées à 200 dpi.
BOITES = [
    ('ex1',         [(1, (225, 488, 1425, 1606)), (1, (225, 1935, 1425, 2035))]),
    ('ex1-annexe',  [(2, (235, 985, 1435, 1612))]),
    ('ex1-q1',      [(1, (225, 1610, 1425, 1780))]),
    ('ex1-q2',      [(1, (225, 1781, 1425, 1878))]),
    ('ex1-q3',      [(1, (225, 1879, 1425, 1916))]),
    ('ex1-q4',      [(2, (240, 225, 1435, 368))]),
    ('ex1-q5',      [(2, (240, 367, 1435, 428))]),
    ('ex1-q6',      [(2, (240, 428, 1435, 503))]),
    ('ex1-q7',      [(2, (240, 503, 1435, 541))]),
    ('ex1-q8',      [(2, (240, 548, 1435, 657))]),
    ('ex1-q9',      [(2, (215, 655, 1435, 745))]),
    ('ex1-q10',     [(2, (215, 748, 1435, 875))]),
    ('ex2',         [(3, (230, 503, 1430, 2025))]),
    ('ex2-rappels', [(4, (225, 1475, 1265, 1870))]),
    ('ex2-q1',      [(4, (225, 235, 1420, 322))]),
    ('ex2-q2',      [(4, (225, 325, 1420, 518))]),
    ('ex2-q3',      [(4, (225, 522, 1420, 564))]),
    ('ex2-q4',      [(4, (225, 566, 1420, 663))]),
    ('ex2-q5',      [(4, (225, 667, 1420, 763))]),
    ('ex2-q6',      [(4, (225, 767, 1420, 863))]),
    ('ex2-q7',      [(4, (225, 912, 1420, 1098))]),
    ('ex2-q8',      [(4, (225, 1150, 1420, 1336))]),
    ('ex2-q9',      [(4, (225, 1337, 1420, 1385))]),
    ('ex2-q10',     [(4, (225, 1386, 1420, 1433))]),
]

# Effacement des annotations manuscrites, par page :
# (x0, y0, x1, y1, seuil, zone gardée) : dans le rectangle, les pixels plus clairs que
# seuil (après normalisation, 0-255) passent au blanc ; seuil 0 = tout le rectangle,
# sauf la zone gardée (numéro imprimé entouré).
EFFACER = {
    1: [(625, 1060, 757, 1150, 70, None),                        # « vbe2 » au crayon
        (771, 1060, 875, 1150, 70, None)],                       # « vbe1 » (fil d'émetteur de Q1 gardé)
    2: [(212, 650, 296, 715, 0, (247, 667, 282, 702)),           # cercle autour de « 9. »
        (212, 815, 296, 877, 0, (247, 829, 294, 858))],          # cercle autour de « 10. »
}


def page(num, tmp):
    base = os.path.join(tmp, f'p{num}')
    subprocess.run(['pdftoppm', '-r', str(DPI), '-f', str(num), '-l', str(num),
                    '-singlefile', '-gray', '-png', PDF, base], check=True)
    g = np.asarray(Image.open(base + '.png').convert('L'), float)
    g = np.clip((g - NOIR) / (BLANC - NOIR), 0, 1) * 255
    for x0, y0, x1, y1, seuil, garde in EFFACER.get(num, []):
        zone = g[y0:y1, x0:x1].copy()
        masque = zone >= seuil
        if garde is not None:
            gx0, gy0, gx1, gy1 = garde
            masque[gy0 - y0:gy1 - y0, gx0 - x0:gx1 - x0] = False
        zone[masque] = 255
        g[y0:y1, x0:x1] = zone
    return Image.fromarray(g.astype(np.uint8))


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
