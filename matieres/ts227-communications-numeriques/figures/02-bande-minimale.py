"""Figure F12 — Bande minimale : chevauchement nécessaire des répliques (TS227, chapitre 2).
D'après les notes de cours [notes, f. 2 r° et f. 3 r°], redessinée. Axes normalisés (f·Ts, G/(g0·Ts)).
Forme du spectre choisie pour l'illustration (cosinus surélevé, beta = 0,4, donc B = 0,7/Ts)."""
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

beta = 0.4; B = (1 + beta) / 2
x = np.linspace(-1, 2, 2001)
fig, ax = plt.subplots(figsize=(6.4, 2.9))
ax.plot(x, cosinus_sureleve(x, beta), color=BLEU, label="$G(f)$, support $[-B, B]$")
ax.plot(x, cosinus_sureleve(x - 1, beta), color=MAGENTA, ls="--", lw=1.4, label=r"$G(f - 1/T_s)$")
ax.axvspan(1 - B, B, color="#DDDDDD", zorder=0)
ax.text(0.5, 1.08, "chevauchement", ha="center", fontsize=9)
ax.annotate("", xy=(1 - B, 1.02), xytext=(B, 1.02), arrowprops=dict(arrowstyle="<->", lw=0.9, color=ENCRE))
ax.set_xticks([-B, 0, 1 - B, B, 1])
ax.set_xticklabels(["$-B$", "$0$", r"$1/T_s - B$", "$B$", r"$1/T_s$"])
ax.set_yticks([0, 1]); ax.set_yticklabels(["$0$", r"$g_0 T_s$"])
ax.set_xlim(-1, 2); ax.set_ylim(-0.05, 1.3)
ax.set_xlabel("Fréquence $f$")
ax.legend(loc="upper center", ncol=2, fontsize=8.5, bbox_to_anchor=(0.5, -0.22))
sauver(fig)
