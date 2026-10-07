"""Figure F10 — Règle de symétrie du critère de Nyquist (TS227, chapitre 2).
D'après le support [poly, p. 41], redessinée, avec l'ordonnée du centre corrigée (g0·Ts/2 au lieu de g0/2,
bloc av-centre-symetrie-nyquist). Axes normalisés (f·Ts, G/(g0·Ts)).
Cosinus surélevé de facteur de retombée beta = 0,2 : valeur estimée à partir de la figure du support."""
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

def cosinus_sureleve(x, beta):
    x = np.abs(x); a, b = (1 - beta) / 2, (1 + beta) / 2
    return np.where(x <= a, 1.0, np.where(x <= b, 0.5 * (1 + np.cos(np.pi / beta * (x - a))), 0.0))

beta = 0.2
x = np.linspace(0, 1, 1001)
fig, ax = plt.subplots(figsize=(5.2, 3.0))
ax.plot(x, cosinus_sureleve(x, beta), color=BLEU)
# Centre de symétrie (1/(2Ts), g0 Ts/2)
ax.plot([0.5, 0.5], [0, 0.5], color=ENCRE, ls=":", lw=1)
ax.plot([0, 0.5], [0.5, 0.5], color=ENCRE, ls=":", lw=1)
ax.plot([0.5], [0.5], "o", ms=7, color=ENCRE, zorder=4)
ax.set_xlim(0, 1); ax.set_ylim(-0.03, 1.12)
ax.set_xticks([0, 0.25, 0.5, 0.75, 1])
ax.set_xticklabels(["$0$", "", r"$1/(2T_s)$", "", r"$1/T_s$"])
ax.set_yticks([0, 0.5, 1]); ax.set_yticklabels(["$0$", r"$g_0 T_s/2$", r"$g_0 T_s$"])
ax.set_xlabel("Fréquence $f$"); ax.set_ylabel("$G(f)$")
sauver(fig)
