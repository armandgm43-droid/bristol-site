"""TSIG2, partiel 2014-2015, ex. 2 q. 1 — Schéma de réalisation causale (forme directe I)
du filtre T1 : y(n) = y(n-1)/5 + y(n-2)/5 + x(n)/4 + 3x(n-1)/4 + x(n-2)/2.
Figure construite d'après l'équation (1) du sujet."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
fig, ax = plt.subplots(figsize=(7.5, 4))
ax.set_xlim(0, 10); ax.set_ylim(-0.4, 4.6); ax.axis("off")
fl = dict(arrowstyle="-|>", color="k", lw=1, shrinkA=0, shrinkB=0)
def fleche(x0, y0, x1, y1): ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=fl)
def boite(x, y, txt, w=0.8, h=0.5):
    ax.add_patch(FancyBboxPatch((x - w/2, y - h/2), w, h, boxstyle="round,pad=0.02", fc="white", ec="k"))
    ax.text(x, y, txt, ha="center", va="center")
def gain(x, y, txt):
    ax.add_patch(plt.Polygon([[x - 0.3, y + 0.25], [x - 0.3, y - 0.25], [x + 0.3, y]], fc="white", ec="k"))
    ax.text(x, y + 0.42, txt, ha="center", va="bottom", fontsize=9)
def somme(x, y):
    ax.add_patch(Circle((x, y), 0.22, fc="white", ec="k")); ax.text(x, y, "+", ha="center", va="center")
Y = [4, 2.4, 0.8]          # niveaux : n, n-1, n-2
xe, xs = 1.0, 9.0          # colonne des retards entrée / sortie
# Branche d'entrée
ax.text(0.1, Y[0], "$x(n)$", ha="left", va="center")
ax.plot([0.6, xe], [Y[0], Y[0]], "k", lw=1)
for i in range(2):
    ax.plot([xe, xe], [Y[i], (Y[i] + Y[i+1]) / 2 + 0.3], "k", lw=1)
    boite(xe, (Y[i] + Y[i+1]) / 2 + 0.05, "$z^{-1}$")
    ax.plot([xe, xe], [(Y[i] + Y[i+1]) / 2 - 0.2, Y[i+1]], "k", lw=1)
for yy, g in zip(Y, ["1/4", "3/4", "1/2"]):
    ax.plot([xe, 2.0], [yy, yy], "k", lw=1); gain(2.3, yy, g); fleche(2.6, yy, 4.28, yy)
# Additionneurs (chaîne verticale)
for yy in Y: somme(4.5, yy)
fleche(4.5, Y[2] + 0.22, 4.5, Y[1] - 0.22); fleche(4.5, Y[1] + 0.22, 4.5, Y[0] - 0.22)
# Sortie
ax.plot([4.72, xs], [Y[0], Y[0]], "k", lw=1); fleche(xs, Y[0], 9.7, Y[0])
ax.text(9.75, Y[0], "$y(n)$", ha="left", va="center")
for i in range(2):
    ax.plot([xs, xs], [Y[i], (Y[i] + Y[i+1]) / 2 + 0.3], "k", lw=1)
    boite(xs, (Y[i] + Y[i+1]) / 2 + 0.05, "$z^{-1}$")
    ax.plot([xs, xs], [(Y[i] + Y[i+1]) / 2 - 0.2, Y[i+1]], "k", lw=1)
for yy in Y[1:]:
    ax.plot([xs, 7.2], [yy, yy], "k", lw=1); fleche(6.6, yy, 4.72, yy)
    ax.add_patch(plt.Polygon([[7.2, yy + 0.25], [7.2, yy - 0.25], [6.6, yy]], fc="white", ec="k"))
    ax.text(6.9, yy + 0.42, "1/5", ha="center", va="bottom", fontsize=9)
fig.tight_layout(); fig.savefig("ann-2014-schema-t1.svg")
