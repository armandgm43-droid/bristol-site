"""EAEP1, partiel 2016-2017, ex. 1, q. 9 et 14 — SEPIC en conduction continue, alpha = 0,4.
Reconstruite (Claude) : tensions v_L1 = v_L2 (Ue puis -Us) et courants i_L1, i_L2.
Ue = 18 V, Us = 12 V (données de la q. 17) ; valeurs moyennes I1 = Ie, I2 = Is pour Is = 5 A ;
ondulations de courant choisies pour l'illustration (L1, L2 non donnés)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

a, Ue, Us, Is = 0.4, 18.0, 12.0, 5.0
I1, I2, dI1, dI2 = Is * Us / Ue, Is, 0.8, 1.2
t = np.linspace(0, 2, 2001)              # en périodes T
ph = t % 1
v = np.where(ph < a, Ue, -Us)
def tri(I, dI):
    return np.where(ph < a, I - dI / 2 + dI * ph / a, I + dI / 2 - dI * (ph - a) / (1 - a))
fig, (a1, a2) = plt.subplots(2, 1, figsize=(7, 4.6), sharex=True)
a1.plot(t, v, color="#2B4C9B")
a1.axhline(0, color="k", lw=0.6)
a1.set_ylabel("$v_{L1} = v_{L2}$ (V)")
a1.set_yticks([-Us, 0, Ue]); a1.set_yticklabels(["$-U_s$", "0", "$U_e$"])
a1.fill_between(t, 0, v, where=ph < a, color="#2B4C9B", alpha=0.12)
a1.fill_between(t, 0, v, where=ph >= a, color="#BF6014", alpha=0.12)
a1.text(0.2, Ue * 0.45, r"aire $U_e\,\alpha T$", ha="center")
a1.text(0.7, -Us * 0.55, r"aire $-U_s(1-\alpha)T$", ha="center")
a2.plot(t, tri(I1, dI1), color="#2B4C9B", label="$i_{L1}$")
a2.plot(t, tri(I2, dI2), color="#BF6014", label="$i_{L2}$")
a2.set_yticks([I1 - dI1 / 2, I1 + dI1 / 2, I2 - dI2 / 2, I2 + dI2 / 2])
a2.set_yticklabels(["$I_{10}$", "$I_{1m}$", "$I_{20}$", "$I_{2m}$"])
a2.set_ylim(0, 6.5); a2.set_ylabel("Courants")
a2.legend(loc="lower right", frameon=False)
for ax in (a1, a2):
    for k in (a, 1, 1 + a):
        ax.axvline(k, color="#7E889B", ls=":", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
a2.set_xticks([0, a, 1, 1 + a, 2]); a2.set_xticklabels(["0", r"$\alpha T$", "$T$", r"$T+\alpha T$", "$2T$"])
a2.set_xlabel("Temps")
fig.tight_layout()
fig.savefig("ann1617-sepic-chronogrammes.svg")
