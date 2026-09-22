"""Por qué el par trenzado rechaza el ruido: señal diferencial.

El transmisor envía +V/2 por un hilo y −V/2 por el otro. El ruido externo
se acopla casi por igual a los dos hilos (modo común). El receptor mide la
DIFERENCIA entre los hilos, así que (ruido cancelado).
El trenzado hace que el acoplamiento sea lo más parecido posible en ambos hilos.
"""
import schemdraw
import schemdraw.elements as elm
from _comun import ruta, CORAL, MORADO, VERDE

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=11)
    G = (0, 1.5)
    # Transmisor diferencial con punto medio a tierra
    d += elm.SourceV().at(G).up().length(1.5).color(MORADO).label("+V/2", loc="bottom")
    A0 = d.here
    d += elm.SourceV().at(G).down().length(1.5).reverse().color(MORADO).label("−V/2", loc="bottom")
    B0 = d.here
    d += elm.Line().at(G).left(0.6)
    d += elm.Ground()
    d += elm.Label().at((0, 3.6)).label("Transmisor", color=MORADO)

    # Los dos hilos del par
    d += elm.Line().at(A0).right(9).color(MORADO).label("hilo A", loc="top")
    A1 = d.here
    d += elm.Line().at(B0).right(9).color(MORADO).label("hilo B", loc="bottom")
    B1 = d.here

    # Ruido acoplado igual a ambos hilos (modo común)
    d += elm.Ground().at((3, 1.5)).right()
    d += elm.SourceSin().at((3, 1.5)).right().length(1.8).color(CORAL).label("ruido (EMI)", loc="bottom", ofst=0.5)
    N = d.here
    d += elm.Capacitor().at(N).up().toy(3).color(CORAL).label("C", loc="bottom")
    d += elm.Capacitor().at(N).down().toy(0).color(CORAL).label("C", loc="bottom")
    d += elm.Dot().at(N).color(CORAL)

    # Receptor diferencial
    op = elm.Opamp(leads=True).right().flip().anchor("center").at((12, 1.5)).color(VERDE)
    d += op
    d += elm.Line().at(A1).toy(op.in2[1]).color(MORADO)
    d += elm.Line().to(op.in2).color(MORADO)
    d += elm.Line().at(B1).toy(op.in1[1]).color(MORADO)
    d += elm.Line().to(op.in1).color(MORADO)
    d += elm.Line().at(op.out).right(0.6).color(VERDE)
    d += elm.Label().at((op.out[0] + 2.9, op.out[1])).label("A − B = V\n(ruido cancelado)", color=VERDE)
    d += elm.Label().at((12, 3.6)).label("Receptor diferencial", color=VERDE)
    d.save(ruta("par_trenzado_diferencial"))
