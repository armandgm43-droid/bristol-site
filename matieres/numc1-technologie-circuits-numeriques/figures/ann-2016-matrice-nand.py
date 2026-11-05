#!/usr/bin/env python3
"""Figure : matrice mémoire flash NAND du partiel NUMC1 2016-2017 (partie 1).

Une colonne (bit line) par bit de donnée B3…B0 : charge de rappel vers VDD en haut,
chaîne de 8 transistors à grille flottante en série jusqu'à la masse. Un transistor
est dessiné quand la cellule n'est PAS programmée (bit lu = 1) ; une cellule
programmée (toujours passante) est remplacée par un fil. Les grilles de la ligne i
reçoivent /Wi (sortie du décodeur inversée).

Usage : python3 ann-2016-matrice-nand.py [sortie.svg]
Aucune dépendance (SVG écrit à la main).
"""
import os, sys

SORTIE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'ann-2016-matrice-nand.svg')

# Contenu de la mémoire (figure 1 du sujet) : adresse -> (B3, B2, B1, B0)
TABLE = {0: (1, 0, 1, 1), 1: (1, 1, 1, 1), 2: (0, 1, 1, 1), 3: (0, 1, 1, 0),
         4: (1, 0, 1, 0), 5: (1, 1, 1, 0), 6: (1, 0, 0, 1), 7: (1, 1, 0, 1)}
NOIR, GRIS = '#1a1a1a', '#7E889B'
X_COL = [230 + 130 * j for j in range(4)]      # B3, B2, B1, B0
Y_HAUT, PAS = 150, 52
Y_LIGNES = [Y_HAUT + 40 + PAS * i for i in range(8)]
Y_GND = Y_LIGNES[-1] + 50

el = []
def ligne(x1, y1, x2, y2, c=NOIR, w=1.6, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    el.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"{d}/>')
def texte(x, y, s, taille=15, anc='middle', c=NOIR, style=''):
    el.append(f'<text x="{x}" y="{y}" font-size="{taille}" text-anchor="{anc}" fill="{c}" {style}>{s}</text>')

def nmos(x, y):
    """NMOS vertical centré en (x, y), grille à gauche ; retourne x de la grille."""
    ligne(x, y - 26, x, y - 12); ligne(x, y + 12, x, y + 26)
    ligne(x, y - 12, x - 10, y - 12); ligne(x, y + 12, x - 10, y + 12)
    ligne(x - 10, y - 15, x - 10, y + 15, w=2.2)      # canal
    ligne(x - 15, y - 13, x - 15, y + 13, w=1.4)      # grille flottante
    ligne(x - 20, y - 13, x - 20, y + 13, w=2.2)      # grille de commande
    el.append(f'<path d="M{x-6},{y+8} L{x-1},{y+12} L{x-6},{y+16}" fill="none" stroke="{NOIR}" stroke-width="1.4"/>')
    return x - 20

# Lignes de mot (/Wi), horizontales
for i, y in enumerate(Y_LIGNES):
    texte(95, y - 15, f'W{i}', anc='end')
    ligne(74, y - 31, 86, y - 31, w=1.2)                 # barre de complément sur W
    ligne(100, y - 20, X_COL[-1] - 20, y - 20, c=NOIR, w=1.0)
# Colonnes
for j, x in enumerate(X_COL):
    b = 3 - j
    # charge de rappel (résistance) vers VDD et sortie
    ligne(x, 60, x, 75)
    el.append(f'<rect x="{x-7}" y="75" width="14" height="34" fill="white" stroke="{NOIR}" stroke-width="1.6"/>')
    ligne(x, 109, x, Y_LIGNES[0] - 26)
    el.append(f'<circle cx="{x}" cy="128" r="3" fill="{NOIR}"/>')
    ligne(x, 128, x + 40, 128)
    texte(x + 44, 133, f'B{b}', anc='start')
    for i, y in enumerate(Y_LIGNES):
        if TABLE[i][j]:
            xg = nmos(x, y)
            ligne(xg, y - 20, xg, y - 13)
            el.append(f'<circle cx="{xg}" cy="{y - 20}" r="2.6" fill="{NOIR}"/>')
        else:
            ligne(x, y - 26, x, y + 26)                 # cellule programmée : fil
        if i < 7:
            ligne(x, y + 26, x, y + PAS - 26)
    ligne(x, Y_LIGNES[-1] + 26, x, Y_GND)
    ligne(x - 12, Y_GND, x + 12, Y_GND, w=2); ligne(x - 7, Y_GND + 5, x + 7, Y_GND + 5, w=2)
# rail VDD
ligne(X_COL[0] - 30, 60, X_COL[-1] + 30, 60, w=2)
texte(X_COL[0] - 36, 65, 'VDD', anc='end')
H = Y_GND + 30
svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{X_COL[-1] + 110}" height="{H}" '
       f'viewBox="0 0 {X_COL[-1] + 110} {H}" font-family="sans-serif">',
       f'<rect width="100%" height="100%" fill="white"/>'] + el + ['</svg>']
open(SORTIE, 'w', encoding='utf-8').write('\n'.join(svg))
print(SORTIE)
