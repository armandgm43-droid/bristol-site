"""Figure — Tension de seuil V_th des NMOS SOI en fonction de la tension de body V_BB (TD 5) (EANA3, chapitre 5).
D'après le support [support, p. 22, figure 2], redessinée : droite passant par (0 mV ; 450 mV) et (1000 mV ; 400 mV),
relevée sur la figure de l'énoncé (lecture graphique)."""
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

vbb = np.linspace(0, 1250, 50)
vth = 450 - 0.05 * vbb

fig, ax = plt.subplots(figsize=(5.6, 3.2))
ax.plot(vbb, vth, color=BLEU)
for x, y in [(0, 450), (1000, 400)]:
    ax.plot([x, x], [380, y], color=GRIS, ls=":", lw=0.9); ax.plot([0, x], [y, y], color=GRIS, ls=":", lw=0.9)
    ax.plot(x, y, "o", color=MAGENTA, ms=4)
ax.set_xlabel(r"tension de body $V_{BB}$ (mV)"); ax.set_ylabel(r"tension de seuil $V_{th}$ (mV)")
ax.set_xlim(0, 1300); ax.set_ylim(380, 460)
virgule(ax)
sauver(fig)
