"""Figure F9 — Répliques G(f - m/Ts) d'un filtre de Nyquist et leur somme (TS227, chapitre 2).
D'après les notes de cours [notes, f. 2 r° et f. 3 r°], redessinée. Axes normalisés (f·Ts, G/(g0·Ts)).
Le filtre (cosinus surélevé, beta = 0,5) est choisi pour l'illustration : les notes n'en donnent qu'un croquis.
Répliques m = ±2 ajoutées (pointillés gris)."""
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
    """G(f)/(g0 Ts) en fonction de x = f Ts."""
    x = np.abs(x); a, b = (1 - beta) / 2, (1 + beta) / 2
    return np.where(x <= a, 1.0, np.where(x <= b, 0.5 * (1 + np.cos(np.pi / beta * (x - a))), 0.0))

beta = 0.5
x = np.linspace(-2.2, 2.2, 2001)
fig, ax = plt.subplots(figsize=(6.6, 2.9))
couleurs = {-1: VERT, 0: BLEU, 1: MAGENTA}
noms = {-1: r"$G(f + 1/T_s)$", 0: "$G(f)$", 1: r"$G(f - 1/T_s)$"}
for m in (-2, 2):
    ax.plot(x, cosinus_sureleve(x - m, beta), color=GRIS, lw=1.2, ls=":")
for m in (-1, 0, 1):
    ax.plot(x, cosinus_sureleve(x - m, beta), color=couleurs[m], lw=1.8 if m == 0 else 1.4,
            ls="-" if m == 0 else "--", label=noms[m])
somme = sum(cosinus_sureleve(x - m, beta) for m in range(-4, 5))
ax.plot(x, somme, color=ENCRE, lw=2.2, label=r"$\sum_m G(f - m/T_s)$")
ax.set_xlim(-2.2, 2.2); ax.set_ylim(-0.05, 1.3)
ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_xticklabels(["$-2/T_s$", "$-1/T_s$", "$0$", "$1/T_s$", "$2/T_s$"])
ax.set_yticks([0, 0.5, 1]); ax.set_yticklabels(["$0$", r"$g_0 T_s/2$", r"$g_0 T_s$"])
ax.set_xlabel("Fréquence $f$"); ax.set_ylabel("Réponse en fréquence")
ax.legend(loc="upper center", ncol=4, fontsize=8.5, bbox_to_anchor=(0.5, 1.17))
sauver(fig)
