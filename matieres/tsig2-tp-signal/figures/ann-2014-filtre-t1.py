"""TSIG2, partiel 2014-2015, ex. 2 — Filtre T1 : pôles et zéros, réponse impulsionnelle,
module de la réponse en fréquence. Figure calculée à partir de l'équation (1) du sujet."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, ROUGE = "#2B4C9B", "#B03A2E"
b = np.array([1/4, 3/4, 1/2]); a = np.array([1, -1/5, -1/5])
z, p = np.roots(b), np.roots(a)
N = 15; h = np.zeros(N)
for n in range(N):
    h[n] = (b[n] if n < 3 else 0) + (h[n-1] / 5 if n >= 1 else 0) + (h[n-2] / 5 if n >= 2 else 0)
fn = np.linspace(0, 0.5, 501); e = np.exp(-2j * np.pi * fn)
H = (b[0] + b[1] * e + b[2] * e**2) / (a[0] + a[1] * e + a[2] * e**2)
fig, ax = plt.subplots(1, 3, figsize=(10, 3.2))
t = np.linspace(0, 2 * np.pi, 400)
ax[0].plot(np.cos(t), np.sin(t), color="k", lw=0.6)
ax[0].plot(z.real, z.imag, "o", mfc="none", color=BLEU, ms=8, label="zéros")
ax[0].plot(p.real, p.imag, "x", color=ROUGE, ms=8, label="pôles")
ax[0].axhline(0, color="k", lw=0.4); ax[0].axvline(0, color="k", lw=0.4)
ax[0].set_aspect("equal"); ax[0].set_xlim(-2.4, 1.4); ax[0].set_ylim(-1.3, 1.3)
ax[0].set_xlabel("Partie réelle"); ax[0].set_ylabel("Partie imaginaire")
ax[0].legend(fontsize=8, loc="upper left")
ax[1].stem(np.arange(N), h, linefmt=BLEU, markerfmt="o", basefmt="k-")
ax[1].stem([0], [1], linefmt="#7E889B", markerfmt="s", basefmt="k-")
ax[1].set_xlabel("$n$"); ax[1].set_ylabel(r"$\delta[n]$ (gris), $h[n]$ (bleu)")
ax[2].plot(fn, np.abs(H), color=BLEU)
ax[2].set_xlabel("Fréquence normalisée $f/F_e$"); ax[2].set_ylabel(r"$|H(f)|$")
for a_ in ax[1:]:
    a_.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("ann-2014-filtre-t1.svg")
