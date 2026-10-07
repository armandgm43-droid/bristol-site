"""Figure F12 — Bande minimale : spectre rectangulaire de bande B = 1/(2Ts) (TS227, chapitre 2).
D'après les notes de cours [notes, f. 2 r°] (spectres rectangulaires), redessinée. Axes normalisés (f·Ts, G/(g0·Ts)).
Cas limite de la bande minimale (beta = 0) : les répliques se juxtaposent exactement (décision d'Armand, 2026-10-07)."""
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

def rectangle(x, B):
    return np.where(np.abs(x) <= B, 1.0, 0.0)

B = 0.5   # bande minimale 1/(2 Ts), en f·Ts
x = np.linspace(-1, 2, 3001)
fig, ax = plt.subplots(figsize=(6.4, 2.9))
ax.plot(x, rectangle(x, B), color=BLEU, label="$G(f)$, support $[-B, B]$")
ax.plot(x, rectangle(x - 1, B), color=MAGENTA, ls="--", lw=1.4, label=r"$G(f - 1/T_s)$")
ax.annotate(r"$B = 1/T_s - B$", xy=(B, 1.0), xytext=(B, 1.17), ha="center", fontsize=9,
            arrowprops=dict(arrowstyle="->", lw=0.9, color=ENCRE))
ax.set_xticks([-B, 0, B, 1])
ax.set_xticklabels(["$-B$", "$0$", r"$B = \dfrac{1}{2T_s}$", r"$1/T_s$"])
ax.set_yticks([0, 1]); ax.set_yticklabels(["$0$", r"$g_0 T_s$"])
ax.set_xlim(-1, 2); ax.set_ylim(-0.05, 1.32)
ax.set_xlabel("Fréquence $f$")
ax.legend(loc="upper center", ncol=2, fontsize=8.5, bbox_to_anchor=(0.5, -0.25))
sauver(fig)
