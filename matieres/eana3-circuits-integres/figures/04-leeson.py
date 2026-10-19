"""Figure — Allure du bruit de phase ℒ(Δω) selon Leeson : pente −30 dB/décade (bruit en 1/f converti), puis
−20 dB/décade (bruit de proximité, close-in), puis plancher de bruit blanc au-delà de ω0/(2Q) (EANA3, chapitre 4).
D'après les notes externes [notes-2023-c09, p. 2], redessinée. Courbe tracée avec la forme de Leeson
ℒ = plancher × (1 + (ω0/(2QΔω))²)(1 + ω_c/Δω), écart Δω normalisé par ω0/(2Q), ω_c = 0,03 ω0/(2Q) :
valeurs choisies pour la figure (les notes n'en donnent pas). Le coin ω_c et la forme exacte sont des ajouts Bristol (gris)."""
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

WC = 0.03                                   # coin du bruit en 1/f (normalisé)
x = np.logspace(-3.3, 2, 600)               # Δω / (ω0 / 2Q)
L = 10 * np.log10((1 + 1 / x**2) * (1 + WC / x))   # dB au-dessus du plancher

fig, ax = plt.subplots(figsize=(6.4, 3.6))
ax.semilogx(x, L, color=BLEU)
# asymptotes
xa = np.logspace(-3.3, np.log10(WC), 50); ax.semilogx(xa, 10 * np.log10(WC / xa**3), color=GRIS, ls="--", lw=1)
xb = np.logspace(np.log10(WC), 0, 50);    ax.semilogx(xb, -20 * np.log10(xb), color=GRIS, ls="--", lw=1)
ax.axhline(0, color=GRIS, ls="--", lw=1)
for xc in (WC, 1):
    ax.axvline(xc, color=GRIS, ls=":", lw=0.8)
ax.text(2e-3, 82, "−30 dB/décade", color=ENCRE, ha="left")
ax.text(0.12, 30, "−20 dB/décade\n(bruit de proximité,\nclose-in)", color=ENCRE, ha="left")
ax.text(4, 4, "plancher\n(bruit blanc)", ha="left", va="bottom")
ax.text(1.12, 100, r"$\dfrac{\omega_0}{2Q}$", ha="left", va="top")
ax.text(WC * 1.12, 100, r"$\omega_c$", ha="left", va="top", color=GRIS)
ax.set_xlabel(r"écart à la porteuse $\Delta\omega$ (échelle logarithmique)")
ax.set_ylabel(r"$\mathcal{L}(\Delta\omega)$ au-dessus du plancher (dB)")
ax.set_xticks([]); ax.minorticks_off()
ax.set_ylim(-14, 110)
virgule(ax, "y")
sauver(fig)
