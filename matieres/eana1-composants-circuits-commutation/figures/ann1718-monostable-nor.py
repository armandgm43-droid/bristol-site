"""EANA1, partiel 2017-2018, ex. IV q. 5 — monostable à deux portes NOR CMOS.
Reconstruite (Claude) : Vdd = 10 V, seuil Vdd/2, C1 = 1 nF, R1 = 14,4 kΩ (TH = 10 µs),
impulsion d'entrée V1 de durée T1 = 1 µs (« très petite ») ; entrées supposées sans
protection (V3 monte à 15 V au retour), comme dans le sujet 2015-2016."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

Vdd, C = 10.0, 1e-9
TH = 10e-6
R = TH / (C * np.log(2)); tau = R * C
T1 = 1e-6
t = np.linspace(-5e-6, 60e-6, 6501)
V1 = np.where((t >= 0) & (t < T1), Vdd, 0.0)
V4 = np.where((t >= 0) & (t < TH), Vdd, 0.0)
V2 = np.where((t >= 0) & (t < TH), 0.0, Vdd)
V3 = np.where(t < 0, Vdd, np.where(t < TH, Vdd * (1 - np.exp(-np.clip(t, 0, None) / tau)),
                                   Vdd + Vdd / 2 * np.exp(-(t - TH) / tau)))
fig, axs = plt.subplots(4, 1, figsize=(7, 6.6), sharex=True)
for ax, y, nom in zip(axs, (V1, V2, V3, V4), ("$V_1$", "$V_2$", "$V_3$", "$V_4$")):
    ax.plot(t * 1e6, y, color="#2B4C9B", lw=1.5)
    ax.axhline(0, color="k", lw=0.5); ax.set_ylabel(nom + " (V)")
    ax.axvline(0, color="#7E889B", ls=":", lw=0.7); ax.axvline(TH * 1e6, color="#7E889B", ls=":", lw=0.7)
    ax.set_yticks([0, 5, 10]); ax.spines[["top", "right"]].set_visible(False)
axs[2].set_yticks([0, 5, 10, 15])
axs[2].axhline(Vdd / 2, color="#BF6014", ls="--", lw=0.8)
axs[2].text(61, Vdd / 2, "$V_{dd}/2$", color="#BF6014", va="center")
axs[3].set_xticks([0, TH * 1e6, 20, 30, 40, 50, 60])
axs[3].set_xticklabels(["0", "$T_H$ = 10", "20", "30", "40", "50", "60"])
axs[3].set_xlabel("$t$ (µs) ; $R_1 = 14{,}4$ kΩ, $C_1 = 1$ nF, $\\tau = R_1 C_1 = 14{,}4$ µs")
fig.tight_layout()
fig.savefig("ann1718-monostable-nor.svg")
