"""TSIG1 ch. 3 — TFD d'un cosinus, même calcul que l'exemple Matlab des notes [notes, f. 6 v°].
N = 256, Te = 0,01 s, f0 = 10 Hz, FFT sur M = 512 points, axe f_k = k fe / M, k = -M/2 .. M/2-1."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
N, Te, f0, M = 256, 0.01, 10.0, 512
n = np.arange(N)
x = np.cos(2 * np.pi * f0 * n * Te)
X = np.fft.fft(x, M)
f = np.arange(-M // 2, M // 2) / (M * Te)
fig, (a, b) = plt.subplots(1, 2, figsize=(8, 2.8), gridspec_kw={"width_ratios": [2, 1]})
a.plot(f, np.fft.fftshift(np.abs(X)), color="#2B4C9B", lw=1)
a.set_xlabel("Fréquence $f$ (Hz)"); a.set_ylabel("$|X[k]|$")
a.set_title("Axe complet $[-f_e/2, f_e/2]$", fontsize=10)
m = (f > 8) & (f < 12)
b.plot(f[m], np.fft.fftshift(np.abs(X))[m], "o-", ms=2.5, color="#2B4C9B", lw=1)
b.set_xlabel("Fréquence $f$ (Hz)"); b.set_title("Zoom autour de $f_0$", fontsize=10)
for ax in (a, b):
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("03-tfd-cosinus.svg")
