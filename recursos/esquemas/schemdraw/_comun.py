"""Utilidades compartidas por los esquemas de schemdraw del curso."""
import os
from pathlib import Path

import matplotlib

# Salida reproducible: sin fijar la sal de los IDs internos ni la fecha de los
# metadatos, cada corrida cambia el SVG aunque la figura sea idéntica, y git
# lo marca como modificado.
matplotlib.rcParams["svg.hashsalt"] = "curso-redes"
os.environ.setdefault("SOURCE_DATE_EPOCH", "0")

# Todas las imágenes generadas van a recursos/imagenes/
IMAGENES = Path(__file__).resolve().parents[2] / "imagenes"
IMAGENES.mkdir(parents=True, exist_ok=True)

# Formato de salida: SVG para GitHub (por defecto). export_pdf.sh vuelve a
# correr cada script con FORMATO=pdf, porque LuaLaTeX no incrusta SVG.
FORMATO = os.environ.get("FORMATO", "svg")

# Paleta del curso (misma que en los esquemas de Graphviz)
MORADO = "#534AB7"
VERDE = "#0F6E56"
CORAL = "#993C1D"
GRIS = "#5F5E5A"
AMBAR = "#854F0B"


def ruta(nombre: str) -> str:
    """Devuelve la ruta de salida para una imagen (SVG, o PDF si FORMATO=pdf)."""
    return str(IMAGENES / f"{nombre}.{FORMATO}")
