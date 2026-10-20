# Annales 2022-2023, ex. 3, q. 3 : pôles et zéros de S(z) = S1(z) S2(z) = z^2 / ((z - 1/2)(z - 1/4)).
# Régénérer : python ann-2022-poles-zeros.py
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, GRIS, POLE = "#2B4C9B", "#7E889B", "#BF6014"

fig, ax = plt.subplots(figsize=(4.2, 4.2))
t = np.linspace(0, 2 * np.pi, 400)
ax.plot(np.cos(t), np.sin(t), ls=(0, (4, 3)), color=GRIS, lw=1, label="cercle unité")
ax.axhline(0, color="k", lw=0.6); ax.axvline(0, color="k", lw=0.6)
ax.plot([0.5, 0.25], [0, 0], "x", color=POLE, ms=10, mew=2, label="pôles $1/2$ et $1/4$")
ax.plot([0], [0], "o", mfc="none", mec=BLEU, ms=10, mew=2, label="zéro double en $0$")
ax.annotate("(2)", (0, 0), textcoords="offset points", xytext=(-16, 8), color=BLEU)
ax.annotate("$1/4$", (0.25, 0), textcoords="offset points", xytext=(-4, -18), color=POLE)
ax.annotate("$1/2$", (0.5, 0), textcoords="offset points", xytext=(-4, -18), color=POLE)
ax.set_xlim(-1.3, 1.3); ax.set_ylim(-1.3, 1.3); ax.set_aspect("equal")
tk = [-1, -0.5, 0, 0.5, 1]; lab = ["−1", "−0,5", "0", "0,5", "1"]
ax.set_xticks(tk, lab); ax.set_yticks(tk, lab)
ax.set_xlabel("partie réelle"); ax.set_ylabel("partie imaginaire")
ax.legend(loc="lower left", fontsize=8, frameon=False)
for s in ("top", "right"): ax.spines[s].set_visible(False)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
