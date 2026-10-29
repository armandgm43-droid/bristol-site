"""EARF1 ch. 4 — Allures temporelles ASK, FSK et PSK pour le message binaire 10010.
D'après le support [mod-num, p. 7], recalculée (4 périodes de porteuse par bit ; ASK : E0 = E/3, E1 = E ;
FSK : f0 = 2 bits⁻¹, f1 = 4 bits⁻¹)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
C1, C0 = "#2B8C8C", "#D2691E"
bits = [1, 0, 0, 1, 0]
t = np.linspace(0, 5, 5000, endpoint=False); b = np.array(bits)[t.astype(int)]
fc = 4.0
ask = np.where(b == 1, 1.0, 1 / 3) * np.cos(2 * np.pi * fc * t)
ph = 2 * np.pi * np.cumsum(np.where(b == 1, 4.0, 2.0)) * (t[1] - t[0])
fsk = np.cos(ph)
psk = np.cos(2 * np.pi * fc * t + np.pi * b)
fig, ax = plt.subplots(3, 1, figsize=(7.5, 4.8), sharex=True)
for a, s, nom in zip(ax, [ask, fsk, psk], ["ASK", "FSK (phase continue)", "PSK"]):
    for k in range(5):
        sel = (t >= k) & (t < k + 1)
        a.plot(t[sel], s[sel], color=C1 if bits[k] else C0, lw=0.9)
        a.axvline(k, color="#999", ls=":", lw=0.6)
    a.set_ylabel(nom, fontsize=9); a.set_yticks([]); a.spines[["top", "right"]].set_visible(False)
for k in range(5):
    ax[0].text(k + 0.5, 1.25, str(bits[k]), ha="center")
ax[0].set_ylim(-1.2, 1.45)
ax[-1].set_xlabel("$t / T_r$ (durée d'un bit)")
fig.tight_layout(); fig.savefig("04-allures-ask-fsk-psk.svg")
