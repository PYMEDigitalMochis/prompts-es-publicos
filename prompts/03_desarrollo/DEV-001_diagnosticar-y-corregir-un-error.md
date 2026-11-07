---
id: DEV-001
titulo: "Diagnosticar y corregir un error"
version: 1.1.0
estado: probado-manualmente-no
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

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
