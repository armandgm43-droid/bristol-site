"""Figure — Filtre adapté à une porte, version causale et filtre global (TS227, chapitre 4).
D'après les notes de cours [notes, f. 4 v°] et la correction du TD [td-correction, p. 10-11, fig. 4 à 6], redessinée. Retard choisi D = Ts."""
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
Ts, D = 1.0, 1.0
t = np.linspace(-2.2, 3.2, 2201)
porte = lambda x: ((x >= 0) & (x < Ts)).astype(float)
fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.2, 2.7), sharey=False)
a1.plot(t, porte(t), color=BLEU, label=r"$h(t)$")
a1.plot(t, porte(-t) * 0.97, color=ORANGE, ls="--", label=r"$h^*(-t)$ (non causal)")
a1.plot(t, porte(D - t) * 0.94, color=VERT, label=r"$h^*(D - t)$, $D = T_s$")
a1.set_xticks([-2, -1, 0, 1, 2, 3]); a1.set_xticklabels([r"$-2T_s$", r"$-T_s$", "$0$", r"$T_s$", r"$2T_s$", r"$3T_s$"])
a1.set_ylim(-0.05, 1.45); a1.set_yticks([0, 1]); a1.set_title("(a) filtre de mise en forme et filtre adapté", fontsize=9)
a1.legend(fontsize=7.5, loc="upper left")
g = np.clip(Ts - np.abs(t - D), 0, None)
a2.plot(t, g, color=BLEU, label=r"$g(t) = R_h(t - D)$")
k = np.arange(-1, 4)
a2.plot(D + k * Ts - D, np.clip(Ts - np.abs(k * Ts - D), 0, None), "o", color=MAGENTA, ms=4, label=r"$g(nT_s)$")
a2.set_xticks([-1, 0, 1, 2, 3]); a2.set_xticklabels([r"$-T_s$", "$0$", r"$D$", r"$D + T_s$", r"$D + 2T_s$"], fontsize=8)
a2.set_yticks([0, 1]); a2.set_yticklabels(["$0$", r"$T_s$"]); a2.set_ylim(-0.05, 1.45)
a2.set_title("(b) filtre global et échantillons", fontsize=9)
a2.legend(fontsize=7.5, loc="upper right")
for ax in (a1, a2): ax.set_xlabel("$t$")
fig.tight_layout()
sauver(fig)
