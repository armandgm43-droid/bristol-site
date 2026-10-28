"""Partiel AU201 du 13 janvier 2017, question 4 : diagramme asymptotique de gain de la
transmittance en régulation S/Ps = 1/(1 + beta) = (1 + p/w0) / ((1 + K G0)(1 + p/w0')),
w0' = (1 + K G0) w0 ; G0 = 10, w0 = 1 rad/s, K = 10 pour l'exemple (non donné par le sujet).
Courbe réelle en trait plein, asymptotes en pointillés. Régénérer : python ann-2016-cl-regulation.py"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
G0, w0, K = 10.0, 1.0, 10.0
w0p = (1 + K * G0) * w0
w = np.logspace(-2, 4, 2000); p = 1j * w
T = (1 + p / w0) / ((1 + K * G0) * (1 + p / w0p))
g0 = -20 * np.log10(1 + K * G0)
asym = np.where(w < w0, g0, np.where(w < w0p, g0 + 20 * np.log10(w / w0), 0.0))
fig, ax = plt.subplots(figsize=(6.4, 3.4))
ax.semilogx(w, 20 * np.log10(abs(T)), color="#2B4C9B", lw=1.5, label="gain réel")
ax.semilogx(w, asym, "--", color="#7E889B", lw=1.3, label="diagramme asymptotique")
for x, lab in ((w0, "$\\omega_0$"), (w0p, "$\\omega_0' \\approx K G_0\\,\\omega_0$")):
    ax.axvline(x, color="k", ls=":", lw=0.7); ax.text(x * 1.15, -45, lab, fontsize=9)
ax.text(0.012, g0 + 2.5, "$-20\\log(1 + K G_0) \\approx -40$ dB", fontsize=9)
ax.text(5, -18, "+20 dB/déc", fontsize=9, rotation=0)
ax.text(500, 2.5, "0 dB : plus de rejet", fontsize=9)
ax.set_ylim(-50, 10)
ax.set_xlabel("pulsation $\\omega$ (rad/s)"); ax.set_ylabel("$|S(j\\omega)/P_s(j\\omega)|$ (dB)")
ax.grid(alpha=0.25, which="both"); ax.spines[["top", "right"]].set_visible(False)
ax.legend(fontsize=8, frameon=False, loc="upper left", bbox_to_anchor=(0.0, 0.85))
fig.tight_layout(); fig.savefig(__file__.replace(".py", ".svg"))
