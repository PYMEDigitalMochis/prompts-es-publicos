---
id: DEV-001
titulo: "Diagnosticar y corregir un error"
version: 1.2.0
estado: evaluacion-parcial
actualizado: 2026-11-06
categoria: 03_desarrollo
etiquetas: [debug, codigo]
---

# Diagnosticar y corregir un error

**Para qué sirve:** Depurar con reproducción, causa comprobada y prueba de regresión.

**Campos a personalizar:** `[SINTOMA]`, `[REPRODUCCION]`, `[ENTORNO]`, `[CODIGO]`

## Prompt listo para copiar

Diagnostica el siguiente error: [SINTOMA]. Pasos para reproducirlo: [REPRODUCCION]. Entorno: [ENTORNO]. Código/logs/evidencia: [CODIGO].

Formula hipótesis ordenadas por probabilidad e impacto, indica qué observación confirmaría cada una y analiza los archivos disponibles. Propón el cambio mínimo que corrija la causa demostrada. Si puedes editar código con autorización, trabaja en una rama o copia, no en producción; agrega o ejecuta pruebas apropiadas, verifica regresiones y documenta resultados reales. Si faltan evidencias, no presentes una hipótesis como causa confirmada.


### Puerta de evidencia obligatoria

Antes de formular un diagnóstico, especifica si has recibido y abierto **archivos reales, configuración y registros verificables**. Un log descrito como ficticio NO es evidencia de una ejecución real. Si no tienes pruebas reales, comienza exactamente con **ESTADO: NO VERIFICADO**, trata todas las causas como hipótesis condicionales y responde con los campos **Hipótesis**, **Prueba que las distinguiría**, **Evidencia faltante**, **Cambios realizados: NINGUNO**, **Pruebas ejecutadas: NINGUNA**. No inventes rutas existentes, fragmentos de archivos inspeccionados, diffs, resultados de pruebas, cambios aplicados, ni mensajes de que algo ya funciona. Puedes dar ejemplos de configuración solo si están rotulados **EJEMPLO NO APLICADO**. Solo cambia el estado a **VERIFICADO** tras identificar evidencia obtenida y pruebas efectivamente realizadas.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
