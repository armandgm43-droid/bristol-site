"""Figure — Théorie de Hajimiri : réponse d'un oscillateur LC à une impulsion de courant injectée au maximum ou au
passage par zéro de v_s(t), et fonctions de sensibilité impulsionnelle Γ(ω0τ) de l'oscillateur LC et de l'anneau (EANA3, chapitre 4).
D'après les notes externes [notes-2023-c09, p. 3-4], redessinée. Courbes calculées : v_s = sin(ω0 t), saut de tension de
0,15 (unité arbitraire) ; Γ_LC = cos(ω0 τ) ; anneau : sortie trapézoïdale idéalisée et Γ triangulaire sur les fronts."""
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

w = np.linspace(0, 4 * np.pi, 2000)          # ω0 t
D = 0.15
ref = np.sin(w)
# impulsion au maximum (ω0 t = π/2) : amplitude modifiée, phase inchangée
t1 = np.pi / 2
bleu = np.where(w < t1, ref, (1 + D) * np.sin(w))
# impulsion au passage par zéro (ω0 t = π) : v saute de D, la pente reste −1 → A sin(ω0 t + φ)
t2 = np.pi
phi = -np.arctan(D); A = np.hypot(1, D)
rouge = np.where(w < t2, ref, A * np.sin(w + phi))

fig, axs = plt.subplots(4, 1, figsize=(6.4, 7.4), sharex=True,
                        gridspec_kw={"height_ratios": [2.2, 1.2, 1.4, 1.2], "hspace": 0.28})
ax = axs[0]
ax.plot(w, ref, color=ENCRE, lw=1.2, label="sans perturbation")
ax.plot(w, bleu, color=BLEU, label="impulsion au maximum")
ax.plot(w, rouge, color=MAGENTA, label="impulsion au passage par zéro")
for x, c in [(t1, BLEU), (t2, MAGENTA)]:
    ax.annotate("", xy=(x, 1.25 if x == t1 else 0.35), xytext=(x, 1.75 if x == t1 else 0.85),
                arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.4))
ax.set_ylabel(r"$v_s(t)$ (LC)"); ax.set_ylim(-1.4, 1.9); ax.set_yticks([])
ax.legend(loc="upper right", fontsize=8, ncol=3, bbox_to_anchor=(1, 1.22))
ax.text(3 * np.pi - 0.1, -1.3, "décalage de phase permanent", color=MAGENTA, ha="center", fontsize=8)

ax = axs[1]
ax.plot(w, np.cos(w), color=ORANGE)
ax.axhline(0, color=GRIS, lw=0.6)
ax.set_ylabel(r"$\Gamma(\omega_0\tau)$ LC"); ax.set_yticks([])

# anneau : trapèze (fronts sur [0, a] et [π, π + a]) et Γ triangulaire sur les fronts
a = 0.6 * np.pi
ph = np.mod(w, 2 * np.pi)
trap = np.where(ph < a, ph / a, np.where(ph < np.pi, 1, np.where(ph < np.pi + a, 1 - (ph - np.pi) / a, 0)))
tri = np.where(ph < a, 1 - np.abs(2 * ph / a - 1), 0) - np.where((ph >= np.pi) & (ph < np.pi + a), 1 - np.abs(2 * (ph - np.pi) / a - 1), 0)
axs[2].plot(w, trap, color=BLEU); axs[2].set_ylabel("sortie\n(anneau)"); axs[2].set_yticks([])
axs[3].fill_between(w, tri, color=ORANGE, alpha=0.25, lw=0); axs[3].plot(w, tri, color=ORANGE)
axs[3].axhline(0, color=GRIS, lw=0.6)
axs[3].set_ylabel(r"$\Gamma(\omega_0\tau)$" + "\nanneau"); axs[3].set_yticks([])
axs[3].set_xticks([0, np.pi, 2 * np.pi, 3 * np.pi, 4 * np.pi], ["0", "π", "2π", "3π", "4π"])
axs[3].set_xlabel(r"$\omega_0 t$ (ou $\omega_0\tau$)")
for ax in axs:
    ax.grid(False)
    for x in (t1, t2):
        ax.axvline(x, color=GRIS, ls=":", lw=0.7)
sauver(fig)
