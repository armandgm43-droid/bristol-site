"""Figure F2 — Constellation 4-PAM et étiquetage de Gray (TS227, chapitre 2).
D'après le support [poly, p. 22] et les notes [notes, f. 1 r°], redessinée."""
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

fig, ax = plt.subplots(figsize=(6.4, 1.9))
symb = [-3, -1, 1, 3]
etiq = ["00", "01", "11", "10"]
ax.axhline(0, color="#555555", lw=0.8, zorder=1)
ax.plot(symb, [0] * 4, "o", ms=9, color=BLEU, zorder=3)
for s, e in zip(symb, etiq):
    ax.text(s, 0.45, f"[{e}]", ha="center", va="bottom", family="DejaVu Sans Mono", fontsize=10)
ax.text(0, 1.05, "Étiquettes", ha="center", fontsize=9, color="#555555")
ax.set_xlim(-4.3, 4.6); ax.set_ylim(-0.8, 1.4)
ax.set_xticks(range(-4, 5)); virgule(ax, "x")
ax.set_yticks([]); ax.grid(False)
ax.spines["left"].set_visible(False); ax.spines["bottom"].set_position("zero")
ax.set_xlabel("Voie en phase (symboles $a_n$)")
sauver(fig)
