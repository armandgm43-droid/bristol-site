#!/usr/bin/env python3
"""Figure : chronogrammes du compteur 4 bits de l'examen NUMC1 2025-2026 (partie I).
(a) question 1 : compteur d'origine, reset synchrone actif jusqu'à 15 ns ; C3 passe
à 1 au front de 90 ns. (b) question 2.3 : compteur à bascules scan, chaîne dont la
bascule de C3 est la première (entrée de scan SI sur son entrée DT) ; C3 passe à 1
au front de 20 ns. Temps de propagation nuls (hypothèse du sujet). TC = 0 : mode
test, d'après la figure 2 du sujet.

Usage : python3 ann-2025-chronogrammes-compteur.py [dossier_sortie]
Aucune dépendance (SVG écrit à la main). Produit ann-2025-chronogramme-compteur.svg
et ann-2025-chronogramme-scan.svg.
"""
import os, sys
DOSSIER = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
NOIR, GRIS = '#1a1a1a', '#7E889B'

def chronogramme(signaux, t_max, pas_grille, px_par_ns, titre_axe='t (ns)', notes=()):
    """signaux : liste de (nom, [(t, v), ...]) avec v in {0, 1, 'x'} (x : indéterminé),
    ou (nom, ('bus', [(t, texte), ...])). Retourne le texte SVG."""
    G, HS, ES = 95, 26, 18          # marge gauche, hauteur signal, écart
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

def horloge(t_max, periode=10):
    return [(k * periode / 2, 1 - (k % 2)) for k in range(int(2 * t_max / periode))]

# (a) compteur d'origine
T = 100
valeurs = [(0, '0')] + [(10 * n + 10, str(n)) for n in range(1, 9)]
valeurs[0] = (0, '0')
reset = [(0, 1), (15, 0)]
c = {b: [(0, 0)] for b in range(4)}
for n in range(1, 9):
    t = 10 * n + 10
    for b in range(4):
        c[b].append((t, (n >> b) & 1))
sig = [('CLK', horloge(T)), ('reset', reset), ('compteur', ('bus', valeurs))] + \
      [(f'C{b}', c[b]) for b in (0, 1, 2, 3)]
open(os.path.join(DOSSIER, 'ann-2025-chronogramme-compteur.svg'), 'w', encoding='utf-8').write(
    chronogramme(sig, T, 10, 8, notes=[(90, 6, 'C3 = 1 : faute détectable')]))

# (b) compteur à bascules scan
T = 40
sig = [('CLK', horloge(T)), ('reset', [(0, 1), (15, 0)]), ('TC', [(0, 0)]),
       ('SI', [(0, 1)]), ('C3', [(0, 0), (20, 1)])]
open(os.path.join(DOSSIER, 'ann-2025-chronogramme-scan.svg'), 'w', encoding='utf-8').write(
    chronogramme(sig, T, 5, 16, notes=[(20, 4, 'C3 = 1 : faute détectable')]))
print('ok')
