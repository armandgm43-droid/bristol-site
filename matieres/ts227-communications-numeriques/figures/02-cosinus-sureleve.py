"""Figure F11 — Exemple de filtre de Nyquist (cosinus surélevé), en temps et en fréquence (TS227, chapitre 2).
D'après le support [poly, p. 43-45] et les notes [notes, f. 2 r°], redessinée.
Axes normalisés (t/Ts, g/g0 ; f·Ts, G/(g0·Ts)), décision d'Armand du 2026-10-07 (bloc
av-echelles-figure-cosinus-sureleve). beta = 0,2 : valeur estimée à partir de la figure du support."""
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

def cosinus_sureleve_temps(u, beta):
    """g(t)/g0 en fonction de u = t/Ts (valeur limite aux points |u| = 1/(2 beta))."""
    u = np.asarray(u, dtype=float)
    den = 1 - (2 * beta * u) ** 2
    sing = np.isclose(den, 0)
    val = np.sinc(u) * np.cos(np.pi * beta * u) / np.where(sing, 1, den)
    return np.where(sing, np.pi / 4 * np.sinc(1 / (2 * beta)), val)

beta = 0.2
fig, (at, af) = plt.subplots(1, 2, figsize=(7.2, 2.9))
u = np.linspace(-5, 5, 2001)
at.plot(u, cosinus_sureleve_temps(u, beta), color=BLEU)
m = np.arange(-5, 6)
at.plot(m, cosinus_sureleve_temps(m, beta), "o", ms=6, color=ENCRE, mfc="white", zorder=3,
        label="$g(mT_s)$")
at.axhline(0, color="#555555", lw=0.8)
at.set_xlim(-5.2, 5.2); at.set_xticks(range(-4, 5, 2))
at.set_xlabel("$t/T_s$"); at.set_ylabel("$g(t)/g_0$"); at.set_title("Critère temporel", fontsize=10)
at.legend(loc="upper right", fontsize=8.5)

x = np.linspace(-2.2, 2.2, 2001)
for k in (-2, -1, 1, 2):
    af.plot(x, cosinus_sureleve(x - k, beta), color=MAGENTA, ls="--", lw=1.1)
af.plot(x, cosinus_sureleve(x, beta), color=BLEU, label="$G(f)$", zorder=3)
af.plot([], [], color=MAGENTA, ls="--", lw=1.1, label=r"$G(f - m/T_s)$, $m \neq 0$")
af.plot(x, sum(cosinus_sureleve(x - k, beta) for k in range(-4, 5)), color=ENCRE, lw=1.4, ls=(0, (1, 1.5)), label="somme des répliques", zorder=4)
af.set_xlim(-2.2, 2.2); af.set_ylim(-0.05, 1.15)
af.set_xlabel("$f\\,T_s$"); af.set_ylabel("$G(f)/(g_0 T_s)$"); af.set_title("Version fréquentielle", fontsize=10)
af.legend(loc="upper center", ncol=1, fontsize=8, bbox_to_anchor=(0.5, -0.28))
for ax in (at, af): virgule(ax)
fig.tight_layout()
sauver(fig)
