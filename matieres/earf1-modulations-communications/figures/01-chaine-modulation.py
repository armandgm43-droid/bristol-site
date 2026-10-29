"""EARF1 ch. 1 — Chaîne de modulation et de démodulation.
D'après le support [mod-ana, p. 7], redessinée."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU = "#2B4C9B"
fig, a = plt.subplots(figsize=(9, 2.6)); a.set_xlim(0, 10); a.set_ylim(0, 3); a.axis("off")
def boite(x, y, w, h, t):
    a.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", fc="white", ec=BLEU, lw=1.5))
    a.text(x + w / 2, y + h / 2, t, ha="center", va="center", color=BLEU, fontsize=11)
def fleche(x1, x2, y):
    a.annotate("", (x2, y), (x1, y), arrowprops=dict(arrowstyle="->", lw=1.3))
boite(1.3, 1.5, 1.8, 0.8, "Modulateur"); boite(6.4, 1.5, 2.0, 0.8, "Démodulateur")
fleche(0.2, 1.3, 1.9); fleche(3.1, 4.0, 1.9); fleche(5.6, 6.4, 1.9); fleche(8.4, 9.6, 1.9)
a.text(0.2, 2.15, "$s_{BB,Tx}$"); a.text(3.2, 2.15, "$s_{HF,Tx}$"); a.text(5.6, 2.15, "$s_{HF,Rx}$"); a.text(8.6, 2.15, "$s_{BB,Rx}$")
a.annotate("", (5.5, 1.9), (4.1, 1.9), arrowprops=dict(arrowstyle="->", lw=1, ls="--", color="#7E889B"))
a.text(4.8, 2.3, "propagation\ndans l'air", ha="center", fontsize=9, style="italic", color="#555")
a.text(0.7, 1.0, "Information (source)\nbande de base (BB)", ha="center", fontsize=8.5)
a.text(3.6, 1.0, "Signal émis (Tx)\nhaute fréquence (HF, RF)", ha="center", fontsize=8.5)
a.text(6.0, 1.0, "Signal reçu (Rx)\nHF, RF", ha="center", fontsize=8.5)
a.text(9.1, 1.0, "Signal démodulé\n(destinataire), BB", ha="center", fontsize=8.5)
a.text(5, 0.2, "Objectif : $s_{BB,Rx} = s_{BB,Tx}$", ha="center", fontsize=11)
fig.tight_layout(); fig.savefig("01-chaine-modulation.svg")
