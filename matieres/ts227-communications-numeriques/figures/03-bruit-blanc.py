"""Figure — DSP d'un bruit blanc (TS227, chapitre 3).
D'après les notes de cours [notes, f. 5 r°], redessinée. Bande [fp − B, fp + B] hachurée (notes) ;
bande symétrique des fréquences négatives ajoutée en pointillés gris (puissance totale d'un bruit réel : 2 N0 B).
Valeurs fp = 3, B = 1 choisies pour le dessin (unités arbitraires)."""
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
fp, B, N2 = 3.0, 1.0, 1.0
fig, ax = plt.subplots(figsize=(6.6, 2.6))
ax.axhline(N2, color=BLEU, lw=1.8)
ax.fill_between([fp - B, fp + B], 0, N2, facecolor="none", edgecolor=BLEU, hatch="///", lw=1.0)
ax.plot([-fp - B, -fp - B, -fp + B, -fp + B], [0, N2, N2, 0], color=GRIS, ls=":", lw=1.4)
ax.text(fp, N2 / 2, "$N_0 B$", ha="center", va="center", color=ENCRE, bbox=dict(facecolor="white", edgecolor="none", pad=2))
ax.axvline(0, color="#555555", lw=0.8)
ax.set_xlim(-5, 5); ax.set_ylim(0, 1.35)
ax.set_xticks([-fp - B, -fp, -fp + B, 0, fp - B, fp, fp + B])
ax.set_xticklabels(["$-f_p - B$", "$-f_p$", "$-f_p + B$", "$0$", "$f_p - B$", "$f_p$", "$f_p + B$"], fontsize=8.5)
ax.set_yticks([0, N2]); ax.set_yticklabels(["$0$", r"$\frac{N_0}{2}$"])
ax.set_xlabel("Fréquence $f$", labelpad=4); ax.set_ylabel(r"$\Gamma(f)$")
sauver(fig)
