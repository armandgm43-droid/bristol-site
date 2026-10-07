"""Figure — Densité gaussienne et intervalles ±σ, ±3σ (TS227, chapitre 3).
D'après le support [poly, p. 78] et les notes de cours [notes, f. 2 v°], redessinée.
Les probabilités affichées (en gris) sont calculées : le support et les notes donnent les arrondis 67 % et 99 %. Axe normalisé : (x − μ)/σ."""
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
from math import erf, sqrt

x = np.linspace(-4.2, 4.2, 1201)
f = np.exp(-x**2 / 2) / np.sqrt(2 * np.pi)
fig, ax = plt.subplots(figsize=(6.4, 3.0))
ax.fill_between(x, f, where=np.abs(x) <= 3, color=BLEU, alpha=0.10, lw=0)
ax.fill_between(x, f, where=np.abs(x) <= 1, color=BLEU, alpha=0.22, lw=0)
ax.plot(x, f, color=BLEU)
p1, p3 = erf(1 / sqrt(2)), erf(3 / sqrt(2))
for k, p, y in ((1, p1, 0.47), (3, p3, 0.53)):
    ax.annotate("", xy=(-k, y), xytext=(k, y), arrowprops=dict(arrowstyle="<->", color=ENCRE, lw=1))
    ax.vlines([-k, k], 0, y, colors=ENCRE, lw=0.8, ls="--")
    txt = f"≈ {100 * p:.1f} %".replace(".", ",")
    ax.text(0, y + 0.012, f"$\\pm {'' if k == 1 else '3'}\\sigma$ : " + txt, ha="center", va="bottom", color=GRIS, fontsize=9)
ax.set_xlim(-4.2, 4.2); ax.set_ylim(0, 0.62)
ax.set_xticks([-3, -1, 0, 1, 3])
ax.set_xticklabels([r"$\mu - 3\sigma$", r"$\mu - \sigma$", r"$\mu$", r"$\mu + \sigma$", r"$\mu + 3\sigma$"])
ax.set_yticks([0, 1 / np.sqrt(2 * np.pi)]); ax.set_yticklabels(["$0$", r"$\frac{1}{\sqrt{2\pi\sigma^2}}$"])
ax.set_xlabel("$x$"); ax.set_ylabel("Densité $f_X(x)$")
sauver(fig)
