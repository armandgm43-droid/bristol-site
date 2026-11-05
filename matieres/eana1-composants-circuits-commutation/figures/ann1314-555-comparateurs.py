"""EANA1, partiel 2013-2014, ex. III q. 1 — LM555, pattes 6 et 2 reliées, e(t) triangulaire
entre 0 et 15 V. Reconstruite (Claude) : seuils Vcc/3 = 5 V (comparateur S) et
2Vcc/3 = 10 V (comparateur R), Vcc = 15 V ; période du triangle arbitraire."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

t = np.linspace(0, 2, 2001)
e = 15 * np.where((t % 1) < 0.5, 2 * (t % 1), 2 - 2 * (t % 1))
S = (e < 5).astype(float)
R = (e > 10).astype(float)
Q = np.zeros_like(t); q = 1.0
for k in range(len(t)):
    if S[k]: q = 1.0
    if R[k]: q = 0.0
    Q[k] = q
fig, axs = plt.subplots(4, 1, figsize=(7, 6.2), sharex=True)
axs[0].plot(t, e, color="#2B4C9B")
for s, nom in ((5, "$V_{cc}/3 = 5$ V"), (10, "$2V_{cc}/3 = 10$ V")):
    axs[0].axhline(s, color="#BF6014", ls="--", lw=0.8)
    axs[0].text(2.02, s, nom, color="#BF6014", va="center")
axs[0].set_ylabel("$e(t)$ (V)"); axs[0].set_yticks([0, 5, 10, 15])
for ax, y, nom in ((axs[1], S, "$S$"), (axs[2], R, "$R$"), (axs[3], Q, "$Q$")):
    ax.plot(t, y, color="#2B4C9B", lw=1.6); ax.set_ylim(-0.25, 1.35)
    ax.set_yticks([0, 1]); ax.set_ylabel(nom)
for x in (1/3, 2/3, 1 + 1/3, 1 + 2/3, 1/6, 5/6, 1 + 1/6, 1 + 5/6):
    for ax in axs:
        ax.axvline(x, color="#7E889B", ls=":", lw=0.7)
for a, b in ((0, 1/3), (5/6, 1 + 1/3), (1 + 5/6, 2)):
    axs[3].text((a + b) / 2, 1.08, "bloqué", ha="center", fontsize=8, color="#BF6014")
for a, b in ((1/3, 5/6), (1 + 1/3, 1 + 5/6)):
    axs[3].text((a + b) / 2, 0.12, "saturé", ha="center", fontsize=8, color="#BF6014")
for ax in axs:
    ax.spines[["top", "right"]].set_visible(False)
axs[3].set_xticks([]); axs[3].set_xlabel("Temps (transistor de décharge : bloqué si Q = 1, saturé si Q = 0)")
fig.tight_layout()
fig.savefig("ann1314-555-comparateurs.svg")
