---
id: ESP-001
titulo: "Verificar cambios antes de producción"
version: 1.1.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 08_casos_practicos
etiquetas: [despliegue, pruebas, control-de-cambios]
---

# Verificar cambios antes de producción

**Para qué sirve:** Controlar cambios de un sitio o aplicación en un entorno de prueba sin tocar producción.

**Campos a personalizar:** `[REPOSITORIO]`, `[CAMBIO]`, `[URL_PREVIEW]`, `[RUTAS]`, `[CRITERIOS_PUBLICACION]`

## Prompt listo para copiar

Revisa de forma segura un cambio técnico antes de publicarlo. Repositorio o código autorizado: [REPOSITORIO]. Cambio propuesto: [CAMBIO]. Entorno de prueba: [URL_PREVIEW]. Rutas o funciones críticas: [RUTAS]. Criterios obligatorios: [CRITERIOS_PUBLICACION].

Recupera los requisitos y decisiones únicamente de fuentes disponibles y autorizadas. Confirma la rama, el alcance del cambio y las pruebas automatizadas; verifica las rutas y funciones en el entorno de prueba, incluidas páginas inexistentes, enlaces, recargas y redirecciones. Registra para cada prueba el procedimiento, el resultado esperado, el observado y la evidencia. Si faltan herramientas, da instrucciones reproducibles y marca las comprobaciones como pendientes. No fusiones, publiques ni modifiques producción sin autorización explícita y sin cumplir los criterios de publicación.

## Comprobación del resultado

- ¿El resultado responde al objetivo con datos reales y verificables?
- ¿Se distinguen acciones ejecutadas, propuestas, restricciones y pendientes?
- ¿La entrega permite continuar de forma segura y autónoma?
