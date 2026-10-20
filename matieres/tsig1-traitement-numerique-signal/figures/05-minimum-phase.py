"""TSIG1 ch. 5 — H1 = (z-b)/(z+a) (minimum de phase), H2 = (bz-1)/(z+a), A = (bz-1)/(z-b) ; a = 0,5, b = 0,6.
D'après les notes de cours [notes, f. 12 v° et f. 13 r°], redessinée ; retards de groupe calculés (dérivée numérique de la phase déroulée)
et comparés à la formule r_A = (1 - b^2) / (1 - 2 b cos w + b^2)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
a_, b_ = 0.5, 0.6
w = np.linspace(-np.pi, np.pi, 4001)
z = np.exp(1j * w)
H1 = (z - b_) / (z + a_); H2 = (b_ * z - 1) / (z + a_); A = (b_ * z - 1) / (z - b_)
gd = lambda H: -np.gradient(np.unwrap(np.angle(H)), w)
rA_th = (1 - b_ ** 2) / (1 - 2 * b_ * np.cos(w) + b_ ** 2)
assert np.allclose(np.abs(H1), np.abs(H2)) and np.allclose(np.abs(A), 1)
assert np.max(np.abs(gd(A)[5:-5] - rA_th[5:-5])) < 1e-3
assert np.all(gd(H2)[5:-5] >= gd(H1)[5:-5] - 1e-9)
fig, ax = plt.subplots(1, 3, figsize=(9.5, 3), gridspec_kw={"width_ratios": [1, 1, 1.8]})
th = np.linspace(0, 2 * np.pi, 400)
for p, (titre, zero) in zip(ax[:2], ((r"$H_1$ (minimum de phase)", b_), (r"$H_2$", 1 / b_))):
    p.plot(np.cos(th), np.sin(th), color="k", lw=0.8)
    p.plot([-a_], [0], "x", color="#BF6014", ms=8, mew=2)
    p.plot([zero], [0], "o", mfc="none", mec="#2B4C9B", ms=7, mew=1.5)
    p.set_aspect("equal"); p.set_xlim(-1.4, 2.0); p.set_ylim(-1.4, 1.4)
    p.axhline(0, color="k", lw=0.4); p.axvline(0, color="k", lw=0.4)
    p.set_title(titre, fontsize=10); p.set_xlabel(r"$\mathrm{Re}(z)$")
ax[0].set_ylabel(r"$\mathrm{Im}(z)$")
c = ax[2]
c.plot(w, gd(H1), color="#2B4C9B", label=r"$r_{H_1}$")
c.plot(w, gd(H2), color="#BF6014", label=r"$r_{H_2} = r_{H_1} + r_A$")
c.plot(w, rA_th, color="#7E889B", ls="--", label=r"$r_A$")
c.set_xticks([-np.pi, 0, np.pi]); c.set_xticklabels([r"$-\pi$", "0", r"$\pi$"])
c.set_xlabel(r"Pulsation normalisée $\omega$ (rad)"); c.set_ylabel("Retard de groupe (échantillons)")
c.axhline(0, color="k", lw=0.4); c.legend(frameon=False, fontsize=8)
c.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("05-minimum-phase.svg")
