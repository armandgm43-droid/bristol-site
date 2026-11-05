"""EAEP1, partiel 2017-2018, q. 12 et 13 — boost en conduction discontinue, alpha = 0,6.
Reconstruite (Claude) : UE = 3,6 V ; point de fonctionnement choisi pour l'illustration
US = 4 UE (d'où beta = alpha US/(US - UE) = 0,8)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

a, UE = 0.6, 3.6
US = 4 * UE; b = a * US / (US - UE)
t = np.linspace(0, 2, 4001); ph = t % 1
s1, s2 = ph < a, (ph >= a) & (ph < b)
iL = np.where(s1, ph / a, np.where(s2, 1 - (ph - a) / (b - a), 0))
u = np.where(s1, 0, np.where(s2, US, UE))
uL = np.where(s1, UE, np.where(s2, UE - US, 0))
fig, axs = plt.subplots(3, 1, figsize=(7, 5.6), sharex=True)
for ax, (nom, y) in zip(axs, [("$i_L$", iL), ("$u$ (V)", u), ("$u_L$ (V)", uL)]):
    ax.plot(t, y, color="#2B4C9B"); ax.axhline(0, color="k", lw=0.5); ax.set_ylabel(nom)
    for k in (a, b, 1, 1 + a, 1 + b):
        ax.axvline(k, color="#7E889B", ls=":", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
axs[0].set_yticks([0, 1]); axs[0].set_yticklabels(["0", "$I_{Max}$"])
axs[1].set_yticks([0, UE, US]); axs[1].set_yticklabels(["0", "$U_E$", "$U_S$"])
axs[1].axhline(UE, color="#BF6014", ls="--", lw=0.8); axs[1].text(2.01, UE, r"$\langle u\rangle$", color="#BF6014", va="center")
axs[2].set_yticks([UE - US, 0, UE]); axs[2].set_yticklabels(["$U_E-U_S$", "0", "$U_E$"])
axs[2].fill_between(t, 0, uL, where=ph < a, color="#2B4C9B", alpha=0.15)
axs[2].fill_between(t, 0, uL, where=(ph >= a) & (ph < b), color="#BF6014", alpha=0.15)
axs[2].set_xticks([0, a, b, 1, 2]); axs[2].set_xticklabels(["0", r"$\alpha T$", r"$\beta T$", "$T$", "$2T$"])
axs[2].set_xlabel("Temps")
fig.tight_layout()
fig.savefig("ann1718-boost-discontinu.svg")
