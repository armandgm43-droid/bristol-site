"""Figure F6 — Constellations antipodale et OOK de même puissance moyenne (0,5 W) (TS227, chapitre 2).
D'après les notes de cours [notes, f. 1 r°], redessinée."""
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

fig, axs = plt.subplots(2, 1, figsize=(6.0, 3.6), sharex=True)
r = np.sqrt(0.5)
cas = [
    ("Constellation antipodale", [-r, r], ["", ""], r"$\sqrt{2}$", [-r, 0, r], [r"$-\sqrt{1/2}$", "$0$", r"$\sqrt{1/2}$"]),
    ("Constellation OOK", [0, 1], ["[0]", "[1]"], "$1$", [0, 1], ["$0$", "$1$"]),
]
for ax, (nom, pts, etiq, ecart, ticks, tlabels) in zip(axs, cas):
    ax.axhline(0, color="#555555", lw=0.8, zorder=1)
    ax.plot(pts, [0, 0], "o", ms=9, color=BLEU, zorder=3)
    for p, e in zip(pts, etiq):
        if e: ax.text(p, 0.3, e, ha="center", family="DejaVu Sans Mono")
    for x0, lab in zip(ticks, tlabels):
        ax.plot([x0, x0], [-0.08, 0.08], color="#555555", lw=0.8)
        ax.text(x0, -0.45, lab, ha="center", va="center")
    ax.annotate("", xy=(pts[0], -1.0), xytext=(pts[1], -1.0),
                arrowprops=dict(arrowstyle="<->", color=ENCRE, lw=1))
    ax.text(np.mean(pts), -1.35, "écart " + ecart, ha="center", va="center", fontsize=9)
    ax.set_title(nom, fontsize=10, loc="left")
    ax.set_ylim(-1.6, 0.8); ax.set_yticks([]); ax.set_xticks([]); ax.grid(False)
    for c in ("left", "bottom"): ax.spines[c].set_visible(False)
axs[1].set_xlim(-1.1, 1.3)
fig.suptitle("Même puissance moyenne : $P = 0{,}5$ W", fontsize=10)
fig.tight_layout()
sauver(fig)
