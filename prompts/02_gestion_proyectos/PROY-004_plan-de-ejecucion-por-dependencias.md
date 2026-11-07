---
id: PROY-004
titulo: "Plan de ejecucion por dependencias"
version: 1.3.0
estado: probado-manualmente-no
actualizado: 2026-11-07
categoria: 02_gestion_proyectos
etiquetas: [planificacion, ejecucion]
---

# Plan de ejecucion por dependencias

**Para qué sirve:** Transformar un objetivo grande en entregas comprobables.

**Campos a personalizar:** `[OBJETIVO]`, `[CONTEXTO]`, `[RECURSOS]`, `[FECHA]`

## Prompt listo para copiar

Objetivo: [OBJETIVO]. Contexto: [CONTEXTO]. Recursos y limitaciones: [RECURSOS]. Fecha objetivo, si aplica: [FECHA].

Divide el trabajo en bloques por dependencia, no en microtareas triviales. Para cada bloque indica resultado usable, prerequisitos, prueba de aceptación, riesgo y alternativa si falla. Identifica la primera acción ejecutable ahora. Evita asignar plazos o capacidades imaginarios; comunica incertidumbre. Prioriza entregas reversibles y fáciles de mantener.

Antes de entregar el plan, comprueba que las dependencias formen un orden ejecutable **sin ciclos**: ningún bloque puede requerir otro posterior que a su vez dependa del primero. Separa validación de enlaces y aprobación del cliente; una aprobación no recibida es **BLOQUEANTE** para publicar. No declares como entregable logrado una web publicada, una aprobación, una fecha ni la satisfacción del cliente sin evidencia. Indica el estado de cada bloque (propuesto, ejecutado o pendiente) y verifica la primera acción que sí se puede realizar ahora. **Un bloque NO está ejecutado por el mero hecho de haberlo descrito en el plan**: si no recibiste evidencia de trabajo realizado, todos los bloques deben figurar PENDIENTES o PROPUESTOS, nunca EJECUTADOS. Comprueba especialmente que el texto, la aprobación y la publicación realmente existen antes de darlos por completados.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
