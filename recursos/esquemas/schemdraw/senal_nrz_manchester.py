"""Cómo viajan los bits por el cable: NRZ frente a Manchester.

Manchester (IEEE 802.3, usado en Ethernet 10 Mb/s):
  bit 1 -> transición de bajo a alto en la mitad del bit
  bit 0 -> transición de alto a bajo en la mitad del bit
La transición garantizada permite al receptor recuperar el reloj.
"""
import schemdraw
import schemdraw.logic as logic
from _comun import ruta

bits = "10110010"
nrz = "".join(b * 2 for b in bits)                       # cada bit dura 2 medios periodos
manchester = "".join("01" if b == "1" else "10" for b in bits)


def a_wave(s: str) -> str:
    """Convierte '0011' al formato wavedrom '0.1.' (el punto repite el nivel)."""
    salida, previo = [], None
    for c in s:
        salida.append("." if c == previo else c)
        previo = c
    return "".join(salida)


onda = {
    "signal": [
        {"name": "reloj", "wave": "p......."},
        {"name": "datos", "wave": "=" * 8, "data": list(bits)},
        {},
        {"name": "NRZ", "wave": a_wave(nrz)},
        {"name": "Manchester", "wave": a_wave(manchester)},
    ],
}
# La fila de reloj y datos usa 8 periodos; las señales usan 16 medios periodos.
onda["signal"][0]["period"] = 2
onda["signal"][1]["period"] = 2

with schemdraw.Drawing(show=False) as d:
    d += logic.TimingDiagram(onda, ygap=0.5, grid=True)
    d.save(ruta("senal_nrz_manchester"))
