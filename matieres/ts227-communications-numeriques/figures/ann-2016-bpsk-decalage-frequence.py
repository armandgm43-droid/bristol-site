"""Figure — Constellation des échantillons r_l[n] d'une BPSK reçue avec un décalage de fréquence Δf0 (partiel TS227 2016-2017, q. 3).
Figure calculée (complément), sans bruit : r_l[n] = S_n exp(−j 2π Δf0 n Ts), n = 0 … 99, symboles aléatoires (graine 1).
Gauche : Ts Δf0 = 1/400 ; droite : Ts Δf0 = 1/1200. Seuil de décision (axe imaginaire) en pointillés gris."""
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
rng = np.random.default_rng(1)
S = rng.choice([-1, 1], 100)
n = np.arange(100)
fig, axs = plt.subplots(1, 2, figsize=(6.4, 3.3))
for ax, r, titre in [(axs[0], 1 / 400, r"$T_s\Delta f_0 = 1/400$" + "\n(rotation totale 90°)"),
                     (axs[1], 1 / 1200, r"$T_s\Delta f_0 = 1/1200$" + "\n(rotation totale 30°)")]:
    z = S * np.exp(-2j * np.pi * r * n)
    th = np.linspace(0, 2 * np.pi, 400)
    ax.plot(np.cos(th), np.sin(th), color="#DADADA", lw=0.8)
    sc = ax.scatter(z.real, z.imag, c=n, cmap="viridis", s=14, zorder=3)
    ax.plot([-1, 1], [0, 0], "x", color=MAGENTA, ms=9, mew=2, zorder=4)
    ax.axvline(0, color=GRIS, ls=":", lw=1.2)
    ax.set_aspect("equal"); ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3)
    ax.set_title(titre, fontsize=9); ax.set_xlabel(r"$\mathrm{Re}(r_l[n])$"); virgule(ax)
axs[0].set_ylabel(r"$\mathrm{Im}(r_l[n])$")
cb = fig.colorbar(sc, ax=axs, shrink=0.8, label="indice $n$ du symbole")
sauver(fig)
