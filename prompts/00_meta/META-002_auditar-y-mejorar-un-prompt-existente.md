---
id: META-002
titulo: "Auditar y mejorar un prompt existente"
version: 1.1.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 00_meta
etiquetas: [meta, calidad]
---

# Auditar y mejorar un prompt existente

**Para qué sirve:** Detectar ambigüedades, redundancia y riesgos sin perder la intención original.

**Campos a personalizar:** `[PROMPT_ORIGINAL]`, `[OBJETIVO]`, `[PROBLEMA]`

## Prompt listo para copiar

Analiza el siguiente prompt con el fin de volverlo más preciso y eficiente.

Prompt original: [PROMPT_ORIGINAL]
Resultado que debería producir: [OBJETIVO]
Problema observado (si existe): [PROBLEMA]

Evalúa claridad, alcance, datos de entrada, comprobabilidad, redundancia, privacidad y dependencia de herramientas. Entrega una versión optimizada completa, una lista de cambios con su motivo y un test breve con un ejemplo de entrada y salida esperada. Conserva restricciones importantes. No prometas ahorro de tokens medido sin datos comparativos.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
