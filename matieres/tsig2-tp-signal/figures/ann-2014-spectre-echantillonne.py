"""TSIG2, partiel 2014-2015, ex. 1 q. 1 — Spectre d'un signal triangulaire de largeur
2 Fmax échantillonné à Fe, pour Fe > 2 Fmax, Fe = 2 Fmax et Fe < 2 Fmax.
Spectre d'origine d'après le sujet [sujet-2014] ; copies périodisées (pointillés gris)
et somme (trait plein) calculées. Amplitude normalisée : A/Te pour la copie centrale."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
GRIS, BLEU = "#7E889B", "#2B4C9B"
tri = lambda f: np.clip(1 - np.abs(f), 0, None)     # Fmax = 1
f = np.linspace(-3.2, 3.2, 3201)
cas = [(3.0, r"$F_e = 3F_{max} > 2F_{max}$"), (2.0, r"$F_e = 2F_{max}$"),
       (1.4, r"$F_e = 1{,}4\,F_{max} < 2F_{max}$ : repliement")]
fig, ax = plt.subplots(3, 1, figsize=(7, 6), sharex=True)
for a, (fe, titre) in zip(ax, cas):
    tot = np.zeros_like(f)
    for k in range(-4, 5):
        c = tri(f - k * fe); tot += c
        if k != 0:
            a.plot(f, c, color=GRIS, ls=":", lw=1)
    a.plot(f, tri(f), color=GRIS, ls="--", lw=1)
    a.plot(f, tot, color=BLEU, lw=1.6)
    a.set_title(titre, fontsize=10, loc="left")
    a.set_ylim(0, 1.6); a.set_yticks([0, 1]); a.set_yticklabels(["0", r"$A/T_e$"])
    a.set_xticks([-fe, -1, 0, 1, fe])
    a.set_xticklabels([r"$-F_e$", r"$-F_{max}$", "0", r"$F_{max}$", r"$F_e$"], fontsize=8)
    a.spines[["top", "right"]].set_visible(False)
ax[-1].set_xlabel("Fréquence $f$")
fig.tight_layout(); fig.savefig("ann-2014-spectre-echantillonne.svg")
