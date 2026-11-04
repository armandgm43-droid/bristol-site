"""EANA4 TP 5/4 — Schéma petits signaux de l'oscillateur (boucle fermée, R1 négligée, U2 non attaquée).
Reconstruit d'après le schéma de la maquette [poly, p. 66] et le modèle du MOS [poly, p. 60] (Complément).
Nécessite schemdraw (pip install schemdraw)."""
import schemdraw
import schemdraw.elements as elm

schemdraw.config(fontsize=11, font="sans-serif")
BLEU = "#2B4C9B"
with schemdraw.Drawing(file="tp05-schema-petits-signaux.svg", show=False) as d:
    # Entrée de l'inverseur (grille) : Vin = VR
    d += (g := elm.Dot(open=True).label("G (Vin)", "left"))
    d += elm.Gap().down().length(3).label(("+", "$v_{in}$", "−"))
    d += (m0 := elm.Ground())
    # Source de courant commandée gm·vin et Rs
    d += elm.Line().at(g.center).right().length(1.5).color("white")
    d += (n1 := elm.Dot().at((4, 0)))
    d += elm.SourceControlledI().down().length(3).at(n1.center).label("$g_m\\,v_{in}$", "bot")
    d += elm.Ground()
    d += elm.Line().right().length(1.8).at(n1.center)
    d += (n2 := elm.Dot())
    d += elm.Resistor().down().length(3).at(n2.center).label("$R_s$", "bot")
    d += elm.Ground()
    d += elm.Line().right().length(1.8).at(n2.center)
    d += (vout := elm.Dot().label("Vout", "top", ofst=(0.5, 0.15)))
    d += elm.Capacitor().down().length(3).at(vout.center).label("$C_3$", "bot")
    d += elm.Ground()
    # Réseau de retour : r + L1, puis C4
    d += elm.Line().right().length(0.8).at(vout.center)
    d += elm.Resistor().right().label("$r$")
    d += elm.Inductor2(loops=3).right().label("$L_1$")
    d += (vr := elm.Dot().label("VR", "top", ofst=(-0.45, 0.15)))
    d += elm.Capacitor().down().length(3).at(vr.center).label("$C_4$", "bot")
    d += elm.Ground()
    # Rebouclage S2 : VR → Vin
    d += elm.Line().up().length(1.5).at(vr.center).color(BLEU)
    d += elm.Line().tox(g.center).color(BLEU).label("S2 fermé : $v_R = v_{in}$", "top", color=BLEU)
    d += elm.Line().toy(g.center).color(BLEU)
    d += elm.Label().at((5.8, -4.0)).label("inverseur : $g_m = g_{m1} + g_{m2}$,  $R_s = r_{ds}/2$,  $A_v = -g_m R_s$", color="black")
