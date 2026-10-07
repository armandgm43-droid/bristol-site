"""Figure — Densités conditionnelles et seuils optimaux de la 4-PAM équiprobable (TS227, chapitre 4).
D'après le support [poly, p. 116 à 119], redessinée. Paramètres choisis : g0 = 1, σ = 0,6 ; zones d'erreur hachurées pour a1."""
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
from math import pi
g0, s = 1.0, 0.6
a = [-3, -1, 1, 3]
z = np.linspace(-4.8, 4.8, 1501)
f = lambda m: np.exp(-(z - m)**2 / (2 * s**2)) / np.sqrt(2 * pi * s**2)
fig, ax = plt.subplots(figsize=(6.4, 2.8))
for ai, c in zip(a, (VERT, MAGENTA, BLEU, ORANGE)):
    ax.plot(z, f(ai * g0), color=c, lw=1.5)
m = -g0
ax.fill_between(z, f(m), where=(z <= -2 * g0) | (z >= 0), color=MAGENTA, alpha=0.3, lw=0)
for gm in (-2 * g0, 0, 2 * g0):
    ax.axvline(gm, color=ENCRE, ls="--", lw=1)
for i, gm in enumerate((-2 * g0, 0, 2 * g0)):
    ax.text(gm, 0.98, rf"$\gamma_{i}$", ha="center", va="bottom", fontsize=9, transform=ax.get_xaxis_transform())
ax.set_xticks([x * g0 for x in a] + [-2, 0, 2])
ax.set_xticklabels([r"$a_0 g_0$", r"$a_1 g_0$", r"$a_2 g_0$", r"$a_3 g_0$", r"$-2g_0$", "$0$", r"$2g_0$"], fontsize=8)
ax.set_xlim(-4.8, 4.8); ax.set_ylim(0, None); ax.set_yticks([])
ax.set_xlabel(r"$r_n$  (constellation $\{-3, -1, 1, 3\}$)"); ax.set_ylabel("Densité")
sauver(fig)
