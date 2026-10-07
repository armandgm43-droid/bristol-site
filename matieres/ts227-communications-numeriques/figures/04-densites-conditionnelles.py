"""Figure — Densités de R_n conditionnellement au bit émis, seuil γ et probabilités d'erreur (TS227, chapitre 4).
D'après le support [poly, p. 103 à 106], redessinée. Paramètres choisis : g0 = 2, σ = 1,3, γ = 0,5 (lecture approximative du support)."""
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
g0, s, gam = 2.0, 1.3, 0.5
z = np.linspace(-6, 6, 1201)
f = lambda m: np.exp(-(z - m)**2 / (2 * s**2)) / np.sqrt(2 * pi * s**2)
fig, ax = plt.subplots(figsize=(6.4, 3.0))
ax.plot(z, f(-g0), color=MAGENTA, label=r"$B_n = 0$ ($A_n = -1$) : $f_{Z'}(r + g_0)$")
ax.plot(z, f(g0), color=BLEU, label=r"$B_n = 1$ ($A_n = 1$) : $f_{Z'}(r - g_0)$")
ax.fill_between(z, f(-g0), where=z >= gam, color=MAGENTA, alpha=0.25, lw=0)
ax.fill_between(z, f(g0), where=z <= gam, color=BLEU, alpha=0.25, lw=0)
ax.axvline(gam, color=ENCRE, ls="--", lw=1)
ax.text(gam + 0.1, 0.335, r"seuil $\gamma$", fontsize=9)
ax.annotate(r"$P(\hat{B}_n = 1 \mid B_n = 0)$", xy=(1.6, 0.03), xytext=(3.2, 0.2), fontsize=9, color=MAGENTA,
            arrowprops=dict(arrowstyle="->", color=MAGENTA, lw=0.8))
ax.annotate(r"$P(\hat{B}_n = 0 \mid B_n = 1)$", xy=(-0.6, 0.03), xytext=(-6, 0.2), fontsize=9, color=BLEU,
            arrowprops=dict(arrowstyle="->", color=BLEU, lw=0.8))
ax.set_xticks([-g0, 0, gam, g0]); ax.set_xticklabels([r"$-g_0$", "$0$", r"$\gamma$", r"$g_0$"])
ax.set_xlim(-6, 6); ax.set_ylim(0, 0.37)
ax.set_xlabel("$r_n$"); ax.set_ylabel("Densité de probabilité"); virgule(ax, "y")
ax.legend(loc="upper left", fontsize=8, bbox_to_anchor=(0, 1.22), ncol=1)
sauver(fig)
