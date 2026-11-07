---
id: PROY-001
titulo: "Retomar un proyecto desde el ultimo avance"
version: 1.2.0
estado: evaluacion-parcial
actualizado: 2026-11-06
categoria: 02_gestion_proyectos
etiquetas: [continuidad, proyectos]
---

# Retomar un proyecto desde el ultimo avance

**Para qué sirve:** Continuar trabajos largos sin repetir ni alterar decisiones documentadas.

**Campos a personalizar:** `[PROYECTO]`, `[FUENTES]`, `[OBJETIVO_ACTUAL]`, `[RESTRICCIONES]`

## Prompt listo para copiar

Continúa el proyecto [PROYECTO] a partir del último estado verificable.
Fuentes autorizadas: [FUENTES]. Objetivo de esta sesión: [OBJETIVO_ACTUAL]. Restricciones: [RESTRICCIONES].

Primero recupera decisiones, tareas terminadas, riesgos y dependencias desde las fuentes accesibles. Diferencia lo documentado de lo supuesto. Ejecuta las acciones autorizadas que permitan completar el siguiente bloque de trabajo; verifica sus resultados. No replantees decisiones ya cerradas sin evidencia de un problema. Al finalizar entrega solo: resultado comprobado, cambios realizados, evidencia y siguiente pendiente concreto. No declares sincronización externa si no pudiste guardar o verificar.


### Puerta de acceso obligatoria

Antes de dar resultados, registra qué fuentes pudiste **abrir y leer efectivamente**. Si una fuente se menciona pero no se adjunta o no es accesible, **detén la ejecución** y empieza exactamente con **ESTADO: BLOQUEADO — FUENTES NO DISPONIBLES**. Entrega únicamente: **Fuentes recibidas: NINGUNA o lista real**, **Resultado comprobado: NINGUNO**, **Cambios realizados: NINGUNO**, **Evidencia: NO DISPONIBLE** y **Siguiente paso: proporcionar las fuentes necesarias**. No inventes decisiones previas, rutas revisadas, enlaces reparados, nombres de archivos/capturas, fechas, adjuntos, pruebas ni actualizaciones de bitácoras. Un plan de revisión hipotético puede presentarse por separado bajo el encabezado **PLAN PROPUESTO — NO EJECUTADO**.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
