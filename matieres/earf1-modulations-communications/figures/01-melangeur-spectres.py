"""EARF1 ch. 1 — Décalage en fréquence par un mélangeur : spectres d'amplitude.
D'après le support [mod-ana, p. 17-18], redessinée (échelles normalisées)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, VERT, ROUGE = "#2B4C9B", "#2E7D32", "#B23A3A"

fig, ax = plt.subplots(2, 3, figsize=(9, 4.6))
fm, fp, Bm = 1.6, 6.0, 1.6
# Ligne 1 : modulant sinusoïdal
a = ax[0, 0]; a.vlines(fm, 0, 1, color=VERT, lw=2); a.set_title("Modulant $A\\cos(2\\pi f_m t)$", fontsize=9)
a.set_xticks([fm]); a.set_xticklabels(["$f_m$"]); a.set_yticks([1]); a.set_yticklabels(["$A$"])
a = ax[0, 1]; a.vlines(fp, 0, 1, color=BLEU, lw=2); a.set_title("Porteuse $\\cos(2\\pi f_p t)$", fontsize=9)
a.set_xticks([fp]); a.set_xticklabels(["$f_p$"]); a.set_yticks([1]); a.set_yticklabels(["1"])
a = ax[0, 2]; a.vlines([fp - fm, fp + fm], 0, 0.5, color=ROUGE, lw=2)
a.vlines(fp, 0, 0.5, color="#7E889B", lw=1, ls=":")
a.set_title("Signal modulé $s(t) = m(t)\\,p(t)$", fontsize=9)
a.set_xticks([fp - fm, fp, fp + fm]); a.set_xticklabels(["$f_p - f_m$", "$f_p$", "$f_p + f_m$"])
a.set_yticks([0.5]); a.set_yticklabels(["$A/2$"])
# Ligne 2 : modulant quelconque (spectre trapézoïdal)
f = np.linspace(0, 8, 1601)
trap = lambda g: np.clip(np.minimum((g + 0.05) / 0.4, (Bm - g) / 0.4), 0, 1) * (g >= 0)
a = ax[1, 0]; a.fill_between(f, trap(f), color=VERT, alpha=0.8); a.set_title("Modulant quelconque $|M(f)|$", fontsize=9)
a.set_xticks([Bm]); a.set_xticklabels(["$B_m$"]); a.set_yticks([])
a = ax[1, 1]; a.vlines(fp, 0, 1, color=BLEU, lw=2); a.set_title("Porteuse $A_p\\cos(2\\pi f_p t)$", fontsize=9)
a.set_xticks([fp]); a.set_xticklabels(["$f_p$"]); a.set_yticks([1]); a.set_yticklabels(["$A_p$"])
a = ax[1, 2]
g = np.abs(f - fp)
a.fill_between(f, 0.5 * trap(g), color=ROUGE, alpha=0.8)
a.set_title("$|S(f)| = \\frac{A_p}{2}|M(f - f_p)|$ pour $f > 0$", fontsize=9)
a.set_xticks([fp - Bm, fp, fp + Bm]); a.set_xticklabels(["$f_p - B_m$", "$f_p$", "$f_p + B_m$"])
a.set_yticks([0.5]); a.set_yticklabels(["$\\propto A_p/2$"])
for a in ax.flat:
    a.set_xlim(0, 8.5); a.set_ylim(0, 1.2); a.set_xlabel("$f$", labelpad=1); a.tick_params(axis="x", labelsize=8)
    a.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("01-melangeur-spectres.svg")
