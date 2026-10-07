"""Figure F7 — Porte Pi_{Ts/2}(t) et filtre de mise en forme h(t) du code Manchester (TS227, chapitre 2).
D'après les notes de cours [notes, f. 1 v°], redessinée. L'amplitude (±1) n'est pas donnée par les notes :
elle est choisie (complément)."""
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

fig, axs = plt.subplots(1, 2, figsize=(6.8, 2.4))
# (a) porte de largeur Ts/2 centrée en 0
t = [-0.6, -0.25, -0.25, 0.25, 0.25, 0.6]
axs[0].plot(t, [0, 0, 1, 1, 0, 0], color=BLEU)
axs[0].set_title(r"$\Pi_{T_s/2}(t)$", fontsize=10)
axs[0].set_xticks([-0.25, 0, 0.25]); axs[0].set_xticklabels([r"$-T_s/4$", "$0$", r"$T_s/4$"])
# (b) h(t) du code Manchester
t = [-0.3, 0, 0, 0.5, 0.5, 1, 1, 1.3]
axs[1].plot(t, [0, 0, 1, 1, -1, -1, 0, 0], color=BLEU)
axs[1].set_title("$h(t)$ (code Manchester)", fontsize=10)
axs[1].set_xticks([0, 0.5, 1]); axs[1].set_xticklabels(["$0$", r"$T_s/2$", "$T_s$"])
for ax in axs:
    ax.axhline(0, color="#555555", lw=0.8)
    ax.set_ylim(-1.4, 1.4); ax.set_yticks([-1, 0, 1]); virgule(ax, "y")
    ax.set_xlabel("$t$")
fig.tight_layout()
sauver(fig)
