"""Máscara de red como operación AND bit a bit.

Ejemplo: último octeto de 192.168.1.57/26.
  IP      57  = 00111001
  Máscara 192 = 11000000
  Red         = 00000000  -> dirección de red 192.168.1.0
"""
import schemdraw
import schemdraw.logic as logic
from _comun import ruta, MORADO, VERDE, CORAL

ip = format(57, "08b")
mascara = format(192, "08b")
red = format(57 & 192, "08b")

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=11, unit=0.6)
    for i in range(8):
        y = -i * 1.3
        g = logic.And(inputs=2).at((0, y)).anchor("in1")
        d += g
        d += logic.Line().at(g.in1).left(0.5).color(MORADO).label(ip[i], loc="left", color=MORADO)
        d += logic.Line().at(g.in2).left(0.5).color(CORAL).label(mascara[i], loc="left", color=CORAL)
        d += logic.Line().at(g.out).right(0.5).color(VERDE).label(red[i], loc="right", color=VERDE)
        d += logic.Line(lw=0).at((g.out[0] + 1.0, g.out[1])).right(0).label(f"bit {7 - i}", loc="right", fontsize=9)
    d += logic.Line(lw=0).at((-2.2, 1.2)).right(0).label("IP: 57 = 00111001", loc="right", color=MORADO)
    d += logic.Line(lw=0).at((-2.2, 0.7)).right(0).label("Máscara: 192 = 11000000", loc="right", color=CORAL)
    d += logic.Line(lw=0).at((-2.2, -10.4)).right(0).label("Red: 00000000 = 0  →  192.168.1.0/26", loc="right", color=VERDE)
    d.save(ruta("mascara_and"))
