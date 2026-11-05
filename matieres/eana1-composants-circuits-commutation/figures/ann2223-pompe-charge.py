"""EANA1, partiel 2022-2023, ex. III q. 8 — pompe de charge à diodes (sortie négative).
Simulation (Claude) du modèle de l'énoncé : Ve créneau 5 V / 0 V (T1 = 10 ms, T = 20 ms),
C1 = 22 µF, C2 = 33 µF, diodes VD = 0,6 V et RD = 1 Ω ; C1 chargé sous 4,4 V et C2
déchargé à t = 0⁻ (voir le corrigé)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

C1, C2, VD, RD, T1, T, dt = 22e-6, 33e-6, 0.6, 1.0, 10e-3, 20e-3, 2e-7
u1, u2 = 4.4, 0.0              # u1 = Ve - VA, u2 = Vs
t = np.arange(-4e-3, 34e-3, dt)
VE, VA, VS = [], [], []
for tk in t:
    ve = 5.0 if tk < 0 or (tk % T) >= T1 else 0.0
    va = ve - u1
    i1 = max(0.0, (va - VD) / RD)          # D1 : de A vers la masse
    i2 = max(0.0, (u2 - va - VD) / RD)     # D2 : de la sortie vers A
    VE.append(ve); VA.append(va); VS.append(u2)
    u1 += (i1 - i2) / C1 * dt
    u2 -= i2 / C2 * dt
t = t * 1e3
fig, axs = plt.subplots(3, 1, figsize=(7, 6.2), sharex=True)
axs[0].plot(t, VE, color="#2B4C9B"); axs[0].set_ylabel("$V_e$ (V)"); axs[0].set_yticks([0, 5])
axs[1].plot(t, VA, color="#2B4C9B"); axs[1].set_ylabel("$V_A$ (V)")
axs[1].set_yticks([-4.4, -3.03, -2.12, 0, 0.6, 2.88]); axs[1].set_yticklabels(["−4,4", "−3,03", "−2,12", "0", "0,6", "2,88"], fontsize=8)
axs[2].plot(t, VS, color="#2B4C9B", lw=1.8); axs[2].set_ylabel("$V_S$ (V)")
axs[2].set_yticks([-3.8, -2.43, -1.52, 0]); axs[2].set_yticklabels(["−3,8", "−2,43", "−1,52", "0"])
axs[2].axhline(-3.8, color="#BF6014", ls="--", lw=0.8)
axs[2].text(30.5, -3.65, "limite $-(E - 2V_D)$", color="#BF6014", fontsize=8)
for ax in axs:
    ax.axhline(0, color="k", lw=0.5)
    for x in (0, 10, 20, 30):
        ax.axvline(x, color="#7E889B", ls=":", lw=0.7)
    ax.spines[["top", "right"]].set_visible(False)
axs[2].set_xticks([0, 10, 20, 30]); axs[2].set_xticklabels(["0", "$T_1$", "$T$", "$T + T_1$"])
axs[2].set_xlabel("$t$ (ms) ; transferts de charge en quelques dizaines de µs (invisibles à cette échelle)")
fig.tight_layout()
fig.savefig("ann2223-pompe-charge.svg")
