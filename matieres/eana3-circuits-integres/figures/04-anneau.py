"""Figure — Oscillateur en anneau à trois inverseurs : tensions de sortie des trois étages, chacune retardée de Δt
(temps de propagation d'un inverseur) et inversée par rapport à la précédente ; période T = 6 Δt (EANA3, chapitre 4).
D'après les notes externes [notes-2023-c07, p. 2] et le corrigé externe [corr-2023-td05-anneau, p. 1], redessinée.
Fronts idéalisés (rampes courtes) ; Δt = 1 (unité arbitraire)."""
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

DT, TR = 1.0, 0.12             # temps de propagation, durée d'un front (figure)
t = np.linspace(0, 13, 4000)

def creneau(t, retard):
    """Créneau de période 6Δt, haut sur [0, 3Δt[, décalé de `retard`, avec fronts de durée TR."""
    phase = np.mod(t - retard, 6 * DT)
    v = np.where(phase < 3 * DT, 1.0, 0.0)
    v = np.where(phase < TR, phase / TR, v)                                  # front montant
    v = np.where((phase >= 3 * DT) & (phase < 3 * DT + TR), 1 - (phase - 3 * DT) / TR, v)  # front descendant
    return v

# V1 haut sur [0,3Δt[ ; V2 = non V1 retardé de Δt ; V3 = non V2 retardé de Δt = V1 retardé de 2Δt
signaux = [(r"$V_1$", creneau(t, 0.0), BLEU), (r"$V_2$", creneau(t, 3 * DT + DT), VERT), (r"$V_3$", creneau(t, 2 * DT), MAGENTA)]

fig, ax = plt.subplots(figsize=(6.4, 3.4))
for k, (nom, v, c) in enumerate(signaux):
    y0 = (2 - k) * 1.6
    ax.plot(t, y0 + v, color=c)
    ax.text(-0.25, y0 + 0.5, nom, color=c, ha="right", va="center")
# retards entre étages (premier front montant de V1 → front descendant de V2 → front montant de V3)
for x in (0, DT, 2 * DT, 6 * DT):
    ax.plot([x, x], [-0.2, 4.4], color=GRIS, lw=0.6, ls=":")
for a, b, y in [(0, DT, 4.25), (DT, 2 * DT, 2.65)]:
    ax.annotate("", xy=(a, y), xytext=(b, y), arrowprops=dict(arrowstyle="<->", lw=0.9, color=ENCRE))
    ax.text((a + b) / 2, y + 0.07, r"$\Delta t$", ha="center", va="bottom")
ax.annotate("", xy=(0, -0.45), xytext=(6 * DT, -0.45), arrowprops=dict(arrowstyle="<->", lw=0.9, color=ENCRE))
ax.text(3 * DT, -0.55, r"$T = 6\,\Delta t$ (3 Δt haut + 3 Δt bas)", ha="center", va="top")
ax.set_xlim(-0.2, 13); ax.set_ylim(-1.2, 4.6)
ax.set_yticks([]); ax.set_xticks([]); ax.grid(False)
ax.spines["left"].set_visible(False)
ax.set_xlabel("temps")
sauver(fig)
