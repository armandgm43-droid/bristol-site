"""EANA1, partiel 2014-2015, ex. II q. 4 et 6 — multivibrateur astable à AOP.
Reconstruite (Claude) : VSAT = 14 V, R = 2,2 kΩ, C = 4,7 µF, R1 = 2 R2 (k = 2/3) ;
condensateur déchargé à t = 0 et S(0) = +VSAT (choix par défaut, l'état initial n'est pas imposé)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

V, R, C, k = 14.0, 2.2e3, 4.7e-6, 2 / 3
tau, dt = R * C, 1e-6
t = np.arange(0, 0.09, dt)
vc, s = 0.0, V
VC, S = [], []
for _ in t:
    VC.append(vc); S.append(s)
    vc += (s - vc) / tau * dt
    if s > 0 and vc >= k * V: s = -V
    elif s < 0 and vc <= -k * V: s = V
t1 = tau * np.log(3); th = tau * np.log(5)
fig, axs = plt.subplots(2, 1, figsize=(7, 4.8), sharex=True)
axs[0].plot(t * 1e3, VC, color="#2B4C9B")
for y, nom in ((k * V, "+9,33 V"), (-k * V, "−9,33 V")):
    axs[0].axhline(y, color="#BF6014", ls="--", lw=0.8); axs[0].text(91, y, nom, color="#BF6014", va="center")
axs[1].plot(t * 1e3, S, color="#2B4C9B")
axs[1].set_yticks([-V, 0, V]); axs[1].set_yticklabels(["−14", "0", "+14"])
axs[0].set_ylabel("$V_C$ (V)"); axs[1].set_ylabel("$S$ (V)")
for ax in axs:
    ax.axhline(0, color="k", lw=0.5)
    for x in (t1, t1 + th, t1 + 2 * th, t1 + 3 * th, t1 + 4 * th):
        ax.axvline(x * 1e3, color="#7E889B", ls=":", lw=0.7)
    ax.spines[["top", "right"]].set_visible(False)
axs[1].set_xticks([0, t1 * 1e3, (t1 + th) * 1e3, (t1 + 2 * th) * 1e3, (t1 + 3 * th) * 1e3, (t1 + 4 * th) * 1e3])
axs[1].set_xticklabels(["0", "11,4", "28,0", "44,6", "61,3", "77,9"])
axs[1].set_xlabel("$t$ (ms) — première demi-alternance 11,4 ms, puis demi-période 16,6 ms")
fig.tight_layout()
fig.savefig("ann1415-astable-chronogrammes.svg")
