#!/usr/bin/env bash
# Regenera todas las imágenes del curso en recursos/imagenes/
# Requisitos: graphviz (paquete del sistema) y schemdraw (pip)
set -euo pipefail
cd "$(dirname "$0")"

echo "== Graphviz"
for f in esquemas/graphviz/*.dot; do
  nombre=$(basename "$f" .dot)
  dot -Tsvg "$f" -o "imagenes/${nombre}.svg"
  echo "   imagenes/${nombre}.svg"
done

echo "== schemdraw"
for f in esquemas/schemdraw/[!_]*.py; do
  python3 "$f"
  echo "   $(basename "$f" .py)"
done
