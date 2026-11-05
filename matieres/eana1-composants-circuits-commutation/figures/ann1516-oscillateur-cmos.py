"""EANA1, partiel 2015-2016, ex. II — oscillateur à portes CMOS (VDD = 5 V, seuil VDD/2),
R1 = 100 kΩ, R2 = 10 kΩ, C1 = 220 nF, diode D1 idéale (seuil 0 V). Reconstruite (Claude).
Trait plein : portes sans protection d'entrée (énoncé) ; tirets : avec diodes de protection
supposées idéales (V2 limité à [0, VDD]), question 4."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

VDD, R1, R2, C = 5.0, 100e3, 10e3, 220e-9
dt, tf = 2e-6, 0.075


def simule(protection):
    t = np.arange(-0.004, tf, dt)
    uc = VDD          # uC = V2 - V3, régime de repos : V2 = 5 V, V3 = 0
    V1, V2, V3 = [], [], []
    v3 = 0.0
    for tk in t:
        vc = VDD if tk >= 0 else 0.0
        v1 = VDD - v3
        v2 = v3 + uc
        if protection and (v2 > VDD or v2 < 0):
            v2 = min(max(v2, 0.0), VDD); uc = v2 - v3
        # commutation de la porte II (NAND de V2 et Vc) puis III
        g2 = 0.0 if (v2 > VDD / 2 and vc > VDD / 2) else VDD
        n3 = VDD - g2
        if n3 != v3:
            v3 = n3; v1 = VDD - v3; v2 = v3 + uc
            if protection and (v2 > VDD or v2 < 0):
                v2 = min(max(v2, 0.0), VDD); uc = v2 - v3
        V1.append(v1); V2.append(v2); V3.append(v3)
        r = R2 if v2 > v1 else R1 + R2     # D1 passante si V2 > V1 (court-circuite R1)
        uc += (v1 - v2) / (r * C) * dt
    return t * 1e3, np.array(V1), np.array(V2), np.array(V3)


t, V1, V2, V3 = simule(False)
tp, _, V2p, _ = simule(True)
fig, axs = plt.subplots(3, 1, figsize=(7, 6.4), sharex=True)
axs[0].plot(t, V3, color="#2B4C9B"); axs[0].set_ylabel("$V_3$ (V)")
axs[1].plot(t, V1, color="#2B4C9B"); axs[1].set_ylabel("$V_1$ (V)")
axs[2].plot(t, V2, color="#2B4C9B", label="sans protection")
axs[2].plot(tp, V2p, color="#BF6014", ls="--", lw=1.2, label="avec protection idéale")
axs[2].axhline(VDD / 2, color="#7E889B", ls=":", lw=0.8)
axs[2].text(tf * 1e3 + 0.5, VDD / 2, "$V_{DD}/2$", color="#7E889B", va="center")
axs[2].set_ylabel("$V_2$ (V)"); axs[2].legend(fontsize=8, loc="upper right", ncol=2)
axs[2].set_yticks([-2.5, 0, 2.5, 5, 7.5, 10])
for ax in axs:
    ax.axhline(0, color="k", lw=0.5)
    ax.spines[["top", "right"]].set_visible(False)
axs[2].set_xlabel("$t$ (ms) ; $V_c$ passe de 0 à $V_{DD}$ à $t = 0$")
fig.tight_layout()
fig.savefig("ann1516-oscillateur-cmos.svg")
