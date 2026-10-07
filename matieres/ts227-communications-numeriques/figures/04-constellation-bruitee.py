"""Figure — Échantillons reçus d'une 4-PAM avec σ = 1/4 et intervalles ±3σ (TS227, chapitre 4, TD ex. 5, q. 12).
Reconstruite (aucune source ne donne de solution) : 400 échantillons simulés, graine 4 ; seuils optimaux ajoutés en pointillés gris."""
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
rng = np.random.default_rng(4)
s = 0.25
A = rng.choice([-3, -1, 1, 3], 400)
r = A + s * rng.standard_normal(400)
fig, ax = plt.subplots(figsize=(6.4, 1.9))
ax.scatter(r, rng.uniform(-0.25, 0.25, 400), s=4, color=BLEU, alpha=0.5, lw=0)
for a in (-3, -1, 1, 3):
    ax.add_patch(plt.Rectangle((a - 3 * s, -0.4), 6 * s, 0.8, fill=False, ec=ENCRE, lw=0.9))
    ax.plot([a], [0], "x", color=MAGENTA, ms=8, mew=2)
for gm in (-2, 0, 2):
    ax.axvline(gm, color=GRIS, ls=":", lw=1.2)
ax.set_xlim(-4.3, 4.3); ax.set_ylim(-0.6, 0.6); ax.set_yticks([])
ax.set_xticks([-3, -2, -1, 0, 1, 2, 3]); ax.grid(False)
ax.set_xlabel(r"$r_l[n]$"); virgule(ax, "x")
sauver(fig)
