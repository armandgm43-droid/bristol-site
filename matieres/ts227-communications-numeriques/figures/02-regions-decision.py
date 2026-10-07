"""Figure F5 — Régions et seuils de décision de la 4-PAM (TS227, chapitre 2).
D'après le support [poly, p. 32 et 34], redessinée. Seuils : -2,5 ; 0,5 ; 1,5."""
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

seuils = [-2.5, 0.5, 1.5]
bornes = [-4.6] + seuils + [4.6]
symb = [-3, -1, 1, 3]
teintes = ["#E6ECF8", "#F6E7EF", "#E4F3EE", "#FBF0E0"]
fig, ax = plt.subplots(figsize=(6.6, 2.3))
for (g, d), s, c in zip(zip(bornes[:-1], bornes[1:]), symb, teintes):
    ax.axvspan(g, d, color=c, zorder=0)
    ax.text((g + d) / 2, 0.55, f"$\\hat{{a}}_n = {s}$".replace("-", "−"), ha="center", fontsize=10)
for s in seuils:
    ax.axvline(s, color=ENCRE, ls="--", lw=1.1, zorder=2)
ax.text(-0.5, 1.05, "Seuils de décision : $-2{,}5$ ; $0{,}5$ ; $1{,}5$".replace("-", "−"),
        ha="center", fontsize=9, color="#333333")
ax.axhline(0, color="#555555", lw=0.8, zorder=1)
ax.plot(symb, [0] * 4, "o", ms=9, color=BLEU, zorder=3)
# Échantillon reçu r_n = 1,7 (position de la croix, lue sur le support)
ax.plot([1.7], [0], "x", ms=9, mew=2, color=ENCRE, zorder=4)
ax.annotate("Si $r_n$ tombe ici,\non décide $\\hat{a}_n = 3$", xy=(1.7, -0.05), xytext=(2.9, -0.75),
            fontsize=9, ha="center", arrowprops=dict(arrowstyle="->", color=ENCRE, lw=0.9))
ax.set_xlim(-4.6, 4.6); ax.set_ylim(-1.15, 1.3)
ax.set_xticks(range(-4, 5)); virgule(ax, "x")
ax.set_yticks([]); ax.grid(False); ax.spines["left"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.set_xlabel("Voie en phase")
sauver(fig)
