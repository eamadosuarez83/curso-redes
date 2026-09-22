"""Utilidades compartidas por los esquemas de schemdraw del curso."""
from pathlib import Path

# Todas las imágenes generadas van a recursos/imagenes/
IMAGENES = Path(__file__).resolve().parents[2] / "imagenes"
IMAGENES.mkdir(parents=True, exist_ok=True)

# Paleta del curso (misma que en los esquemas de Graphviz)
MORADO = "#534AB7"
VERDE = "#0F6E56"
CORAL = "#993C1D"
GRIS = "#5F5E5A"
AMBAR = "#854F0B"


def ruta(nombre: str) -> str:
    """Devuelve la ruta de salida para una imagen SVG."""
    return str(IMAGENES / f"{nombre}.svg")
