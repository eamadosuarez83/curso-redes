"""Diagrama de flujo de diagnóstico de red, de abajo hacia arriba por capas."""
import schemdraw
import schemdraw.flow as flow
from _comun import ruta, CORAL, VERDE

PREGUNTAS = [
    ("¿Hay enlace físico?\n(luces, ip link)", "Capa 1-2: cable, conector,\npuerto, Wi-Fi, SSID/clave"),
    ("¿Tiene IP y máscara\nválidas? (ip addr)", "DHCP: servidor, concesión,\no IP fija mal escrita"),
    ("¿Responde la puerta\nde enlace? (ping)", "Red local: gateway mal\nconfigurado, VLAN, ARP"),
    ("¿Responde una IP\nexterna? (ping 1.1.1.1)", "Router, NAT o\nproveedor (ISP)"),
    ("¿Resuelve nombres?\n(dig ejemplo.co)", "DNS: resolv.conf,\nservidor DNS caído"),
]

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=10, unit=0.6)
    d += flow.Start(w=3.2, h=1.2).label("Sin conexión")
    for pregunta, causa in PREGUNTAS:
        d += flow.Arrow().down(d.unit)
        dec = d.add(flow.Decision(w=4.6, h=2.2, E="No", S="Sí").label(pregunta))
        d += flow.Arrow().at(dec.E).right(1.2)
        d += flow.Box(w=4.6, h=1.3).anchor("W").label(causa).color(CORAL)
        d.here = dec.S
    d += flow.Arrow().down(d.unit)
    d += flow.Terminal(w=5.2, h=1.3).label("Capas 4-7: puerto, firewall,\nservicio o aplicación").color(VERDE)
    d.save(ruta("flujo_diagnostico"))
