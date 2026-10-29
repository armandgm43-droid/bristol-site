"""EARF1 ch. 3 — Modulateur d'Armstrong (FM à faible indice).
D'après le support [mod-ana, p. 46], redessinée."""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle
plt.rcParams.update({"font.family": "sans-serif", "font.size": 10, "svg.fonttype": "none"})
B = "#2B4C9B"
fig, a = plt.subplots(figsize=(8, 2.9)); a.set_xlim(0, 10); a.set_ylim(0, 3.6); a.axis("off")
def boite(x, y, w, h, t, fs=10):
    a.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02", fc="white", ec=B, lw=1.4))
    a.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=fs)
def f(p, q, **k): a.annotate("", q, p, arrowprops=dict(arrowstyle="->", lw=1.2), **k)
boite(1.0, 2.2, 1.9, 0.8, "$2\\pi k_f\\int_0^t \\cdot\\,\\mathrm{d}u$", 10)
a.text(1.95, 1.95, "intégrateur", ha="center", fontsize=8, style="italic")
a.add_patch(Circle((4.6, 2.6), 0.32, fc="white", ec="black", lw=1.2)); a.text(4.6, 2.6, "×", ha="center", va="center", fontsize=14)
boite(4.15, 0.9, 0.9, 0.6, "$-\\pi/2$")
a.add_patch(Circle((7.6, 1.8), 0.35, fc="white", ec="black", lw=1.2)); a.text(7.6, 1.8, "Σ", ha="center", va="center", fontsize=13)
f((0.2, 2.6), (1.0, 2.6)); a.text(0.2, 2.8, "$m(t)$")
f((2.9, 2.6), (4.28, 2.6)); a.text(3.3, 2.8, "$\\varphi(t)$")
a.plot([6.0, 9.2], [0.4, 0.4], color="black", lw=1.2); a.text(8.4, 0.05, "$A\\cos(2\\pi f_p t)$", fontsize=9)
a.plot([7.6, 7.6], [0.4, 1.45], color="black", lw=1.2); f((7.6, 1.0), (7.6, 1.45)); a.text(7.75, 1.0, "+", fontsize=11)
a.plot([4.6, 4.6], [0.4, 0.9], color="black", lw=1.2); a.plot([4.6, 6.0], [0.4, 0.4], color="black", lw=1.2)
a.text(5.6, 0.15, "porteuse", fontsize=8, style="italic")
f((4.6, 1.5), (4.6, 2.28)); a.text(4.75, 1.85, "$A\\sin(2\\pi f_p t)$", fontsize=8.5)
a.plot([4.92, 7.6], [2.6, 2.6], color="black", lw=1.2); f((7.6, 2.6), (7.6, 2.15)); a.text(7.75, 2.3, "−", fontsize=12)
a.text(5.3, 2.8, "$A\\,\\varphi(t)\\sin(2\\pi f_p t)$", fontsize=8.5)
f((7.95, 1.8), (9.3, 1.8)); a.text(8.3, 2.0, "$s_{FM}(t)$")
fig.tight_layout(); fig.savefig("03-modulateur-armstrong.svg")
