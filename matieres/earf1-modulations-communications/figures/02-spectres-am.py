"""EARF1 ch. 2 — Spectres d'amplitude (f > 0) des trois modulations d'amplitude, modulant quelconque.
D'après le support [mod-ana, p. 22, 28 et 30], redessinée (échelles normalisées)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
VERT, ROUGE, BLEU = "#2E7D32", "#B23A3A", "#2B4C9B"
fp, Bm, e = 6.0, 1.6, 0.15
f = np.linspace(0, 9, 3001)
def bande(g):  # spectre du modulant entre e et Bm (pas de composante continue)
    return np.clip(np.minimum((g - e) / 0.35, (Bm - g) / 0.35), 0, 1)
fig, ax = plt.subplots(1, 4, figsize=(10, 2.6))
ax[0].fill_between(f, bande(f), color=VERT, alpha=0.85); ax[0].set_title("Modulant $|M(f)|$", fontsize=9)
ax[0].set_xticks([Bm]); ax[0].set_xticklabels(["$B_m$"])
bli, bls = bande(fp - f) * (f < fp), bande(f - fp) * (f > fp)
ax[1].fill_between(f, 0.5 * (bli + bls), color=ROUGE, alpha=0.85); ax[1].set_title("AMDBSP", fontsize=9)
ax[2].fill_between(f, 0.5 * (bli + bls), color=ROUGE, alpha=0.85); ax[2].vlines(fp, 0, 1, color=BLEU, lw=2)
ax[2].set_title("AMDBAP (porteuse)", fontsize=9)
ax[2].text(fp - 1.0, 0.62, "BLI", fontsize=8, ha="center"); ax[2].text(fp + 1.0, 0.62, "BLS", fontsize=8, ha="center")
ax[3].fill_between(f, 0.5 * bls, color=ROUGE, alpha=0.85); ax[3].set_title("AM BLU (ici BLS)", fontsize=9)
for a in ax[1:]:
    a.set_xticks([fp - Bm, fp, fp + Bm]); a.set_xticklabels(["$f_p-B_m$", "$f_p$", "$f_p+B_m$"], fontsize=7.5)
for a in ax:
    a.set_xlim(0, 9); a.set_ylim(0, 1.15); a.set_yticks([]); a.set_xlabel("$f$", labelpad=0)
    a.spines[["top", "right"]].set_visible(False)
ax[1].annotate("", (fp + Bm, 0.8), (fp - Bm, 0.8), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax[1].text(fp, 0.86, "$2B_m$", ha="center", fontsize=8)
ax[3].annotate("", (fp + Bm, 0.8), (fp, 0.8), arrowprops=dict(arrowstyle="<->", lw=0.8))
ax[3].text(fp + Bm / 2, 0.86, "$B_m$", ha="center", fontsize=8)
fig.tight_layout(); fig.savefig("02-spectres-am.svg")
