"""Figure — DSP de l'OOK {0, 1} avec le filtre g_α du partiel 2015-2016 (TS227, annale), α = 1 et α = 1/2.
Figure calculée (complément) : Γ = |G_α|²/(4Ts) + (1/(4Ts²)) Σ_k |G_α(k/Ts)|² δ(f − k/Ts).
Axes normalisés : f·Ts et Γ/Ts ; chaque raie est une flèche dont la hauteur est son poids (hors échelle de la partie continue)."""
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
f = np.linspace(-4, 4, 4001)
cont1 = np.sinc(f) ** 2 / 4
cont2 = np.sinc(f / 2) ** 2 * np.sin(np.pi * f / 2) ** 2 / 4
fig, axs = plt.subplots(2, 1, figsize=(6.4, 4.6), sharex=True)
for ax, c, raies, titre in [
        (axs[0], cont1, {0: 0.25}, r"$\alpha = 1$ : $\Gamma = \frac{T_s}{4}\,\mathrm{sinc}^2(fT_s) + \frac{1}{4}\delta(f)$"),
        (axs[1], cont2, {k: 1 / (np.pi * k) ** 2 for k in (-3, -1, 1, 3)},
         r"$\alpha = 1/2$ : $\Gamma = \frac{T_s}{4}\,\mathrm{sinc}^2(\frac{fT_s}{2})\sin^2(\frac{\pi fT_s}{2}) + \sum_{k\ \mathrm{impair}} \frac{\delta(f - k/T_s)}{\pi^2k^2}$")]:
    ax.plot(f, c, color=BLEU, label="partie continue  $\\Gamma\\,/\\,T_s$")
    for k, p in raies.items():
        ax.annotate("", xy=(k, p), xytext=(k, 0), arrowprops=dict(arrowstyle="-|>", color=MAGENTA, lw=1.6))
    ax.plot([], [], color=MAGENTA, label="raie (hauteur = poids)")
    ax.set_title(titre, fontsize=10, loc="left")
    ax.set_ylim(0, 0.3); ax.set_ylabel(r"$\Gamma_{s_l}^{\alpha}(f)\,/\,T_s$")
    ax.legend(loc="upper right", fontsize=8); virgule(ax)
axs[1].axvspan(0, 2, color=GRIS, alpha=0.12, lw=0)
axs[0].axvspan(0, 1, color=GRIS, alpha=0.12, lw=0)
axs[1].set_xlabel(r"$f\,T_s$"); axs[1].set_xticks(range(-4, 5))
fig.tight_layout()
sauver(fig)
