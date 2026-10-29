"""EARF1 ch. 3 — Spectre d'amplitude d'un signal FM (modulant sinusoïdal) pour β = 0,2 ; 1 ; 3 ; 5.
D'après le support [mod-ana, p. 40], recalculée : raies A|J_n(β)| (A = 1) ; zone de Carson grisée."""
import numpy as np
from scipy.special import jv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
fig, ax = plt.subplots(4, 1, figsize=(7.5, 6.4), sharex=True)
n = np.arange(-9, 10)
for a, beta in zip(ax, [0.2, 1, 3, 5]):
    amp = np.abs(jv(n, beta))
    a.axvspan(-(beta + 1), beta + 1, color="#7E889B", alpha=0.15, lw=0)
    a.vlines(n, 0, amp, color="#2B4C9B", lw=2)
    for k, v in zip(n, amp):
        if v >= 0.01:
            a.text(k, v + 0.03, f"{v:.2f}".replace(".", ","), ha="center", fontsize=6.5)
    a.set_ylim(0, 1.15); a.set_yticks([]); a.text(-9.3, 0.8, f"$\\beta = {str(beta).replace('.', '{,}')}$", fontsize=9)
    a.spines[["top", "right", "left"]].set_visible(False)
ax[-1].set_xticks(range(-8, 9, 2))
ax[-1].set_xticklabels([f"$f_p{'+' if k > 0 else '-'}{abs(k)}f_m$" if k else "$f_p$" for k in range(-8, 9, 2)], fontsize=7)
ax[-1].set_xlabel("Fréquence ; zone grisée : $|f - f_p| \\leq (\\beta + 1) f_m$ (règle de Carson)")
fig.tight_layout(); fig.savefig("03-spectres-fm.svg")
