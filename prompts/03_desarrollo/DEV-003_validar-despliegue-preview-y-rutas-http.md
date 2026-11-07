---
id: DEV-003
titulo: "Validar despliegue preview y rutas HTTP"
version: 1.0.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 03_desarrollo
etiquetas: [cloudflare, http, pruebas]
---

# Validar despliegue preview y rutas HTTP

**Para qué sirve:** Comprobar rutas y comportamiento sin modificar producción.

**Campos a personalizar:** `[URL_PREVIEW]`, `[RUTAS]`, `[COMPORTAMIENTO_ESPERADO]`, `[RAMA]`

## Prompt listo para copiar

Valida un despliegue de prueba (preview): [URL_PREVIEW], rama/commit [RAMA]. Rutas a verificar: [RUTAS]. Comportamiento esperado: [COMPORTAMIENTO_ESPERADO].

Para cada ruta registra URL exacta, código HTTP, redirecciones, contenido/estado final y resultado. Revisa páginas 404, rutas directas, recarga de URLs internas, assets y enlaces internos si están en alcance. Comprueba que el entorno es preview y no producción. Si no tienes acceso de red adecuado, proporciona comandos o pasos reproducibles sin fingir mediciones. No promociones a producción antes de cumplir las pruebas establecidas.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
