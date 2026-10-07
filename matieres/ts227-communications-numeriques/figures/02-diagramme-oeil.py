"""Figure F14 — Construction et lecture du diagramme de l'œil (TS227, chapitre 2).
D'après le support [poly, p. 56 et 60] et les notes [notes, f. 2 v°], reconstruite par simulation.
Paramètres choisis (non donnés par le support) : symboles binaires ±1 équiprobables, Ts = 1 ms,
filtre global en cosinus surélevé de facteur de retombée 0,5, tronqué à ±8 Ts ; graine aléatoire fixée."""
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

def cosinus_sureleve_temps(u, beta):
    u = np.asarray(u, dtype=float)
    den = 1 - (2 * beta * u) ** 2
    sing = np.isclose(den, 0)
    val = np.sinc(u) * np.cos(np.pi * beta * u) / np.where(sing, 1, den)
    return np.where(sing, np.pi / 4 * np.sinc(1 / (2 * beta)), val)

rng = np.random.default_rng(227)
beta, N, L, ech = 0.5, 160, 8, 100          # ech : points par symbole
a = rng.choice([-1.0, 1.0], size=N)
t = np.arange(N * ech) / ech                  # en unités de Ts (= ms)
r = np.zeros_like(t)
for m, am in enumerate(a):
    i0, i1 = max(0, (m - L) * ech), min(len(t), (m + L) * ech)
    r[i0:i1] += am * cosinus_sureleve_temps(t[i0:i1] - m, beta)

fig = plt.figure(figsize=(7.0, 5.6))
haut = fig.add_axes([0.08, 0.71, 0.9, 0.25]); bas = fig.add_axes([0.08, 0.07, 0.56, 0.48])
# (a) signal reçu, 30 symboles, instants d'échantillonnage
d0 = 20                                       # on montre les symboles d0 à d0+30 (régime établi)
sel = (t >= d0) & (t <= d0 + 30)
haut.plot(t[sel] - d0, r[sel], color=BLEU, lw=1.3)
haut.plot(np.arange(31), a[d0:d0 + 31], "o", ms=3.5, color=ENCRE)
haut.set_xlim(0, 30); haut.set_ylim(-2, 2); haut.set_xticks(range(0, 31, 5))
haut.set_xlabel("Temps (ms)"); haut.set_ylabel("Amplitude"); haut.set_title("(a) Signal reçu $r_l(t)$", fontsize=10)
# (b) superposition des tranches de durée 2 Ts centrées sur les instants d'échantillonnage
u = np.arange(-ech, ech + 1) / ech
for k in range(L + 1, N - L - 1):
    bas.plot(u, r[k * ech - ech:k * ech + ech + 1], color=BLEU, lw=0.5, alpha=0.35)
for tc in (-1, 0, 1):
    for niv in (-1, 1):
        bas.plot([tc], [niv], "o", ms=11, mfc="none", mec=MAGENTA, mew=1.6, zorder=4)
# ouvertures de l'œil (au centre, entre deux instants d'échantillonnage)
bas.annotate("", xy=(0, 0.93), xytext=(0, -0.93), arrowprops=dict(arrowstyle="<->", color=ENCRE, lw=1.2))
bas.annotate("", xy=(-0.42, 0), xytext=(0.42, 0), arrowprops=dict(arrowstyle="<->", color=ENCRE, lw=1.2))
bas.set_xlim(-1, 1); bas.set_ylim(-2, 2)
bas.set_xlabel("Temps (ms)"); bas.set_ylabel("Amplitude"); bas.set_title("(b) Diagramme de l'œil", fontsize=10)
fig.text(0.68, 0.45, "Points de croisement uniques\n(cercles) : absence d'IES", fontsize=9, va="top")
fig.text(0.68, 0.33, "Ouverture verticale (flèche ↕) :\nrobustesse au bruit", fontsize=9, va="top")
fig.text(0.68, 0.21, "Ouverture horizontale (flèche ↔) :\nrobustesse aux déphasages\nde l'échantillonneur", fontsize=9, va="top")
for ax in (haut, bas): virgule(ax)
sauver(fig)
