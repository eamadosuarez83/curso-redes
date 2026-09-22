#!/usr/bin/env bash
# Regenera todas las imágenes del curso en recursos/imagenes/
# Requisitos: graphviz (paquete del sistema) y schemdraw (pip, en .venv/)
#
# Uso:
#   ./generar_recursos.sh        # solo SVG (los que se versionan y ve GitHub)
#   ./generar_recursos.sh --pdf  # además PDF vectorial, para export_pdf.sh
set -euo pipefail
cd "$(dirname "$0")"

PDF=0
[ "${1:-}" = "--pdf" ] && PDF=1

# Python del entorno virtual del proyecto si existe; si no, el del sistema.
PY="$(command -v python3)"
[ -x ../.venv/bin/python ] && PY="$(cd .. && pwd)/.venv/bin/python"

echo "== Graphviz"
for f in esquemas/graphviz/*.dot; do
  nombre=$(basename "$f" .dot)
  dot -Tsvg "$f" -o "imagenes/${nombre}.svg"
  [ "$PDF" = 1 ] && dot -Tpdf "$f" -o "imagenes/${nombre}.pdf"
  echo "   imagenes/${nombre}.svg"
done

echo "== schemdraw ($PY)"
for f in esquemas/schemdraw/[!_]*.py; do
  "$PY" "$f"
  [ "$PDF" = 1 ] && FORMATO=pdf "$PY" "$f"
  echo "   $(basename "$f" .py)"
done
