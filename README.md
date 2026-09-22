# Curso de redes desde cero

Curso de redes de computadores en español para estudiantes de ingeniería que no traen conocimientos previos de redes. Parte de lo que sabe un estudiante de tercer semestre (álgebra, física general y uso básico de Linux) y llega hasta diseñar, configurar, asegurar y mantener una red real.

![Red típica](recursos/imagenes/red_domestica.svg)

## Cómo está organizado

- [FILOSOFIA.md](FILOSOFIA.md) — el enfoque del curso y las reglas con que se escribe cada bloque.
- [ESTRUCTURA.md](ESTRUCTURA.md) — el temario completo: 17 bloques y 5 anexos.
- `bloques/` — un archivo Markdown por bloque, más `_plantilla_bloque.md`.

**Por dónde empezar:** [Bloque 00 — Entorno de trabajo en Linux](bloques/bloque_00_entorno_linux.md).
- `anexos/` — glosario, comandos, laboratorio virtual, tablas y estándares.
- `recursos/` — esquemas (fuentes en Graphviz y schemdraw) e imágenes generadas.

## Requisitos para trabajar el curso

Un equipo con Linux. Las herramientas se instalan en el bloque 00.

## Regenerar los esquemas

```bash
# Graphviz desde el gestor de paquetes (apt, pacman, dnf…)
sudo apt install graphviz          # Debian/Ubuntu
sudo pacman -S graphviz            # Arch

python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
./recursos/generar_recursos.sh
```

## Estado

| Parte | Estado |
|---|---|
| Filosofía y temario | Listo |
| Esquemas base | 15 de los previstos |
| Bloque 00 — Entorno Linux | Listo |
| Bloques 01–16 | Por escribir |
| Anexos A–E | Por escribir |
