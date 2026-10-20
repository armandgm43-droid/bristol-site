"""Examen de mars 2014, ex. 2 e) : |H(e^{j2πf})| pour H(z) = z^{-1}(1 - z^{-2}) / (1 - 1,2 z^{-1} + 0,7 z^{-2} - 0,1 z^{-3})
(gain K = 1, non donné par le sujet). Régénérer : python ann-2013-module.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
f = np.linspace(-0.5, 0.5, 2001)
z = np.exp(2j * np.pi * f)
H = (z ** 2 - 1) / ((z - 0.2) * (z ** 2 - z + 0.5))
assert abs(abs(H[np.argmin(abs(f - 0.125))]) - 4.531) < 1e-3
fig, a = plt.subplots(figsize=(6.4, 2.8))
a.plot(f, abs(H), color="#2B4C9B", lw=1.6)
for f0 in (-0.125, 0.125):
    a.axvline(f0, color="#7E889B", ls="--", lw=0.8)
a.text(0.2, 4.3, r"$f = 1/8$ (argument des pôles)", color="#7E889B", fontsize=9)
a.annotate("zéro en $z=1$", (0, 0), (0.0, 1.2), ha="center", arrowprops=dict(arrowstyle="->", lw=0.6))
a.annotate("zéro en $z=-1$", (0.5, 0), (0.4, 1.2), ha="center", arrowprops=dict(arrowstyle="->", lw=0.6))
a.set_xlim(-0.5, 0.5); a.set_ylim(0, 5)
a.set_xlabel("fréquence normalisée $f$"); a.set_ylabel(r"$|H(e^{j2\pi f})|$")
a.spines[["top", "right"]].set_visible(False); a.grid(alpha=0.25)
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
