"""Figure — Constellation QPSK {e^{jπ/4}, …, e^{j7π/4}} bruitée, partiel TS227 2018-2019, q. 19-20.
Figure calculée (complément) : bruit complexe circulaire de variance totale σ² = 2/9, soit 1/9 par voie (σ_v = 1/3) ;
carrés ±3σ_v autour de chaque symbole, 400 échantillons (graine 7). Gauche : v[0] = 1 ; droite : v[0] = √2 (proposition de la q. 20).
Seuils de décision (axes) en pointillés gris."""
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
rng = np.random.default_rng(7)
sv = 1 / 3
pts = np.exp(1j * np.pi / 4 * np.array([1, 3, 5, 7]))
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.3))
for ax, v0, titre in [(axs[0], 1, r"$v[0] = 1$"), (axs[1], np.sqrt(2), r"$v[0] = \sqrt{2}$ (énergie × 2)")]:
    S = rng.choice(pts, 400)
    r = v0 * S + sv * (rng.standard_normal(400) + 1j * rng.standard_normal(400))
    ax.scatter(r.real, r.imag, s=4, color=BLEU, alpha=0.5, lw=0)
    for p in v0 * pts:
        ax.add_patch(plt.Rectangle((p.real - 3 * sv, p.imag - 3 * sv), 6 * sv, 6 * sv, fill=False, ec=ENCRE, lw=0.9))
        ax.plot(p.real, p.imag, "x", color=MAGENTA, ms=8, mew=2)
    ax.axhline(0, color=GRIS, ls=":", lw=1.2); ax.axvline(0, color=GRIS, ls=":", lw=1.2)
    ax.set_aspect("equal"); ax.set_xlim(-2.8, 2.8); ax.set_ylim(-2.8, 2.8)
    ax.set_title(titre, fontsize=10); ax.set_xlabel(r"$\mathrm{Re}(r_l[n])$"); virgule(ax)
axs[0].set_ylabel(r"$\mathrm{Im}(r_l[n])$")
fig.tight_layout()
sauver(fig)
