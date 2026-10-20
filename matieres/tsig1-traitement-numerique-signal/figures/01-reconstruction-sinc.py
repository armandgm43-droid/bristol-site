"""TSIG1 ch. 1 — Reconstruction par somme de sinus cardinaux.
D'après les notes de cours [notes, f. 3 r°], redessinée. Signal d'exemple : somme de deux sinusoïdes, Te = 1."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})

Te = 1.0
x = lambda t: 0.8 * np.sin(2 * np.pi * 0.11 * t) + 0.4 * np.cos(2 * np.pi * 0.27 * t)
n = np.arange(-4, 5)
t = np.linspace(-6, 6, 1500)
fig, a = plt.subplots(figsize=(7, 3))
tot = np.zeros_like(t)
for k in n:
    s = x(k * Te) * np.sinc((t - k * Te) / Te)
    tot += s
    a.plot(t, s, color="#7E889B", lw=0.7, ls="--")
a.plot(t, tot, color="#2B4C9B", lw=1.6, label="somme des sinus cardinaux")
a.stem(n * Te, x(n * Te), linefmt="k-", markerfmt="ko", basefmt=" ", label="échantillons $x_a(nT_e)$")
a.axhline(0, color="k", lw=0.5)
a.set_xlabel("Temps $t$ (en unités de $T_e$)"); a.set_ylabel("Amplitude")
a.legend(frameon=False, fontsize=8, loc="lower left")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("01-reconstruction-sinc.svg")
