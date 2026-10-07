"""Figure F13 — Filtres des exercices sur le critère de Nyquist (TS227, chapitre 2).
D'après le support [poly, p. 47 à 51], redessinée.
(a) g(t), p. 47 ; (b) g(t), p. 48 et 50 ; (c) G(f), p. 49 ; (d) h(t), p. 51.
Points pleins : valeur prise ; points vides : valeur exclue (comme sur le support)."""
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

def porte(ax, nom):
    ax.plot([-2, 0], [0, 0], color=BLEU); ax.plot([0, 1], [10, 10], color=BLEU); ax.plot([1, 3], [0, 0], color=BLEU)
    ax.plot([0, 0], [0, 10], color=BLEU, lw=0.8, ls=":"); ax.plot([1, 1], [0, 10], color=BLEU, lw=0.8, ls=":")
    ax.plot([0, 1], [10, 0], "o", ms=6, color=BLEU, zorder=3)                    # valeurs prises
    ax.plot([0, 1], [0, 10], "o", ms=6, color=BLEU, mfc="white", zorder=3)       # valeurs exclues
    ax.set_xlim(-2, 3); ax.set_xlabel("$t$ (ms)"); ax.set_ylabel(nom)

def triangle(ax, demi, nom, unite):
    ax.plot([-2 * demi, -demi, 0, demi, 2 * demi], [0, 0, 10, 0, 0], color=BLEU)
    ax.set_xlim(-2 * demi, 2 * demi); ax.set_xlabel(unite); ax.set_ylabel(nom)

fig, axs = plt.subplots(2, 2, figsize=(7.0, 4.8))
porte(axs[0, 0], "$g(t)$"); axs[0, 0].set_title("(a) p. 47", fontsize=10)
triangle(axs[0, 1], 1, "$g(t)$", "$t$ (ms)"); axs[0, 1].set_title("(b) p. 48 et 50", fontsize=10)
triangle(axs[1, 0], 1000, "$G(f)$", "$f$ (Hz)"); axs[1, 0].set_title("(c) p. 49", fontsize=10)
porte(axs[1, 1], "$h(t)$"); axs[1, 1].set_title("(d) p. 51", fontsize=10)
axs[0, 1].set_xticks([-2, -1.5, -1, -0.5, 0, 0.5, 1, 1.5, 2])
axs[1, 0].set_xticks([-2000, -1000, 0, 1000, 2000])
for ax in axs.flat:
    ax.set_ylim(-0.8, 11); ax.set_yticks([0, 5, 10]); virgule(ax)
fig.tight_layout()
sauver(fig)
