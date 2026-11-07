---
id: INV-002
titulo: "Comparar opciones con criterios ponderados"
version: 1.1.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 01_investigacion
etiquetas: [investigacion, comparacion]
---

# Comparar opciones con criterios ponderados

**Para qué sirve:** Tomar decisiones transparentes sin esconder supuestos.

**Campos a personalizar:** `[OPCIONES]`, `[CRITERIOS]`, `[PRIORIDADES]`, `[CONTEXTO]`

## Prompt listo para copiar

Compara estas opciones: [OPCIONES], en el contexto de [CONTEXTO].
Criterios: [CRITERIOS]. Prioridades relativas: [PRIORIDADES].

Define una tabla con criterios, evidencia, ventajas, desventajas, costos/riesgos y una valoración cualitativa fundamentada. Si faltan precios o condiciones actuales, compruébalos con fuentes disponibles o márcalos como pendientes. No asignes puntos numéricos arbitrarios si no hay ponderaciones acordadas. Termina con recomendación condicionada y el dato que más podría cambiarla.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
