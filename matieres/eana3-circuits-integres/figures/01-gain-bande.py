"""Figure — Compromis gain-bande passante : gain de l'amplificateur seul A et du montage bouclé A_F (EANA3, chapitre 1).
D'après les notes externes [tableau-2020-c01, p. 7] et [notes-2023-c01, p. 3], redessinée.
Courbes recalculées pour un amplificateur du premier ordre A(jω) = A0 / (1 + jω/ω0), avec A0 = 10^4 et β_F = 10^-2
(valeurs choisies pour la figure : les notes n'en donnent pas)."""
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
A0, beta = 1e4, 1e-2
w = np.logspace(-1, 6, 800)            # pulsation normalisée ω/ω0
A = A0 / (1 + 1j * w)
AF = A / (1 + A * beta)
dB = lambda x: 20 * np.log10(np.abs(x))
fig, ax = plt.subplots(figsize=(6.2, 3.4))
ax.semilogx(w, dB(A), color=ENCRE, label="amplificateur seul $A$")
ax.semilogx(w, dB(AF), color=BLEU, label="montage bouclé $A_F$")
ax.axhline(dB(1 / beta), color=ORANGE, ls="--", lw=1.2, label=r"$20\log(1/\beta_F)$")
wc = 1 + A0 * beta
for x, lab in [(1, r"$\omega_0$"), (wc, r"$(1 + A_0\beta_F)\,\omega_0$")]:
    ax.axvline(x, color=GRIS, ls=":", lw=1)
    ax.text(x * 1.12, 3, lab, color=ENCRE, fontsize=9)
ax.annotate("", xy=(wc, -12), xytext=(1, -12), arrowprops=dict(arrowstyle="<->", color=VERT, lw=1.2))
ax.text(np.sqrt(wc), -21, r"bande passante $\times(1 + A_0\beta_F)$", color=VERT, ha="center", fontsize=9)
ax.annotate("", xy=(0.3, dB(1 / beta) + 1), xytext=(0.3, dB(A0) - 1), arrowprops=dict(arrowstyle="->", color=VERT, lw=1.2))
ax.text(0.36, 60, r"gain $\div(1 + A_0\beta_F)$", color=VERT, fontsize=9)
ax.set_xlim(0.1, 1e6); ax.set_ylim(-25, 90)
ax.set_xlabel(r"pulsation normalisée $\omega/\omega_0$"); ax.set_ylabel("gain (dB)")
ax.legend(loc="upper right", fontsize=9)
virgule(ax, "y")
sauver(fig)
