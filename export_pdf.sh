#!/usr/bin/env bash
# Exporta los bloques del curso (y el libro completo) a PDF.
#
# Mismos parámetros que los cursos hermanos (robotica, curso-control):
# pandoc + LuaLaTeX, clase report, márgenes de 2.5 cm, DejaVu Serif/Sans Mono
# con respaldo Noto Color Emoji. Detalle en README.md, sección "Exportar a PDF".
#
# Requiere: pandoc, TeX Live con lualatex, las fuentes DejaVu + Noto Color
# Emoji, el binario `dot` de Graphviz y un entorno Python con schemdraw y
# matplotlib (.venv/, ver README.md) para regenerar los esquemas.
#
# Uso:
#   ./export_pdf.sh                           # cada bloque por separado + el libro completo
#   ./export_pdf.sh bloque_00_entorno_linux   # solo ese bloque

set -euo pipefail
cd "$(dirname "$0")"

OUT=pdf
mkdir -p "$OUT"

PANDOC_OPTS=(
  --pdf-engine=lualatex
  -V lang=es
  -V geometry:margin=2.5cm
  -V mainfont="DejaVu Serif"
  -V monofont="DejaVu Sans Mono"
  -V mainfontfallback="Noto Color Emoji:mode=harf"
  -V monofontfallback="Noto Color Emoji:mode=harf"
  -V documentclass=report
  --lua-filter=recursos/pdf/detalles.lua
  -H recursos/pdf/estilo.tex
)

# ------------------------------------------------------------------ figuras
# Cada esquema (.dot de Graphviz o .py de schemdraw) se genera como SVG (para
# leer el Markdown en GitHub) y como PDF (vectorial, para LuaLaTeX, que no
# incrusta SVG directamente).
generar_figuras() {
  echo "Generando figuras..."
  ./recursos/generar_recursos.sh --pdf > /dev/null
}

# Sustituye rutas .../imagenes/nombre.svg -> .pdf en una copia temporal, para
# que LuaLaTeX use el vectorial. Devuelve la ruta de la copia por stdout.
preparar_md() {
  local origen="$1"
  local copia
  copia="$(dirname "$origen")/.build-$(basename "$origen")"
  sed 's|\(recursos/imagenes/[A-Za-z0-9_-]*\)\.svg|\1.pdf|g' "$origen" > "$copia"
  echo "$copia"
}

# Los bloques enlazan las imágenes como ../recursos/imagenes/… y los archivos
# de la raíz como recursos/imagenes/…; pandoc resuelve contra su directorio de
# trabajo, así que se le dan ambas bases.
RECURSOS=.:bloques:anexos

exportar_bloque() {
  local archivo="$1"
  local base copia
  base=$(basename "$archivo" .md)
  copia=$(preparar_md "$archivo")
  echo "-> $OUT/$base.pdf"
  pandoc "$copia" -o "$OUT/$base.pdf" \
    --resource-path="$RECURSOS" \
    "${PANDOC_OPTS[@]}"
  rm -f "$copia"
}

generar_figuras

if [ $# -ge 1 ]; then
  for nombre in "$@"; do
    exportar_bloque "bloques/${nombre}.md"
  done
  exit 0
fi

echo "Exportando bloques individuales..."
for f in bloques/bloque_*.md; do
  exportar_bloque "$f"
done

echo "Exportando libro completo..."
COPIAS=()
for f in FILOSOFIA.md ESTRUCTURA.md bloques/bloque_*.md anexos/anexo_*.md; do
  [ -e "$f" ] || continue
  COPIAS+=("$(preparar_md "$f")")
done
pandoc "${COPIAS[@]}" \
  -o "$OUT/curso_redes_completo.pdf" \
  --resource-path="$RECURSOS" \
  --toc \
  "${PANDOC_OPTS[@]}"
rm -f "${COPIAS[@]}"
echo "-> $OUT/curso_redes_completo.pdf"

echo "Listo. PDFs en $OUT/ (carpeta ignorada por git)."
