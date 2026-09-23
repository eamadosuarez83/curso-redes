"""Diagrama espacio-tiempo: tiempo de transmisión frente a tiempo de propagación.

El emisor (izquierda) pone los bits en el enlace durante t_tx = L/R. Cada bit
tarda t_prop = d/v en cruzar. El último bit llega en t_tx + t_prop.
"""
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from _comun import ruta, MORADO, VERDE, CORAL, GRIS

t_tx, t_prop = 2.0, 3.0      # unidades arbitrarias, solo proporción
fig, ax = plt.subplots(figsize=(6.2, 4.4))

# Ejes verticales: emisor y receptor. El tiempo corre hacia abajo.
for x, nombre in ((0, "Emisor"), (1, "Receptor")):
    ax.plot([x, x], [0, -(t_tx + t_prop + 0.8)], color=GRIS, lw=1.5)
    ax.text(x, 0.35, nombre, ha="center", fontsize=11, color=GRIS)

# El paquete viaja como una banda inclinada
banda = Polygon([(0, 0), (0, -t_tx), (1, -(t_tx + t_prop)), (1, -t_prop)],
                closed=True, facecolor="#EEEDFE", edgecolor=MORADO, lw=1.2)
ax.add_patch(banda)
ax.text(0.5, -(t_tx / 2 + t_prop / 2), "paquete\n(L bits)", ha="center",
        va="center", color=MORADO, fontsize=10)

# t_tx en el emisor
ax.annotate("", xy=(-0.08, 0), xytext=(-0.08, -t_tx),
            arrowprops=dict(arrowstyle="<->", color=CORAL, lw=1.4))
ax.text(-0.12, -t_tx / 2, "transmisión\n$t_{tx} = L/R$", ha="right",
        va="center", color=CORAL, fontsize=10)

# t_prop del primer bit
ax.annotate("", xy=(1.08, 0), xytext=(1.08, -t_prop),
            arrowprops=dict(arrowstyle="<->", color=VERDE, lw=1.4))
ax.text(1.12, -t_prop / 2, "propagación\n$t_{prop} = d/v$", ha="left",
        va="center", color=VERDE, fontsize=10)

# Llegada del último bit
ax.plot([1, 1.3], [-(t_tx + t_prop)] * 2, color=GRIS, lw=0.8, ls=":")
ax.text(1.12, -(t_tx + t_prop) - 0.35, "llega el último bit:\n$t_{tx} + t_{prop}$",
        ha="left", va="top", color=GRIS, fontsize=10)

ax.text(0.5, 0.05, "distancia d  →", ha="center", va="bottom", fontsize=9, color=GRIS)
ax.text(-0.55, -(t_tx + t_prop + 0.6), "tiempo ↓", fontsize=9, color=GRIS)
ax.set_xlim(-0.9, 1.9)
ax.set_ylim(-(t_tx + t_prop + 1.3), 0.7)
ax.axis("off")
fig.tight_layout()
fig.savefig(ruta("tiempos_transmision_propagacion"))
