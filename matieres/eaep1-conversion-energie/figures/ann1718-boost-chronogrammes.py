"""EAEP1, partiel 2017-2018, q. 5 — boost en conduction continue, alpha = 0,4.
Reconstruite (Claude) : UE = 3,6 V, L = 96 µH, f = 50 kHz (données du sujet), US = 6 V ;
courant moyen IL = 1 A choisi pour l'illustration (charge non précisée à cette question)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

a, UE, US, IL, dI = 0.4, 3.6, 6.0, 1.0, 0.3
t = np.linspace(0, 2, 2001); ph = t % 1; on = ph < a
iL = np.where(on, IL - dI / 2 + dI * ph / a, IL + dI / 2 - dI * (ph - a) / (1 - a))
sig = [("$i_L$ (A)", iL), ("$i_{Tr}$ (A)", np.where(on, iL, 0)), ("$i_D$ (A)", np.where(on, 0, iL)),
       ("$u_L$ (V)", np.where(on, UE, UE - US)), ("$u$ (V)", np.where(on, 0, US))]
fig, axs = plt.subplots(5, 1, figsize=(7, 7.5), sharex=True)
for ax, (nom, y) in zip(axs, sig):
    ax.plot(t, y, color="#2B4C9B"); ax.axhline(0, color="k", lw=0.5)
    ax.set_ylabel(nom)
    for k in (a, 1, 1 + a):
        ax.axvline(k, color="#7E889B", ls=":", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
axs[0].set_yticks([0, IL - dI / 2, IL + dI / 2]); axs[0].set_yticklabels(["0", "$I_{min}$", "$I_{Max}$"])
axs[0].axhline(IL, color="#BF6014", ls="--", lw=0.8); axs[0].text(2.01, IL, "$I_L$", color="#BF6014", va="center")
axs[1].set_yticks([0, IL - dI / 2, IL + dI / 2]); axs[1].set_yticklabels(["0", "$I_{min}$", "$I_{Max}$"])
axs[2].set_yticks([0, IL - dI / 2, IL + dI / 2]); axs[2].set_yticklabels(["0", "$I_{min}$", "$I_{Max}$"])
axs[3].set_yticks([UE - US, 0, UE]); axs[3].set_yticklabels(["$U_E-U_S$", "0", "$U_E$"])
axs[4].set_yticks([0, (1 - a) * US, US]); axs[4].set_yticklabels(["0", r"$\langle u\rangle$", "$U_S$"])
axs[4].axhline((1 - a) * US, color="#BF6014", ls="--", lw=0.8)
axs[4].set_xticks([0, a, 1, 1 + a, 2]); axs[4].set_xticklabels(["0", r"$\alpha T$", "$T$", r"$T+\alpha T$", "$2T$"])
axs[4].set_xlabel("Temps")
fig.tight_layout()
fig.savefig("ann1718-boost-chronogrammes.svg")
