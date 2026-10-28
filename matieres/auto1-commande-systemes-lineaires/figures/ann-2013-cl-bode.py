"""Partiel AU201 du 10 janvier 2014, partie B : diagramme de Bode de la boucle ouverte
beta(jw) = C(jw) G'(jw), G'(p) = 100 / (p (1 + p/10)), avec un régulateur proportionnel
(question 1, wu = 100 rad/s) puis avec le régulateur à avance-retard de phase de la
question 2 (marge de phase 45° à wu). Valeurs calculées dans le corrigé.
Régénérer : python ann-2013-cl-bode.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
w0p, w0, wu = 100.0, 10.0, 100.0
w = np.logspace(-3, 4, 2000)
p = 1j * w
G = w0p / (p * (1 + p / w0))
Cp = np.sqrt(101.0)                         # proportionnel : |beta(j wu)| = 1
a = 4.5615                                  # rapport w2'/w1' de l'avance de phase
w1p, w2p = wu / np.sqrt(a), wu * np.sqrt(a)
w1, w2 = w1p / 50, w1p / 5000
C0 = 470.53
C = C0 * (1 + p / w1) * (1 + p / w1p) / ((1 + p / w2) * (1 + p / w2p))
bP, bC = Cp * G, C * G
k = np.argmin(abs(w - wu))
assert abs(abs(bC[k]) - 1) < 0.01 and abs(np.degrees(np.angle(bC[k])) + 135) < 0.3
fig, (a1, a2) = plt.subplots(2, 1, figsize=(6.4, 5.2), sharex=True)
for b, st, lab in ((bP, "--", "régulateur proportionnel ($C_0 = \\sqrt{101}$)"),
                   (bC, "-", "régulateur à avance-retard de phase (question 2)")):
    a1.semilogx(w, 20 * np.log10(abs(b)), st, color="#2B4C9B", lw=1.5, label=lab)
    a2.semilogx(w, np.degrees(np.unwrap(np.angle(b))), st, color="#2B4C9B", lw=1.5)
for ax in (a1, a2):
    ax.axvline(wu, color="#7E889B", ls=":", lw=0.9)
    ax.grid(alpha=0.25, which="both"); ax.spines[["top", "right"]].set_visible(False)
a1.axhline(0, color="k", lw=0.6)
a2.axhline(-180, color="k", lw=0.6)
a2.annotate("$M_\\varphi = 45°$", (wu, -135), (300, -110), arrowprops=dict(arrowstyle="->", lw=0.6))
a2.annotate("$M_\\varphi \\approx 5{,}7°$", (wu, -174.3), (1.5, -170), arrowprops=dict(arrowstyle="->", lw=0.6))
a1.text(wu * 1.1, 60, "$\\omega_u = 100$ rad/s", color="#7E889B", fontsize=9)
a1.set_ylabel("$|\\beta(j\\omega)|$ (dB)"); a2.set_ylabel("arg $\\beta(j\\omega)$ (°)")
a2.set_xlabel("pulsation $\\omega$ (rad/s)"); a2.set_ylim(-185, -80)
a1.legend(fontsize=8, frameon=False, loc="lower left")
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
