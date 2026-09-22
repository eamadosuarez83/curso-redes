-- Filtro de pandoc para export_pdf.sh.
-- En GitHub, las respuestas de los ejercicios van plegadas en
-- <details><summary>Título</summary> … </details>. LaTeX descarta ese HTML,
-- así que el título se perdería: aquí se convierte en un párrafo en negrita
-- y se eliminan las etiquetas.
--
-- Pandoc lee ese HTML como bloques sueltos:
--   RawBlock "<details>", RawBlock "<summary>", Plain [título],
--   RawBlock "</summary>", …contenido…, RawBlock "</details>"

local function etiqueta(b, nombre)
  return b.t == "RawBlock" and (b.format == "html" or b.format == "html5")
     and b.text:match("^%s*<" .. nombre .. ">%s*$") ~= nil
end

function Blocks(bloques)
  local salida = {}
  local en_summary = false
  for _, b in ipairs(bloques) do
    if etiqueta(b, "details") or etiqueta(b, "/details") then
      -- se descarta
    elseif etiqueta(b, "summary") then
      en_summary = true
    elseif etiqueta(b, "/summary") then
      en_summary = false
    elseif en_summary and (b.t == "Plain" or b.t == "Para") then
      salida[#salida + 1] = pandoc.Para({ pandoc.Strong(b.content) })
    else
      salida[#salida + 1] = b
    end
  end
  return salida
end
