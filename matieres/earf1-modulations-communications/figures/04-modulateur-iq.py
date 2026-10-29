"""EARF1 ch. 4 — Modulateur IQ (modulateur vectoriel).
D'après le support [mod-num, p. 10], redessinée."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
B, R = "#2B4C9B", "#B23A3A"
fig, a = plt.subplots(figsize=(8.5, 3.2)); a.set_xlim(0, 10.5); a.set_ylim(0, 4); a.axis("off")
def boite(x, y, w, h, t, c="black"):
    a.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", fc="white", ec=c, lw=1.3))
    a.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=9)
def fl(p, q, c="black"): a.annotate("", q, p, arrowprops=dict(arrowstyle="->", lw=1.2, color=c))
boite(1.2, 1.9, 1.6, 0.9, "Calculateur\nnumérique")
boite(3.6, 3.0, 0.9, 0.5, "CNA"); boite(3.6, 1.2, 0.9, 0.5, "CNA")
fl((0.2, 2.35), (1.2, 2.35)); a.text(0.15, 2.55, "message $m(t)$", fontsize=8.5)
a.plot([2.8, 3.2, 3.2], [2.6, 2.6, 3.25], color=B); fl((3.2, 3.25), (3.6, 3.25), B)
a.plot([2.8, 3.2, 3.2], [2.1, 2.1, 1.45], color=R); fl((3.2, 1.45), (3.6, 1.45), R)
for y in (3.25, 1.45):
    a.add_patch(Circle((6.0, y), 0.28, fc="white", ec="black")); a.text(6.0, y, "×", ha="center", va="center", fontsize=12)
fl((4.5, 3.25), (5.72, 3.25), B); a.text(5.0, 3.4, "$I$", color=B)
fl((4.5, 1.45), (5.72, 1.45), R); a.text(5.0, 1.6, "$Q$", color=R)
boite(6.55, 0.35, 1.2, 0.55, "déphaseur\n$+\\pi/2$")
a.plot([0.2, 7.15], [0.15, 0.15], color="black"); a.text(0.15, 0.3, "porteuse $\\cos(2\\pi f_c t)$", fontsize=8.5)
a.plot([7.15, 7.15], [0.15, 0.35], color="black"); a.plot([7.15, 7.15], [0.9, 1.0], color="black")
a.plot([7.15, 6.0], [1.0, 1.0], color="black"); fl((6.0, 1.0), (6.0, 1.17))
a.plot([5.4, 5.4], [0.15, 2.4], color="black"); a.plot([5.4, 6.0], [2.4, 2.4], color="black"); fl((6.0, 2.4), (6.0, 2.97))
a.add_patch(Circle((8.6, 2.35), 0.32, fc="white", ec="black")); a.text(8.6, 2.35, "Σ", ha="center", va="center", fontsize=12)
a.plot([6.28, 8.6], [3.25, 3.25], color="black"); fl((8.6, 3.25), (8.6, 2.67))
a.plot([6.28, 8.6], [1.45, 1.45], color="black"); fl((8.6, 1.45), (8.6, 2.03))
fl((8.92, 2.35), (10.2, 2.35)); a.text(9.1, 2.55, "$s(t)$")
a.text(0.2, 3.75, "bleu, rouge : signaux numériques, basses fréquences ; noir : signaux analogiques, hautes fréquences", fontsize=7.5, color="#555")
fig.tight_layout(); fig.savefig("04-modulateur-iq.svg")
