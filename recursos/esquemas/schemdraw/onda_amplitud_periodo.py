"""Onda senoidal con amplitud, periodo y frecuencia señalados.

Ejemplo numérico: f = 2 Hz (T = 0.5 s), amplitud 1 V. Los mismos nombres
sirven para la portadora de Wi-Fi a 2.4 GHz, solo cambia la escala.
"""
import numpy as np
import matplotlib.pyplot as plt
from _comun import ruta, MORADO, VERDE, CORAL, GRIS

f = 2.0            # Hz
T = 1 / f          # s
A = 1.0            # V
t = np.linspace(0, 1.25, 1000)
v = A * np.sin(2 * np.pi * f * t)

fig, ax = plt.subplots(figsize=(7, 3.2))
ax.plot(t, v, color=MORADO, lw=2)
ax.axhline(0, color=GRIS, lw=0.8)

# Amplitud
ax.annotate("", xy=(0.125, A), xytext=(0.125, 0),
            arrowprops=dict(arrowstyle="<->", color=CORAL, lw=1.5))
ax.text(0.14, 0.45, "amplitud A = 1 V", color=CORAL, fontsize=10)

# Periodo, entre dos crestas
ax.annotate("", xy=(0.625, 1.15), xytext=(0.125, 1.15),
            arrowprops=dict(arrowstyle="<->", color=VERDE, lw=1.5))
ax.text(0.375, 1.22, "periodo T = 0.5 s", color=VERDE, fontsize=10, ha="center")
ax.plot([0.125, 0.125], [A, 1.15], color=VERDE, lw=0.8, ls=":")
ax.plot([0.625, 0.625], [A, 1.15], color=VERDE, lw=0.8, ls=":")

ax.text(0.98, -1.3, "frecuencia f = 1/T = 2 Hz (2 ciclos por segundo)",
        color=GRIS, fontsize=10, ha="center")

ax.set_xlabel("tiempo t [s]")
ax.set_ylabel("voltaje v [V]")
ax.set_ylim(-1.45, 1.45)
ax.set_xlim(0, 1.25)
for lado in ("top", "right"):
    ax.spines[lado].set_visible(False)
ax.grid(True, color="#E5E3DC", lw=0.5)
fig.tight_layout()
fig.savefig(ruta("onda_amplitud_periodo"))
