"""Figure — Tension de sortie d'une référence bandgap en fonction de la température : coefficient nul (TC0) à 300 K,
TC+ dominant en dessous, TC− dominant au-dessus (EANA3, chapitre 5).
D'après les notes externes [notes-2023-c10, p. 3], redessinée. Courbe calculée avec le modèle usuel
V_BE(T) = V_G0 (1 − T/T0) + V_BE0 T/T0 − (γ − α) U_T ln(T/T0), V_G0 = 1,205 V, V_BE0 = 0,65 V, γ − α = 3, T0 = 300 K,
et V_ref = V_BE + K T avec K choisi pour annuler la dérivée à 300 K : valeurs choisies pour la figure."""
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

K_B, Q = 1.380649e-23, 1.602176634e-19
VG0, VBE0, ETA, T0 = 1.205, 0.65, 3.0, 300.0
T = np.linspace(220, 400, 400)
UT = K_B * T / Q
vbe = VG0 * (1 - T / T0) + VBE0 * T / T0 - ETA * UT * np.log(T / T0)
# dVBE/dT à T0 = (VBE0 - VG0)/T0 - ETA k/q ; on compense par K
K = -((VBE0 - VG0) / T0 - ETA * K_B / Q)
vref = vbe + K * T

fig, ax = plt.subplots(figsize=(6.0, 3.3))
ax.plot(T, vref * 1e3, color=BLEU)
ax.axvline(T0, color=GRIS, ls=":", lw=0.9)
v0 = np.interp(T0, T, vref) * 1e3
ax.annotate("TC0", xy=(T0, v0), xytext=(T0, v0 + 1.2), ha="center", color=MAGENTA,
            arrowprops=dict(arrowstyle="-", color=MAGENTA, lw=0.8))
ax.text(232, v0 - 6.5, "TC+ dominant", color=ENCRE)
ax.text(352, v0 - 6.5, "TC− dominant", color=ENCRE)
ax.set_xlabel("température (K)"); ax.set_ylabel(r"$V_{ref}$ (mV)")
ax.set_ylim(v0 - 9, v0 + 3)
virgule(ax)
sauver(fig)
