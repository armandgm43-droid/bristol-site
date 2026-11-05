"""TSIG2, partiel 2016-2017, ex. 1 — Signal DTMF : module de la TFD (N = 4096) de la
touche 5 (M = 700, Fe = 8000 Hz), et spectrogramme de la séquence 05 05 77 75 57
(M zéros entre chaque paire de chiffres). Figure calculée."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
BLEU = "#2B4C9B"
Fe, M = 8000, 700
n = np.arange(M)
LO = {"1": 697, "2": 697, "3": 697, "4": 770, "5": 770, "6": 770, "7": 852, "8": 852, "9": 852, "0": 941}
HI = {"1": 1209, "4": 1209, "7": 1209, "2": 1336, "5": 1336, "8": 1336, "0": 1336, "3": 1477, "6": 1477, "9": 1477}
ton = lambda c: np.cos(2 * np.pi * LO[c] * n / Fe) + np.cos(2 * np.pi * HI[c] * n / Fe)
X = np.abs(np.fft.fft(ton("5"), 4096)); f = np.arange(4096) * Fe / 4096
morceaux = []
for paire in "05 05 77 75 57".split():
    morceaux += [ton(c) for c in paire] + [np.zeros(M)]
s = np.concatenate(morceaux[:-1])
fig, ax = plt.subplots(1, 2, figsize=(10, 3.4), gridspec_kw={"width_ratios": [1, 1.3]})
ax[0].plot(f[:2048], X[:2048], color=BLEU, lw=0.9)
ax[0].set_xlim(500, 1600)
ax[0].set_xlabel("Fréquence (Hz)"); ax[0].set_ylabel("$|X[k]|$")
ax[0].set_title("Touche 5 : TFD sur N = 4096 points", fontsize=10, loc="left")
ax[0].spines[["top", "right"]].set_visible(False)
ax[1].specgram(s, NFFT=256, Fs=Fe, noverlap=192, window=np.hanning(256), cmap="Blues", scale="dB", vmin=-60)
ax[1].set_ylim(0, 2000)
for fr in (697, 770, 852, 941, 1209, 1336, 1477):
    ax[1].axhline(fr, color="#7E889B", ls=":", lw=0.6)
ax[1].set_xlabel("Temps (s)"); ax[1].set_ylabel("Fréquence (Hz)")
ax[1].set_title("Spectrogramme de 05 05 77 75 57", fontsize=10, loc="left")
fig.tight_layout(); fig.savefig("ann-2016-dtmf.svg")
