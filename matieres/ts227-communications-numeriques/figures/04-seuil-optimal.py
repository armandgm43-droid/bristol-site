"""Figure — Seuil optimal γ*(p0) de la décision binaire (TS227, chapitre 4).
D'après le support [poly, p. 108], redessinée. Axe vertical normalisé : γ* / (σ²/(2 g0)) = ln(p0/(1 − p0))."""
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
p = np.linspace(0.005, 0.995, 600)
fig, ax = plt.subplots(figsize=(6.0, 3.0))
ax.plot(p, np.log(p / (1 - p)), color=BLEU)
ax.plot([0.5], [0], "o", color=ENCRE, ms=4)
ax.annotate(r"$\gamma^*(0{,}5) = 0$", xy=(0.5, 0), xytext=(0.56, -2.2), fontsize=9, arrowprops=dict(arrowstyle="->", lw=0.8))
ax.text(0.80, 3.6, r"$\gamma^* \to +\infty$ quand $p_0 \to 1$", fontsize=9, ha="center")
ax.text(0.20, -4.4, r"$\gamma^* \to -\infty$ quand $p_0 \to 0$", fontsize=9, ha="center")
ax.set_xlim(0, 1); ax.set_ylim(-5, 5)
ax.set_xlabel(r"$p_0 = P(B_n = 0)$")
ax.set_ylabel(r"$\gamma^*(p_0)\ /\ \dfrac{\sigma^2}{2 g_0}$")
virgule(ax)
sauver(fig)
