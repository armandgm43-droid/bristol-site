"""Figure — Probabilité d'erreur binaire minimale de la M-PAM en fonction de Eb/N0 (TS227, chapitre 4).
D'après le support [poly, p. 138], redessinée (courbes recalculées à partir de la formule de la p. 137, étiquetage de Gray)."""
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
from math import erfc, sqrt, log2
Q = np.vectorize(lambda x: 0.5 * erfc(x / sqrt(2)))
db = np.linspace(0, 15, 301); r = 10**(db / 10)
fig, ax = plt.subplots(figsize=(6.0, 3.6))
for M, c, mk in ((2, BLEU, None), (4, VERT, "s"), (8, MAGENTA, "x"), (16, ORANGE, "D")):
    n = log2(M)
    pb = 2 * (M - 1) / (M * n) * Q(np.sqrt(6 * n / (M**2 - 1) * r))
    ax.semilogy(db, pb, color=c, marker=mk, markevery=20, ms=4, mfc="none", label=f"M = {M}")
ax.axvline(10, color=GRIS, ls="-.", lw=1); ax.axhline(1e-2, color=GRIS, ls="-.", lw=1)
ax.set_xlim(0, 15); ax.set_ylim(1e-16, 1)
ax.set_xlabel(r"$E_b/N_0$ (dB)"); ax.set_ylabel(r"$P_{b,\min}$")
ax.legend(loc="lower left", fontsize=8)
sauver(fig)
