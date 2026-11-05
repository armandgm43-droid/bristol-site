"""EAEP1, TD SEPIC (EI-TD 2024), q. 8 et 13 — SEPIC en conduction continue.
Ue = 6 V, Is = 1,5 A, alpha = 0,4 (q. 13), f = 20 kHz et L1 = 330 µH (q. 14).
L2 = 680 µH : valeur NON donnée par l'énoncé, choisie seulement pour respecter L1 < L2.
Reconstruite (Claude) : tensions u_L1 = u_L2 (Ue puis -Us) et courants i_L1, i_L2."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

a, Ue, Is, f, L1, L2 = 0.4, 6.0, 1.5, 20e3, 330e-6, 680e-6
T = 1 / f
Us, Ie = a / (1 - a) * Ue, a / (1 - a) * Is
t = np.linspace(0, 2 * T, 4001)
ph = (t % T) / T
u = np.where(ph < a, Ue, -Us)

def courant(L, moy):
    dI = Ue * a * T / L
    m = moy - dI / 2
    return np.where(ph < a, m + dI * ph / a, m + dI - dI * (ph - a) / (1 - a)), m, m + dI

i1, I1m, I1M = courant(L1, Ie)
i2, I2m, I2M = courant(L2, Is)
us = t * 1e6
fig, (a1, a2) = plt.subplots(2, 1, figsize=(7, 5), sharex=True)
a1.plot(us, u, color="#2B4C9B")
a1.axhline(0, color="k", lw=0.6)
a1.fill_between(us, 0, u, where=ph < a, color="#2B4C9B", alpha=0.12)
a1.fill_between(us, 0, u, where=ph >= a, color="#BF6014", alpha=0.12)
a1.set_ylabel("$u_{L1} = u_{L2}$ (V)")
a1.set_yticks([-Us, 0, Ue]); a1.set_yticklabels(["$-U_s = -4$", "0", "$U_e = 6$"])
a1.text(10, Ue * 0.45, r"aire $U_e\,\alpha T$", ha="center")
a1.text(35, -Us * 0.55, r"aire $-U_s(1-\alpha)T$", ha="center")
a2.plot(us, i1, color="#2B4C9B", label=r"$i_{L1}$ ($L_1$ = 330 µH, moyenne $I_e$ = 1 A)")
a2.plot(us, i2, color="#BF6014", label=r"$i_{L2}$ ($L_2$ = 680 µH, moyenne $I_s$ = 1,5 A)")
a2.set_yticks([I1m, I1M, I2m, I2M])
a2.set_yticklabels([f"$I_{{1m}}$ = {I1m:.2f}".replace(".", ","), f"$I_{{1M}}$ = {I1M:.2f}".replace(".", ","),
                    f"$I_{{2m}}$ = {I2m:.2f}".replace(".", ","), f"$I_{{2M}}$ = {I2M:.2f}".replace(".", ",")])
a2.set_ylim(0, 2); a2.set_ylabel("Courants (A)")
a2.legend(loc="lower right", frameon=False, fontsize=9)
for ax in (a1, a2):
    for k in (a * T, T, T + a * T):
        ax.axvline(k * 1e6, color="#7E889B", ls=":", lw=0.8)
    ax.spines[["top", "right"]].set_visible(False)
a2.set_xticks([0, 20, 50, 70, 100])
a2.set_xlabel("Temps (µs)  —  $\\alpha T$ = 20 µs, $T$ = 50 µs")
fig.tight_layout()
fig.savefig("td01-sepic-chronogrammes.svg")
print(Us, Ie, I1m, I1M, I2m, I2M)
