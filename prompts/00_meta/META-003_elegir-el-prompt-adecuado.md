---
id: META-003
titulo: "Elegir el prompt adecuado"
version: 1.1.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 00_meta
etiquetas: [meta, catalogo]
---

# Elegir el prompt adecuado

**Para qué sirve:** Seleccionar una plantilla existente o identificar dónde falta una.

**Campos a personalizar:** `[TAREA]`, `[INVENTARIO]`, `[RESTRICCIONES]`

## Prompt listo para copiar

Tarea a realizar: [TAREA]
Inventario de prompts disponibles (IDs, títulos o enlaces): [INVENTARIO]
Restricciones: [RESTRICCIONES]

Encuentra el prompt de menor complejidad que resuelva la tarea. Indica ID, motivo, variables por completar y un ejemplo listo para usar. Si no hay coincidencia razonable, propón una nueva entrada con ID provisional, categoría y diferencias frente a las existentes; no declares que ya existe. Evita duplicar instrucciones que un protocolo global ya garantiza.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
