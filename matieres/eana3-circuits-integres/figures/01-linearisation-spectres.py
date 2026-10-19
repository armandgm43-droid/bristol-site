"""Figure — Linéarisation : spectre d'entrée (une raie) et spectre de sortie d'un amplificateur non linéaire (EANA3, chapitre 1).
D'après les notes externes [tableau-2020-c01, p. 6] et [notes-2023-c01, p. 2], redessinée.
Amplitudes des harmoniques arbitraires (les notes ne donnent pas de valeurs)."""
import matplotlib
matplotlib.use("svg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np
from pathlib import Path

# --- Style commun des figures Bristol (recopié dans chaque script) ---
plt.rcParams.update({
    "font.family": "DejaVu Sans", "mathtext.fontset": "dejavusans", "font.size": 10,
    "axes.grid": True, "grid.color": "#DADADA", "grid.linewidth": 0.6,
    "axes.edgecolor": "#555555", "axes.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "lines.linewidth": 1.8, "legend.frameon": False,
    "svg.hashsalt": "bristol",  # rendu SVG reproductible
})
BLEU, VERT, MAGENTA, ORANGE = "#2B59C3", "#1B9E77", "#A23B72", "#E08A1E"
GRIS = "#7E889B"   # éléments ajoutés par rapport à la source (conventions.md § 9)
ENCRE = "#222222"

def virgule(ax, axes="xy"):
    """Virgule décimale et vrai signe moins sur les graduations."""
    f = mticker.FuncFormatter(lambda x, _: f"{x:g}".replace(".", ",").replace("-", "−"))
    if "x" in axes: ax.xaxis.set_major_formatter(f)
    if "y" in axes: ax.yaxis.set_major_formatter(f)

def sauver(fig):
    fig.savefig(Path(__file__).with_suffix(".svg"), bbox_inches="tight", metadata={"Date": None})
# --- Fin du style commun ---
fig, axs = plt.subplots(1, 2, figsize=(6.4, 2.3), sharey=True)
f0 = 1
for ax, titre in zip(axs, ["Entrée de l'amplificateur", "Sortie de l'amplificateur"]):
    ax.set_xlim(0, 4.2); ax.set_ylim(0, 1.15)
    ax.set_xticks([1, 2, 3]); ax.set_xticklabels(["$f_0$", "$2f_0$", "$3f_0$"])
    ax.set_yticks([]); ax.grid(False)
    ax.set_xlabel("$f$"); ax.set_title(titre, fontsize=10)
axs[0].vlines(f0, 0, 0.45, color=BLEU, lw=2.4)
axs[1].vlines(f0, 0, 1.0, color=BLEU, lw=2.4)
axs[1].vlines([2, 3], 0, [0.32, 0.16], color=MAGENTA, lw=2.4)
axs[1].annotate("harmoniques\n(distorsion)", xy=(2.05, 0.33), xytext=(2.4, 0.75), color=MAGENTA, fontsize=9,
                arrowprops=dict(arrowstyle="->", color=MAGENTA, lw=0.9))
axs[0].set_ylabel("amplitude")
fig.tight_layout()
sauver(fig)
