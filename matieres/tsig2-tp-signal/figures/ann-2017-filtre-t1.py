"""TSIG2, partiel 2017-2018 (groupe 5), ex. 3 — Filtre T1 : y[n] = y[n-1]/8 + y[n-2]/3 + x[n]/3.
Module de la réponse en fréquence ; aux trois fréquences de x (4, 64 et 128/256),
|Y[k]|/|X[k]| mesuré sur les TFD à 256 points (points). Figure calculée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, ROUGE = "#2B4C9B", "#B03A2E"
fn = np.linspace(0, 0.5, 1001); e = np.exp(-2j * np.pi * fn)
H = (1 / 3) / (1 - e / 8 - e**2 / 3)
n = np.arange(256)
x = sum(np.cos(2 * np.pi * k / 256 * n) for k in (4, 64, 128))
y = np.zeros(256)
for i in range(256):
    y[i] = x[i] / 3 + (y[i-1] / 8 if i >= 1 else 0) + (y[i-2] / 3 if i >= 2 else 0)
X, Y = np.fft.fft(x), np.fft.fft(y)
k = np.array([4, 64, 128])
fig, a = plt.subplots(figsize=(7, 3))
a.plot(fn, np.abs(H), color=BLEU, label="$|H(f)|$")
a.plot(k / 256, np.abs(Y[k]) / np.abs(X[k]), "o", color=ROUGE, label="$|Y[k]|/|X[k]|$ (TFD à 256 points)")
a.set_ylim(0, 0.7); a.set_xlabel("Fréquence réduite $f/f_e$"); a.set_ylabel("Gain")
a.legend(fontsize=8); a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("ann-2017-filtre-t1.svg")
