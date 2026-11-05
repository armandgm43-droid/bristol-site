"""EAEP1, partiel 2022-2023, q. 5, 6 et 8 — buck-boost (chargeur Li-ion) en conduction continue.
Reconstruite (Claude) : alpha = 0,4, Ui = 3,3 V, L = 330 µH, f = 50 kHz (données du sujet) ;
Uo = 2,2 V ; charge Ro = 6,6 ohms (valeur de la q. 7) choisie pour fixer les courants."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

a, Ui, L, f, Ro = 0.4, 3.3, 330e-6, 50e3, 6.6
Uo = Ui * a / (1 - a); Io = Uo / Ro; IL = Io / (1 - a); dI = Ui * a / (L * f)
t = np.linspace(0, 2, 2001); ph = t % 1; on = ph < a
iL = np.where(on, IL - dI / 2 + dI * ph / a, IL + dI / 2 - dI * (ph - a) / (1 - a))
sig = [("$u_L$ (V)", np.where(on, Ui, -Uo)), ("$i_L$ (A)", iL), ("$i_Q$ (A)", np.where(on, iL, 0)),
       ("$i_D$ (A)", np.where(on, 0, iL)), ("$i_{C_o}$ (A)", np.where(on, 0, iL) - Io)]
fig, axs = plt.subplots(5, 1, figsize=(7, 7.5), sharex=True)
for ax, (nom, y) in zip(axs, sig):
    ax.plot(t, y, color="#2B4C9B"); ax.axhline(0, color="k", lw=0.5); ax.set_ylabel(nom)
    for k in (a, 1, 1 + a):
        ax.axvline(k, color="#7E889B", ls=":", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
axs[0].set_yticks([-Uo, 0, Ui]); axs[0].set_yticklabels(["$-U_o$", "0", "$U_i$"])
for ax in axs[1:4]:
    ax.set_yticks([0, IL - dI / 2, IL + dI / 2]); ax.set_yticklabels(["0", "$I_{min}$", "$I_{Max}$"])
axs[1].axhline(IL, color="#BF6014", ls="--", lw=0.8); axs[1].text(2.01, IL, "$I_L$", color="#BF6014", va="center")
axs[2].axhline(a * IL, color="#BF6014", ls="--", lw=0.8); axs[2].text(2.01, a * IL, "$I_Q$", color="#BF6014", va="center")
axs[3].axhline((1 - a) * IL, color="#BF6014", ls="--", lw=0.8); axs[3].text(2.01, (1 - a) * IL, "$I_D$", color="#BF6014", va="center")
axs[4].set_yticks([-Io, 0, IL + dI / 2 - Io]); axs[4].set_yticklabels(["$-I_o$", "0", "$I_{Max}-I_o$"])
axs[4].fill_between(t, 0, np.where(on, 0, iL) - Io, where=on, color="#BF6014", alpha=0.15)
axs[4].set_xticks([0, a, 1, 1 + a, 2]); axs[4].set_xticklabels(["0", r"$\alpha T$", "$T$", r"$T+\alpha T$", "$2T$"])
axs[4].set_xlabel("Temps")
fig.tight_layout()
fig.savefig("ann2223-buck-boost-chronogrammes.svg")
