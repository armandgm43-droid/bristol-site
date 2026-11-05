"""TSIG2, partiel 2017-2018 (groupe 7), ex. 1 — TFD d'un cosinus de période 30,5
échantillons observé sur M = 256 échantillons : TFD sur 256 points (points) et sur
2048 points (trait), fréquence vraie en pointillés. Figure calculée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU, ROUGE = "#2B4C9B", "#B03A2E"
M = 256; f0 = 1 / 30.5
x = np.cos(2 * np.pi * f0 * np.arange(M))
X1 = np.abs(np.fft.fft(x, M)); X2 = np.abs(np.fft.fft(x, 2048))
fig, a = plt.subplots(figsize=(7, 3.2))
a.plot(np.arange(2048) / 2048, X2, color=BLEU, lw=1, label="TFD sur 2048 points")
a.plot(np.arange(M) / M, X1, "o", color=ROUGE, ms=4, label="TFD sur N = M = 256 points")
a.axvline(f0, color="#7E889B", ls=":", lw=1)
a.set_xlim(0, 0.08)
a.set_xlabel("Fréquence réduite $f/f_e$"); a.set_ylabel("Module de la TFD")
a.legend(fontsize=8); a.spines[["top", "right"]].set_visible(False)
fig.tight_layout(); fig.savefig("ann-2017-tfd-fenetrage.svg")
