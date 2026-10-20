"""TSIG1, partiel 2019-2020, exercice 1 : RIF antisymétrique h = {a, b, -b, -a} tel que
|H(e^{j0,25π})| = 0,5 et |H(e^{j0,5π})| = 1. H(e^{j2πf}) = 2j e^{-j3πf} [a sin(3πf) + b sin(πf)].
Solution retenue : amplitude positive aux deux fréquences (a ≈ -0,0381 ; b ≈ 0,7452) ;
autre solution (amplitude -0,5 en 0,25π) en pointillés. Figure calculée.
Régénérer : python ann-2019-rif-antisymetrique.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
s = np.sin
M = np.array([[2 * s(0.375 * np.pi), 2 * s(0.125 * np.pi)],
              [2 * s(0.75 * np.pi), 2 * s(0.25 * np.pi)]])
a1, b1 = np.linalg.solve(M, [0.5, 1.0])
a2, b2 = np.linalg.solve(M, [-0.5, 1.0])
f = np.linspace(0, 0.5, 500)
H = lambda a, b: np.abs(np.polyval([a, b, -b, -a][::-1], np.exp(-2j * np.pi * f)))
for a, b in ((a1, b1), (a2, b2)):
    h = [a, b, -b, -a]
    for w, v in ((0.25 * np.pi, 0.5), (0.5 * np.pi, 1.0)):
        assert abs(abs(np.polyval(h[::-1], np.exp(-1j * w))) - v) < 1e-12
fig, (g, d) = plt.subplots(1, 2, figsize=(9.5, 3.2), gridspec_kw={"width_ratios": [1.3, 1]})
g.plot(f, H(a1, b1), color="#2B4C9B", lw=1.8, label=fr"$a \approx {a1:.4f}$, $b \approx {b1:.4f}$".replace(".", "{,}"))
g.plot(f, H(a2, b2), color="#7E889B", lw=1.2, ls="--", label=fr"$a \approx {a2:.4f}$, $b \approx {b2:.4f}$".replace(".", "{,}"))
g.plot([0.125, 0.25], [0.5, 1.0], "o", color="k", ms=4)
g.annotate("0,5", (0.125, 0.5), xytext=(-18, 6), textcoords="offset points")
g.annotate("1", (0.25, 1.0), xytext=(-12, 6), textcoords="offset points")
g.set_xlabel("$f$ (fréquence normalisée)"); g.set_ylabel(r"$|H(e^{j2\pi f})|$")
g.set_xlim(0, 0.5); g.set_ylim(0, 5.5); g.legend(fontsize=8, frameon=False, loc="upper left"); g.grid(alpha=.25)
g.spines[["top", "right"]].set_visible(False)
z = np.roots([a1, b1, -b1, -a1])  # zéros de a z^3 + b z^2 - b z - a
th = np.linspace(0, 2 * np.pi, 400)
d.plot(np.cos(th), np.sin(th), color="#7E889B", lw=0.8, ls="--")
zin = z[np.abs(z) < 2]                 # zéros visibles dans le cadre
zout = z[np.abs(z) >= 2]               # zéro lointain (≈ 18,52), signalé par une flèche
d.plot(zin.real, zin.imag, "o", mfc="none", mec="#2B4C9B", ms=7, mew=1.5)
d.plot([0], [0], "x", color="#BF6014", ms=9, mew=2)
d.annotate("pôle triple", (0, 0), xytext=(-6, 10), textcoords="offset points", ha="right", fontsize=8, color="#BF6014")
for zz, dy in zip(sorted(zin.real), (-16, 10)):
    d.annotate(f"{zz:.3f}".replace(".", ","), (zz, 0), xytext=(0, dy), textcoords="offset points", ha="center", fontsize=8, color="#2B4C9B")
d.annotate(f"zéro en {zout[0].real:.2f}".replace(".", ",") + " (hors cadre)", xy=(2.45, 0), xytext=(2.4, 0.9),
           ha="right", fontsize=8, color="#2B4C9B", arrowprops=dict(arrowstyle="->", color="#2B4C9B"))
d.set_aspect("equal"); d.set_xlim(-1.5, 2.5); d.set_ylim(-1.5, 1.5)
d.axhline(0, color="k", lw=0.4); d.axvline(0, color="k", lw=0.4)
d.set_xlabel(r"$\mathrm{Re}(z)$"); d.set_ylabel(r"$\mathrm{Im}(z)$")
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
print(a1, b1, a2, b2, z)
