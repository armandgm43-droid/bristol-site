"""Figure F3 — Signaux s_a(t) (impulsions) et s_l(t) (mise en forme par une porte) (TS227, chapitre 2).
D'après le support [poly, p. 28], redessinée. Séquence de symboles lue sur la figure du support ;
T_s = 1 ms ; h(t) = porte de hauteur 1 sur [0, T_s[."""
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

a = [1, 3, -3, -1, 1, -1, -1, -3, 1, -1]
Ts = 1.0  # ms
fig, ax = plt.subplots(figsize=(6.6, 2.8))
# s_l(t) : paliers de hauteur a_m sur [m Ts, (m+1) Ts[
t = np.repeat(np.arange(len(a) + 1) * Ts, 2)[1:-1]
y = np.repeat(a, 2)
ax.plot(t, y, color=VERT, lw=1.6, label="$s_l(t)$", zorder=2)
# s_a(t) : impulsions de Dirac de poids a_m (flèches)
for m, am in enumerate(a):
    ax.annotate("", xy=(m * Ts, am), xytext=(m * Ts, 0),
                arrowprops=dict(arrowstyle="-|>", color=BLEU, lw=2, mutation_scale=10), zorder=3)
ax.plot([], [], color=BLEU, lw=2, label="$s_a(t)$")
ax.axhline(0, color="#555555", lw=0.8)
ax.set_xlim(-0.3, 10); ax.set_ylim(-3.6, 3.6)
ax.set_xticks(range(0, 11)); ax.set_yticks([-3, -1, 0, 1, 3]); virgule(ax)
ax.set_xlabel("Temps (ms)"); ax.set_ylabel("Amplitude")
ax.legend(loc="upper right", ncol=2)
sauver(fig)
