"""TSIG1, partiel 2015-2016, exercice 3 : RIF symétrique h = {a, b, b, a} tel que
|H(e^{j0,2π})| = 0,8 et |H(e^{j0,5π})| = 0,5. Amplitude réelle A(ω) = 2a cos(3ω/2) + 2b cos(ω/2).
Solution retenue : A > 0 aux deux pulsations (a ≈ 0,0414 ; b ≈ 0,3950) ; autre solution
(A(0,5π) = -0,5) en pointillés. Figure calculée. Régénérer : python ann-2015-rif-phase.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
M = np.array([[2 * np.cos(0.3 * np.pi), 2 * np.cos(0.1 * np.pi)],
              [2 * np.cos(0.75 * np.pi), 2 * np.cos(0.25 * np.pi)]])
a1, b1 = np.linalg.solve(M, [0.8, 0.5])
a2, b2 = np.linalg.solve(M, [0.8, -0.5])
f = np.linspace(0, 0.5, 500)
H = lambda a, b: np.abs(np.polyval([a, b, b, a][::-1], np.exp(-2j * np.pi * f)))
for a, b in ((a1, b1), (a2, b2)):
    h = [a, b, b, a]
    for w, v in ((0.2 * np.pi, 0.8), (0.5 * np.pi, 0.5)):
        assert abs(abs(np.polyval(h[::-1], np.exp(-1j * w))) - v) < 1e-12
fig, (g, d) = plt.subplots(1, 2, figsize=(9, 3.2), gridspec_kw={"width_ratios": [1.2, 1.3]})
g.plot(f, H(a1, b1), color="#2B4C9B", lw=1.8, label=fr"$a \approx {a1:.4f}$, $b \approx {b1:.4f}$".replace(".", "{,}"))
g.plot(f, H(a2, b2), color="#7E889B", lw=1.2, ls="--", label=fr"$a \approx {a2:.4f}$, $b \approx {b2:.4f}$".replace(".", "{,}"))
g.plot([0.1, 0.25], [0.8, 0.5], "o", color="k", ms=4)
g.annotate("0,8", (0.1, 0.8), xytext=(4, 6), textcoords="offset points")
g.annotate("0,5", (0.25, 0.5), xytext=(4, 6), textcoords="offset points")
g.set_xlabel("$f$ (fréquence normalisée)"); g.set_ylabel(r"$|H(e^{j2\pi f})|$")
g.set_xlim(0, 0.5); g.set_ylim(0, 1.35); g.legend(fontsize=8, frameon=False); g.grid(alpha=.25)
g.spines[["top", "right"]].set_visible(False)
z = np.roots([a1, b1, b1, a1])  # zéros de a z^3 + b z^2 + b z + a
th = np.linspace(0, 2 * np.pi, 400)
d.plot(np.cos(th), np.sin(th), color="#7E889B", lw=0.8, ls="--")
d.plot(z.real, z.imag, "o", mfc="none", mec="#2B4C9B", ms=7, mew=1.5)
d.plot([0], [0], "x", color="#BF6014", ms=9, mew=2)
d.annotate("pôle triple", (0, 0), xytext=(4, 10), textcoords="offset points", fontsize=8, color="#BF6014")
for zz, dy, ha in zip(sorted(z.real), (-16, 10, -16), ("center", "right", "left")):
    d.annotate(f"{zz:.3f}".replace(".", ","), (zz, 0), xytext=(0, dy), textcoords="offset points", ha=ha, fontsize=8, color="#2B4C9B")
d.set_aspect("equal"); d.set_xlim(-9, 1.5); d.set_ylim(-1.6, 1.6)
d.axhline(0, color="k", lw=0.4); d.axvline(0, color="k", lw=0.4)
d.set_xlabel(r"$\mathrm{Re}(z)$"); d.set_ylabel(r"$\mathrm{Im}(z)$")
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
print(a1, b1, a2, b2, z)
