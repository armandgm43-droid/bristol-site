"""Figure — Constellations 2-PAM, 4-PAM et 8-PAM de même puissance moyenne (partiel TS227 2019-2020, q. 11).
Figure calculée (complément) : symboles ±d, ±3d, … avec σ_A² = d²(M² − 1)/3 = 1, donc d = √(3/(M² − 1)).
Seuils de décision en pointillés gris ; la flèche indique la demi-distance d entre un symbole et le seuil voisin."""
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
fig, ax = plt.subplots(figsize=(6.4, 2.4))
for i, M in enumerate((2, 4, 8)):
    d = np.sqrt(3 / (M ** 2 - 1))
    a = d * np.arange(-(M - 1), M, 2)
    y = 2 - i
    ax.plot(a, np.full(M, y), "x", color=MAGENTA, ms=8, mew=2)
    for s in d * np.arange(-(M - 2), M - 1, 2):
        ax.plot([s, s], [y - 0.3, y + 0.3], color=GRIS, ls=":", lw=1.2)
    ax.annotate("", xy=(a[-1] - d, y - 0.25), xytext=(a[-1], y - 0.25),
                arrowprops=dict(arrowstyle="<->", color=ENCRE, lw=0.9))
    ax.text(a[-1] - d / 2, y - 0.45, f"d = {d:.2f}".replace(".", ","), ha="center", va="top", fontsize=8)
    ax.text(-2.2, y, f"M = {M} ($n_b$ = {int(np.log2(M))})", va="center", ha="right", fontsize=9)
ax.set_ylim(-0.8, 2.5); ax.set_xlim(-2.3, 2.3); ax.set_yticks([]); ax.grid(False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("amplitude des symboles (puissance moyenne fixée à 1)"); virgule(ax, "x")
sauver(fig)
