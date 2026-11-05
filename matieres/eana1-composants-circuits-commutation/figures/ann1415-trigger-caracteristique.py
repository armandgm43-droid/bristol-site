"""EANA1, partiel 2014-2015, ex. II q. 1 — caractéristique S(Vc) du trigger inverseur à AOP.
Reconstruite (Claude) : seuils ±k VSAT avec k = R1/(R1 + R2) ; valeurs de la question 6
(VSAT = 14 V, R1 = 2 R2, d'où k = 2/3 et seuils ±9,33 V)."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

V, k = 14.0, 2 / 3
s = k * V
fig, ax = plt.subplots(figsize=(5.8, 3.8))
ax.plot([-18, s, s], [V, V, -V], color="#2B4C9B", lw=1.8)
ax.plot([18, -s, -s], [-V, -V, V], color="#2B4C9B", lw=1.8, ls="--")
ax.annotate("", xy=(s, 2), xytext=(s, 8), arrowprops=dict(arrowstyle="->", color="#BF6014"))
ax.annotate("", xy=(-s, -2), xytext=(-s, -8), arrowprops=dict(arrowstyle="->", color="#BF6014"))
ax.axhline(0, color="k", lw=0.6); ax.axvline(0, color="k", lw=0.6)
ax.set_xticks([-s, 0, s]); ax.set_xticklabels([r"$-k\,V_{SAT}$", "0", r"$+k\,V_{SAT}$"])
ax.set_yticks([-V, 0, V]); ax.set_yticklabels([r"$-V_{SAT}$", "0", r"$+V_{SAT}$"])
ax.set_xlabel("$V_C$ (entrée)"); ax.set_ylabel("$S$ (sortie)")
ax.text(-17.5, 2.0, "trait plein : $V_C$ croissant\ntirets : $V_C$ décroissant", fontsize=8, color="#2B4C9B")
ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig("ann1415-trigger-caracteristique.svg")
