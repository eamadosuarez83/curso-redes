# Recursos gráficos

Todas las imágenes del curso se generan desde código. Así se pueden corregir, versionar en git y regenerar con el mismo estilo.

## Carpetas

| Carpeta | Contenido |
|---|---|
| `esquemas/graphviz/` | Fuentes `.dot`: topologías, flujos entre equipos, tablas de capas, mapas. |
| `esquemas/schemdraw/` | Fuentes `.py`: señales, circuitos, compuertas lógicas, cableado, diagramas de flujo. |
| `imagenes/` | SVG generados. Son los que se enlazan desde los bloques. (Los `.pdf` de al lado los genera `export_pdf.sh` y no se versionan.) |
| `pdf/` | Estilo de la exportación a PDF: filtro `detalles.lua` y ajustes `estilo.tex`. Ver la sección *Exportar a PDF* del [README](../README.md). |

## Cuándo usar cada herramienta

- **Graphviz:** cuando lo importante son las **relaciones** entre cosas: qué se conecta con qué, quién le habla a quién, en qué orden. Graphviz acomoda los nodos solo.
- **schemdraw:** cuando el esquema es **eléctrico o de señales**: formas de onda, circuitos, compuertas lógicas, pines de un conector, o un diagrama de flujo con forma precisa.

## Reglas

1. Toda imagen en `imagenes/` tiene su fuente en `esquemas/` con **el mismo nombre**.
2. Nombres en minúscula, con guion bajo y sin tildes: `resolucion_dns.dot` → `resolucion_dns.svg`.
3. Formato de salida: **SVG** (se ve nítido en GitHub y pesa poco).
4. Paleta común (definida en `esquemas/schemdraw/_comun.py` y repetida en los `.dot`):

   | Uso | Color |
   |---|---|
   | Capas altas, datos, transmisor | morado `#534AB7` |
   | Equipos finales, subredes, resultado correcto | verde `#0F6E56` |
   | Equipos de red (router, switch, AP), fallas | coral `#993C1D` |
   | Estructura, texto secundario | gris `#5F5E5A` |

5. Direcciones de ejemplo según [FILOSOFIA.md](../FILOSOFIA.md): rangos privados o de documentación.

## Generar

```bash
./generar_recursos.sh         # SVG
./generar_recursos.sh --pdf   # SVG + PDF vectorial (lo usa export_pdf.sh)
```

## Inventario

| Imagen | Fuente | Bloque |
|---|---|---|
| `mapa_curso.svg` | graphviz | Estructura |
| `anatomia_comando.svg` | graphviz | 00 |
| `arbol_archivos.svg` | graphviz | 00 |
| `tuberias_redirecciones.svg` | graphviz | 00 |
| `capas_osi_tcpip.svg` | graphviz | 02 |
| `encapsulamiento.svg` | graphviz | 02 |
| `red_domestica.svg` | graphviz | 02 |
| `senal_nrz_manchester.svg` | schemdraw | 03 |
| `cable_utp_t568b.svg` | schemdraw | 03 |
| `par_trenzado_diferencial.svg` | schemdraw | 03 |
| `mascara_and.svg` | schemdraw | 05 |
| `enrutamiento_dos_subredes.svg` | graphviz | 06 |
| `dhcp_dora.svg` | graphviz | 09 |
| `resolucion_dns.svg` | graphviz | 09 |
| `flujo_diagnostico.svg` | schemdraw | 15 |
