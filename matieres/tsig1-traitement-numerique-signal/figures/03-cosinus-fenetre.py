"""TSIG1 ch. 3 — Spectre d'un cosinus observé sur une durée finie (fenêtre rectangulaire).
D'après les notes de cours [notes, f. 6 r°], redessinée. f0 = 10 Hz, tau = 0,4 s."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
f0, tau = 10.0, 0.4
f = np.linspace(-18, 18, 4001)
W = lambda g: tau * np.sinc(g * tau)
X0 = 0.5 * (W(f - f0) + W(f + f0))
fig, a = plt.subplots(figsize=(7, 2.8))
a.plot(f, X0, color="#2B4C9B")
a.axhline(0, color="k", lw=0.5)
a.set_xticks([-f0, 0, f0, f0 + 1 / tau])
a.set_xticklabels([r"$-f_0$", "0", r"$f_0$", r"$f_0 + 1/\tau$"])
a.set_xlabel("Fréquence $f$ (Hz)"); a.set_ylabel("$X_0(f)$")
a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("03-cosinus-fenetre.svg")
