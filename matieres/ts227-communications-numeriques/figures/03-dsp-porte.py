"""Figure — DSP d'un signal mis en forme par une porte de durée Ts (TS227, chapitre 3).
D'après les notes de cours [notes, f. 5 v°] et la correction du TD [td-correction, p. 9], redessinée.
Axes normalisés : f·Ts et Γ/(σ_A² Ts) = sinc²(f Ts). Échelle linéaire."""
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
x = np.linspace(-3.5, 3.5, 3001)
fig, ax = plt.subplots(figsize=(6.6, 2.9))
ax.plot(x, np.sinc(x) ** 2, color=BLEU)
ax.annotate("", xy=(-1, 1.08), xytext=(1, 1.08), arrowprops=dict(arrowstyle="<->", color=ENCRE, lw=1))
ax.text(0, 1.11, "lobe principal", ha="center", va="bottom", fontsize=9)
ax.annotate("", xy=(0, 0.3), xytext=(1, 0.3), arrowprops=dict(arrowstyle="<->", color=VERT, lw=1))
ax.text(1.05, 0.3, r"$B = 1/T_s$", ha="left", va="center", color=VERT, fontsize=9)
ax.set_xlim(-3.5, 3.5); ax.set_ylim(0, 1.3)
ax.set_xticks([-3, -2, -1, 0, 1, 2, 3])
ax.set_xticklabels(["$-3/T_s$", "$-2/T_s$", "$-1/T_s$", "$0$", "$1/T_s$", "$2/T_s$", "$3/T_s$"])
ax.set_yticks([0, 0.5, 1]); ax.set_yticklabels(["$0$", r"$\sigma_A^2 T_s/2$", r"$\sigma_A^2 T_s$"])
ax.set_xlabel("Fréquence $f$", labelpad=4); ax.set_ylabel(r"$\Gamma_{s_l}(f)$")
sauver(fig)
