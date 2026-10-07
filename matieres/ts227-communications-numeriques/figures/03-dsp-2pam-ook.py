"""Figure — DSP d'une 2-PAM et d'une 2-OOK avec une porte de durée Ts (TS227, chapitre 3).
TD [td, p. 2, ex. 2, q. 10-11]. 2-PAM d'après la correction [td-correction, p. 9], redessinée ;
2-OOK reconstruite (complément) : Γ = (Ts/4) sinc²(f Ts) + (1/4) δ(f). Axes normalisés : f·Ts et Γ/Ts.
La flèche de la raie n'est pas à l'échelle (poids 1/4)."""
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
x = np.linspace(-3.5, 3.5, 3001)
fig, axes = plt.subplots(2, 1, figsize=(6.6, 4.2), sharex=True)
axes[0].plot(x, np.sinc(x) ** 2, color=BLEU, label=r"2-PAM $\{-1, 1\}$ : $T_s\,\mathrm{sinc}^2(fT_s)$")
axes[1].plot(x, np.sinc(x) ** 2 / 4, color=MAGENTA, label=r"2-OOK $\{0, 1\}$ : $\frac{T_s}{4}\mathrm{sinc}^2(fT_s) + \frac{1}{4}\delta(f)$")
axes[1].annotate("", xy=(0, 0.9), xytext=(0, 0), arrowprops=dict(arrowstyle="-|>", color=MAGENTA, lw=1.8))
axes[1].text(0.08, 0.8, r"$\frac{1}{4}\,\delta(f)$", color=MAGENTA)
for ax in axes:
    ax.set_ylim(0, 1.15); ax.set_yticks([0, 0.25, 0.5, 1]); virgule(ax, "y")
    ax.set_ylabel(r"$\Gamma_{s_l}(f)/T_s$"); ax.legend(loc="upper right", fontsize=8.5)
axes[1].set_xticks([-3, -2, -1, 0, 1, 2, 3])
axes[1].set_xticklabels(["$-3/T_s$", "$-2/T_s$", "$-1/T_s$", "$0$", "$1/T_s$", "$2/T_s$", "$3/T_s$"])
axes[1].set_xlabel("Fréquence $f$")
sauver(fig)
