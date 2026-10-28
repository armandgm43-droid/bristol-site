"""Partiel AU201 du 6 janvier 2015, partie B : module de la sensibilité de l'entrée
U(jw)/E(jw) = C(jw) / (1 + beta(jw)) avec G'(p) = 100 / (p (1 + p/10)) et le régulateur
à avance de phase de la question 2 (marge de phase 54° à wu = 100 rad/s), sans puis avec
un pôle de filtrage ajouté en wf = 10 w2 (proposition du corrigé, pas du sujet).
Régénérer : python ann-2014-cl-sensibilite.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
w0p, w0, wu = 100.0, 10.0, 100.0
a = 6.890
w1, w2 = wu / np.sqrt(a), wu * np.sqrt(a)
C0 = 3.829
wf = 10 * w2
w = np.logspace(-1, 5, 2000); p = 1j * w
G = w0p / (p * (1 + p / w0))
C = C0 * (1 + p / w1) / (1 + p / w2)
Cf = C / (1 + p / wf)
S, Sf = C / (1 + C * G), Cf / (1 + Cf * G)
assert abs(abs(S[-1]) - C0 * a) < 0.1
fig, ax = plt.subplots(figsize=(6.4, 3.2))
ax.semilogx(w, 20 * np.log10(abs(S)), color="#2B4C9B", lw=1.5, label="régulateur de la question 2")
ax.semilogx(w, 20 * np.log10(abs(Sf)), "--", color="#7E889B", lw=1.5,
            label=f"avec un pôle de filtrage en $\\omega_f = 10\\,\\omega_2 \\approx {wf:.0f}$ rad/s (ajouté)")
ax.axhline(20 * np.log10(C0 * a), color="k", lw=0.6, ls=":")
ax.text(0.15, 20 * np.log10(C0 * a) + 2, "$C_0\\,\\omega_2/\\omega_1 \\approx 26{,}4$ (28,4 dB)", fontsize=9)
ax.axvline(wu, color="#7E889B", ls=":", lw=0.9)
ax.set_xlabel("pulsation $\\omega$ (rad/s)"); ax.set_ylabel("$|U(j\\omega)/E(j\\omega)|$ (dB)")
ax.set_ylim(-60, 40); ax.grid(alpha=0.25, which="both"); ax.spines[["top", "right"]].set_visible(False)
ax.legend(fontsize=8, frameon=False, loc="lower right")
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
