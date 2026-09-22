"""Conector RJ45 con cableado T568B y función de cada par en 100BASE-TX.

En 1000BASE-T (Gigabit) los cuatro pares transmiten y reciben a la vez.
"""
import schemdraw
import schemdraw.elements as elm
from _comun import ruta, GRIS

# (pin, color del aislante, color para dibujar, rayado, función en 100BASE-TX)
PINES = [
    (1, "blanco-naranja", "#D85A30", True, "TX+"),
    (2, "naranja", "#D85A30", False, "TX−"),
    (3, "blanco-verde", "#3B6D11", True, "RX+"),
    (4, "azul", "#185FA5", False, "sin uso en 100 Mb/s"),
    (5, "blanco-azul", "#185FA5", True, "sin uso en 100 Mb/s"),
    (6, "verde", "#3B6D11", False, "RX−"),
    (7, "blanco-café", "#712B13", True, "sin uso en 100 Mb/s"),
    (8, "café", "#712B13", False, "sin uso en 100 Mb/s"),
]

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=11, unit=5)
    for i, (pin, nombre, color, rayado, funcion) in enumerate(PINES):
        y = -i * 0.8
        d += elm.Dot(open=True).at((0, y)).label(f"pin {pin}", loc="left")
        estilo = "--" if rayado else "-"
        d += elm.Line(lw=3, ls=estilo).at((0, y)).right(5).color(color).label(nombre, loc="top", fontsize=9)
        d += elm.Dot().color(color).label(funcion, loc="right", fontsize=10)
    d += elm.Label().at((2.5, 1.0)).label("RJ45 (vista frontal, pestaña abajo) · norma T568B", color=GRIS)
    d += elm.Label().at((2.5, -6.4)).label("Punteado = hilo blanco con franja · Gigabit usa los 4 pares", color=GRIS, fontsize=9)
    d.save(ruta("cable_utp_t568b"))
