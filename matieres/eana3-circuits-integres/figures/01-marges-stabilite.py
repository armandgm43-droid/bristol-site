"""Figure — Stabilité : lecture de la marge de phase sur le diagramme de Bode de A, avec 20 log(1/β_F) comme « nouvel axe 0 dB » (EANA3, chapitre 1).
D'après les notes externes [tableau-2020-c02, p. 2-3] et [notes-2023-c01, p. 4-5], redessinée.
Courbes recalculées pour A(jω) = A0 / ((1 + jω/ω1)(1 + jω/ω2)), A0 = 10^4, ω2 = 100 ω1, et deux valeurs de β_F
(10^-1 et 10^-3) choisies pour la figure : les notes n'en donnent pas."""
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
A0, w2 = 1e4, 100.0
w = np.logspace(-1, 4, 2000)           # pulsation normalisée ω/ω1
A = A0 / ((1 + 1j * w) * (1 + 1j * w / w2))
gain = 20 * np.log10(np.abs(A))
phase = np.degrees(np.unwrap(np.angle(A)))
cas = [(1e-1, MAGENTA, r"\beta_F = 0{,}1"), (1e-3, VERT, r"\beta_F = 0{,}001")]

fig, (ag, ap) = plt.subplots(2, 1, figsize=(6.2, 5.2), sharex=True, gridspec_kw={"height_ratios": [1.15, 1]})
ag.semilogx(w, gain, color=ENCRE, label="$A$")
ap.semilogx(w, phase, color=ENCRE)
for beta, coul, lab in cas:
    niveau = 20 * np.log10(1 / beta)
    wc = np.interp(-niveau, -gain, w)          # gain décroissant : croisement |A| = 1/β_F
    phi = np.interp(wc, w, phase)
    mphi = 180 + phi
    ag.axhline(niveau, color=coul, ls="--", lw=1.2, label=rf"$20\log(1/\beta_F)$, ${lab}$")
    ag.plot(wc, niveau, "o", color=coul, ms=5)
    ag.axvline(wc, color=coul, ls=":", lw=1); ap.axvline(wc, color=coul, ls=":", lw=1)
    ap.annotate("", xy=(wc, -180), xytext=(wc, phi), arrowprops=dict(arrowstyle="<->", color=coul, lw=1.3))
    ytxt = (phi - 180) / 2 if mphi > 40 else -150
    ap.text(wc * 1.15, ytxt, f"$M_\\varphi \\approx {mphi:.0f}°$", color=coul, fontsize=9, va="center")
for x, lab in [(1, r"$\omega_1$"), (w2, r"$\omega_2$")]:
    ag.text(x, -32, lab, ha="center", fontsize=9)
ag.set_ylim(-25, 90); ag.set_ylabel("gain (dB)")
ag.legend(loc="upper right", fontsize=8.5)
ap.axhline(-180, color=GRIS, lw=1)
ap.set_ylim(-190, 5); ap.set_yticks([0, -45, -90, -135, -180])
ap.set_ylabel("phase (°)"); ap.set_xlabel(r"pulsation normalisée $\omega/\omega_1$")
ap.set_xlim(0.1, 1e4)
virgule(ag, "y"); virgule(ap, "y")
fig.tight_layout()
sauver(fig)
