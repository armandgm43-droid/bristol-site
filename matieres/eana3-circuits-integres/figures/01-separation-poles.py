"""Figure — Séparation des pôles : position des deux pôles de v_out/i_e en fonction de la capacité C entre grille et drain (EANA3, chapitre 1).
Reconstruite (aucune source ne trace ces courbes) : pôles calculés à partir du dénominateur établi dans les notes externes
[notes-2023-c02, p. 3] et [tableau-2020-c03, p. 2] ; allure à comparer au croquis [notes-2023-c02, p. 4] et [tableau-2020-c03, p. 4].
Valeurs choisies pour la figure : g_m = 10 mS (ordre de grandeur des notes), R_e = R_S = 10 kΩ, C_e = C_S = 10 fF."""
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
gm, Re, Rs, Ce, Cs = 10e-3, 10e3, 10e3, 10e-15, 10e-15
C = np.logspace(-15, -11, 400)
b1 = (Cs + C) * Rs + (Ce + C) * Re + gm * Re * Rs * C
b2 = (Cs * Ce + C * Ce + C * Cs) * Re * Rs
# D(p) = 1 + b1 p + b2 p^2 = (1 + p/p1)(1 + p/p2) : p1, p2 > 0 (pôles réels négatifs -p1, -p2)
disc = np.sqrt(b1**2 - 4 * b2)
p1 = 2 / (b1 + disc)
p2 = (b1 + disc) / (2 * b2)
Cf = C * 1e15  # en fF
fig, ax = plt.subplots(figsize=(6.2, 3.8))
ax.loglog(Cf, p1, color=BLEU, label="$p_1$ (calcul exact)")
ax.loglog(Cf, p2, color=MAGENTA, label="$p_2$ (calcul exact)")
ax.loglog(Cf, 1 / (gm * Re * Rs * C), color=BLEU, ls="--", lw=1.1, label=r"$p_1 \approx 1/(g_m R_e R_S C)$")
ax.axhline(gm / (Ce + Cs), color=MAGENTA, ls="--", lw=1.1, label=r"$p_2 \approx g_m/(C_e + C_S)$")
ax.loglog(Cf, 1 / (Rs * (C + Cs)), color=GRIS, ls=":", lw=1.6, label=r"$p_2$ « méthode de l'enseirbien » $1/(R_S(C + C_S))$")
ax.set_xlabel("capacité $C$ (fF)"); ax.set_ylabel("pôle (rad/s)")
ax.set_xlim(1, 1e4); ax.set_ylim(1e4, 1e13)
ax.legend(loc="center left", bbox_to_anchor=(1.01, 0.5), fontsize=8.5)
ax.grid(True, which="major", color="#DADADA", lw=0.6)
sauver(fig)
