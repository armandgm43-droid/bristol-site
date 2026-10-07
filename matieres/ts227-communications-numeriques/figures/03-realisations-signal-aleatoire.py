"""Figure — Deux réalisations du signal aléatoire s_l(t) (TS227, chapitre 3).
D'après les notes de cours [notes, f. 4 v°], redessinée. Symboles ±1, h(t) porte d'amplitude 1 sur [0, Ts].
Les suites de symboles sont tirées au hasard (graine fixée) : les notes n'en donnent qu'un croquis."""
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
rng = np.random.default_rng(3)
N = 8
t0 = 3.4   # instant d'observation (en Ts)
fig, axes = plt.subplots(2, 1, figsize=(6.6, 3.6), sharex=True)
for ax, nom, coul in zip(axes, (r"$\omega_0$", r"$\omega_1$"), (BLEU, MAGENTA)):
    a = rng.choice([-1, 1], size=N)
    ax.step(np.arange(N + 1), np.append(a, a[-1]), where="post", color=coul)
    v = a[int(t0)]
    ax.axvline(t0, color=VERT, lw=1.2)
    ax.plot([t0], [v], "o", color=VERT, ms=5)
    ax.text(t0 + 0.08, v * 0.55, f"$s_l(t) = {v:+d}$".replace("+", "+"), color=VERT, fontsize=9)
    ax.set_ylim(-1.5, 1.5); ax.set_yticks([-1, 0, 1]); virgule(ax, "y")
    ax.set_ylabel(f"$s_l(t)$, {nom}")
axes[1].set_xticks(range(N + 1)); axes[1].set_xticklabels(["$0$"] + [f"${k}T_s$" if k > 1 else "$T_s$" for k in range(1, N + 1)])
axes[1].set_xlabel("Temps $t$")
axes[0].text(t0, 1.62, "$t$", color=VERT, ha="center", fontsize=10)
sauver(fig)
