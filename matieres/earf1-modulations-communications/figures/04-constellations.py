"""EARF1 ch. 4 — Diagrammes de constellation OOK, BPSK, QPSK, 8PSK et 16QAM.
D'après le support [mod-num, p. 12, 15, 18, 21, 22], redessinée (étiquettes binaires du support pour OOK, BPSK et QPSK)."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
B, R = "#2B4C9B", "#B23A3A"
fig, ax = plt.subplots(1, 5, figsize=(11, 2.7))
def axes(a, lim=1.4):
    a.axhline(0, color=B, lw=0.8); a.axvline(0, color=R, lw=0.8)
    a.add_patch(plt.Circle((0, 0), 1, fill=False, ls=":", color="#999"))
    a.set_xlim(-lim, lim); a.set_ylim(-lim, lim); a.set_aspect("equal"); a.axis("off")
    a.text(lim, 0.08, "I", color=B, fontsize=9); a.text(0.06, lim - 0.15, "Q", color=R, fontsize=9)
def pts(a, P, lab=None):
    P = np.array(P); a.plot(P[:, 0], P[:, 1], "o", color="black", ms=4)
    if lab:
        for (x, y), l in zip(P, lab): a.text(x * 1.22, y * 1.22 + (0.12 if y == 0 else 0), l, ha="center", va="center", fontsize=8)
axes(ax[0]); pts(ax[0], [(0, 0), (1, 0)], ["0", "1"]); ax[0].set_title("OOK", fontsize=9)
axes(ax[1]); pts(ax[1], [(1, 0), (-1, 0)], ["0", "1"]); ax[1].set_title("BPSK", fontsize=9)
q = np.sqrt(0.5)
axes(ax[2]); pts(ax[2], [(q, q), (-q, q), (-q, -q), (q, -q)], ["00", "01", "11", "10"]); ax[2].set_title("QPSK (1 symbole = 2 bits)", fontsize=9)
axes(ax[3]); pts(ax[3], [(np.cos(k * np.pi / 4), np.sin(k * np.pi / 4)) for k in range(8)]); ax[3].set_title("8PSK ($\\Delta\\varphi = 45°$)", fontsize=9)
axes(ax[4]); g = np.array([-3, -1, 1, 3]) / (3 * np.sqrt(2))
pts(ax[4], [(x, y) for x in g for y in g]); ax[4].set_title("16QAM (1 symbole = 4 bits)", fontsize=9)
fig.tight_layout(); fig.savefig("04-constellations.svg")
