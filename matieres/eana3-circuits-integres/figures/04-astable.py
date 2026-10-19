"""Figure — Astable à charge et décharge d'une capacité à courant constant : tension V_C(t) triangulaire entre les seuils
V_b et V_h du comparateur à hystérésis, et état de l'interrupteur (EANA3, chapitre 4).
D'après les notes externes [notes-2023-c07, p. 1], redessinée. Valeurs choisies pour la figure (unités arbitraires) :
V_b = 1, V_h = 3, I/C = 1. Le chronogramme de l'interrupteur (en gris) est ajouté par Bristol."""
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

VB, VH, PENTE = 1.0, 3.0, 1.0
DT = (VH - VB) / PENTE          # durée d'une rampe entre les deux seuils
T0 = VH / PENTE                 # première charge depuis 0

# points du signal triangulaire
t_pts, v_pts = [0.0, T0], [0.0, VH]
t, monte = T0, False
while t < T0 + 4 * DT - 1e-9:
    t += DT
    t_pts.append(t); v_pts.append(VH if monte else VB)
    monte = not monte

fig, (ax, ax2) = plt.subplots(2, 1, figsize=(6.4, 3.9), sharex=True,
                              gridspec_kw={"height_ratios": [3, 1], "hspace": 0.12})
ax.plot(t_pts, v_pts, color=BLEU)
for niveau, nom, coul in [(VH, r"$V_h$", ORANGE), (VB, r"$V_b$", VERT)]:
    ax.axhline(niveau, color=coul, lw=1, ls="--")
    ax.text(-0.15, niveau, nom, color=coul, ha="right", va="center")
# cotes Δt
for k, (a, b) in enumerate([(T0, T0 + DT), (T0 + DT, T0 + 2 * DT)]):
    ax.annotate("", xy=(a, 3.45), xytext=(b, 3.45), arrowprops=dict(arrowstyle="<->", color=ENCRE, lw=0.9))
    ax.text((a + b) / 2, 3.55, r"$\Delta t$", ha="center", va="bottom")
    for x in (a, b):
        ax.plot([x, x], [0, 3.45], color=GRIS, lw=0.6, ls=":")
ax.annotate("", xy=(T0 + 2 * DT, 3.95), xytext=(T0, 3.95), arrowprops=dict(arrowstyle="<->", color=MAGENTA, lw=0.9))
ax.text(T0 + DT, 4.05, r"$T = 2\,\Delta t$", ha="center", va="bottom", color=MAGENTA)
ax.text(0.1, 2.3, r"pente $+\dfrac{I}{C}$", color=ORANGE, ha="left")
ax.text(T0 + 0.5 * DT + 0.35, 2.3, r"pente $-\dfrac{I}{C}$", color=VERT, ha="left")
ax.set_ylim(0, 4.5); ax.set_ylabel(r"$V_C(t)$")
ax.set_yticks([]); ax.grid(False)

# état de l'interrupteur (ajout Bristol)
etat_t = [0, T0]; etat = [1, 1]
t, ch = T0, 0
while t < T0 + 4 * DT - 1e-9:
    etat_t += [t, t + DT]; etat += [ch, ch]; t += DT; ch = 1 - ch
ax2.plot(etat_t, etat, color=GRIS, lw=1.4)
ax2.set_yticks([0, 1], ["décharge", "charge"]); ax2.set_ylim(-0.3, 1.3); ax2.grid(False)
ax2.set_xlabel("temps"); ax2.set_xticks([])
ax2.set_xlim(0, T0 + 4 * DT)
sauver(fig)
