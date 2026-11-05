#!/usr/bin/env python3
"""Figure : chronogrammes de la porte NAND Dynamic-BiMOS (partiel NUMC1 2019-2020,
partie 2, question 1). Temps de propagation idéalisés ; les impulsions de X1 et X2
au début des phases d'évaluation où A = B = 1 ont une largeur exagérée (1,5 ns)
pour être visibles. Horloge supposée de rapport cyclique 1/2.

Usage : python3 ann-2019-chronogrammes-bimos.py [sortie.svg]
Aucune dépendance (SVG écrit à la main).
"""
import os, sys
SORTIE = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'ann-2019-chronogrammes-bimos.svg')
NOIR, GRIS = '#1a1a1a', '#7E889B'

def chronogramme(signaux, t_max, pas_grille, px_par_ns, titre_axe='t (ns)', notes=()):
    """signaux : liste de (nom, [(t, v), ...]) avec v in {0, 1, 'x'} (x : indéterminé),
    ou (nom, ('bus', [(t, texte), ...])). Retourne le texte SVG."""
    G, HS, ES = 70, 26, 18          # marge gauche, hauteur signal, écart
    W = G + t_max * px_par_ns + 30
    H = 20 + len(signaux) * (HS + ES) + 40
    el = []
    X = lambda t: G + t * px_par_ns
    for k in range(0, t_max + 1, pas_grille):
        el.append(f'<line x1="{X(k)}" y1="12" x2="{X(k)}" y2="{H-34}" stroke="#d4d4d8" stroke-width="0.8"/>')
        el.append(f'<text x="{X(k)}" y="{H-18}" font-size="12" text-anchor="middle" fill="{NOIR}">{k}</text>')
    el.append(f'<text x="{X(t_max)+4}" y="{H-4}" font-size="12" text-anchor="end" fill="{NOIR}">{titre_axe}</text>')
    for i, (nom, trans) in enumerate(signaux):
        y0 = 20 + i * (HS + ES)
        yh, yb = y0, y0 + HS
        el.append(f'<text x="{G-10}" y="{y0+HS/2+5}" font-size="14" text-anchor="end" fill="{NOIR}">{nom}</text>')
        if isinstance(trans, tuple) and trans[0] == 'bus':
            pts = trans[1] + [(t_max, None)]
            for (t1, txt), (t2, _) in zip(pts[:-1], pts[1:]):
                d = 3
                el.append(f'<path d="M{X(t1)},{(yh+yb)/2} L{X(t1)+d},{yh} L{X(t2)-d},{yh} L{X(t2)},{(yh+yb)/2} '
                          f'L{X(t2)-d},{yb} L{X(t1)+d},{yb} Z" fill="none" stroke="{NOIR}" stroke-width="1.4"/>')
                el.append(f'<text x="{(X(t1)+X(t2))/2}" y="{(yh+yb)/2+4}" font-size="11" text-anchor="middle" fill="{NOIR}">{txt}</text>')
            continue
        pts = trans + [(t_max, None)]
        chemin = []
        prec = None
        for (t1, v), (t2, _) in zip(pts[:-1], pts[1:]):
            if v == 'x':
                el.append(f'<rect x="{X(t1)}" y="{yh}" width="{X(t2)-X(t1)}" height="{HS}" fill="#e4e4e7" stroke="{NOIR}" stroke-width="1"/>')
                prec = None
                continue
            y = yh if v == 1 else yb
            if prec is not None and prec != y:
                chemin.append(f'L{X(t1)},{y}')
            elif prec is None:
                chemin.append(f'M{X(t1)},{y}')
            chemin.append(f'L{X(t2)},{y}')
            prec = y
        el.append(f'<path d="{" ".join(chemin)}" fill="none" stroke="{NOIR}" stroke-width="1.6"/>')
    for (t, i, txt) in notes:
        y0 = 20 + i * (HS + ES)
        el.append(f'<text x="{X(t)}" y="{y0-3}" font-size="10" text-anchor="middle" fill="{GRIS}">{txt}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
            f'font-family="sans-serif"><rect width="100%" height="100%" fill="white"/>' + ''.join(el) + '</svg>')

d = 1.5   # largeur (exagérée) des impulsions
H  = [(0, 0), (5, 1), (10, 0), (15, 1), (20, 0), (25, 1), (30, 0), (35, 1)]
A  = [(0, 0), (13, 1)]
B  = [(0, 0), (23, 1)]
X1 = [(0, 1), (5, 0), (10, 1), (15, 0), (20, 1), (25, 0), (25 + d, 1), (35, 0), (35 + d, 1)]
X2 = [(0, 0), (25, 1), (25 + d, 0), (35, 1), (35 + d, 0)]
Y  = [(0, 1), (25 + d / 2, 0), (30, 1), (35 + d / 2, 0)]
svg = chronogramme([('H', H), ('A', A), ('B', B), ('X1', X1), ('X2', X2), ('Y', Y)],
                   40, 5, 16,
                   notes=[(2.5, 0, 'préch.'), (7.5, 0, 'éval.'), (12.5, 0, 'préch.'), (17.5, 0, 'éval.'),
                          (22.5, 0, 'préch.'), (27.5, 0, 'éval.'), (32.5, 0, 'préch.'), (37.5, 0, 'éval.')])
open(SORTIE, 'w', encoding='utf-8').write(svg)
print(SORTIE)
