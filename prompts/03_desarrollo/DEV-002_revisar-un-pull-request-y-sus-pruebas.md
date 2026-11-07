---
id: DEV-002
titulo: "Revisar un pull request y sus pruebas"
version: 1.0.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 03_desarrollo
etiquetas: [github, revision]
---

# Revisar un pull request y sus pruebas

**Para qué sirve:** Validar cambios antes de integrarlos.

**Campos a personalizar:** `[REPOSITORIO]`, `[PR]`, `[REQUISITOS]`, `[CONDICIONES]`

## Prompt listo para copiar

Revisa el repositorio [REPOSITORIO], PR [PR], con requisitos [REQUISITOS]. Condiciones de integración: [CONDICIONES].

Examina diff, alcance, seguridad, compatibilidad, pruebas y reportes de CI/CD accesibles. Señala fallas bloqueantes con archivo y evidencia, riesgos secundarios y cambios sugeridos. Verifica que los checks concluyeron satisfactoriamente; si no hay acceso a ellos, repórtalo. No apruebes, fusiones ni despliegues si las condiciones documentadas no se han cumplido o no existe autorización inequívoca. Entrega dictamen: listo, requiere cambios o no verificable.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
