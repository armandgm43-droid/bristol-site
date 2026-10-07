"""Figure — Probabilité d'erreur binaire Pb = Q(g0/σ) en fonction du RSB 20 log10(g0/σ) (TS227, chapitre 4).
D'après le support [poly, p. 113], redessinée (courbe recalculée à partir de la formule)."""
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
from math import erfc, sqrt
Q = np.vectorize(lambda x: 0.5 * erfc(x / sqrt(2)))
db = np.linspace(-10, 10, 401)
fig, ax = plt.subplots(figsize=(6.0, 3.2))
ax.semilogy(db, Q(10**(db / 20)), color=BLEU)
ax.set_xlim(-10, 10); ax.set_ylim(1e-4, 1)
ax.set_xticks(range(-10, 11, 2))
ax.grid(True, which="both", color="#DADADA", lw=0.5)
ax.set_xlabel(r"$20 \log_{10}(g_0/\sigma)$ (dB)"); ax.set_ylabel("$P_b$")
virgule(ax, "x")
sauver(fig)
