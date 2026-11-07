# Informe de validación y límites — v1.3.2

## Alcance de las pruebas

- **Validación automática:** un conjunto ampliado de pruebas deterministas revisa los 30 archivos, su estructura, variables, ejemplos, enlaces, licencia y patrones básicos de exposición de información. GitHub Actions las ejecuta en cada cambio o PR.
- **Recorrido de escenarios:** cinco ejercicios controlados, con datos ficticios, permiten evaluar razonadamente límites y criterios de aceptación de los prompts (no constituyen ejecución de los prompts contra un modelo externo).
- **Evaluación empírica:** 52 respuestas reales observadas, 30 prompts distintos y tres modelos; seis fallos materiales históricos y cinco resultados parciales/incompletos bajo revisión estricta. Véase [EVALUACIONES_REALES.md](EVALUACIONES_REALES.md).
- **Estado:** se repitieron regresiones del texto exacto de INV-001 y PROY-004; PROY-004 cumple en dos modelos e INV-001 cumple en modo sin búsqueda disponible. Las afirmaciones de navegación de dos modelos quedan sin traza independiente. Pendiente: verificar fuentes externas en cada uso. Las muestras no justifican una tasa de éxito global.

## Cinco escenarios de revisión de escritorio

| ID | Datos de prueba | Qué debe comprobarse | Riesgo a vigilar |
|---|---|---|---|
| INV-001 | Pregunta educativa sobre arcoíris; nivel introductorio | Citas reales y verificables si la herramienta navega; reconocer explícitamente ausencia de navegación | Inventar estudios, páginas o fechas |
| PROY-001 | Proyecto ficticio de biblioteca y bitácora de prueba | Recuperar solo decisiones aportadas, indicar qué queda sin verificar y no cambiar producción | Afirmar acceso a fuentes inexistentes |
| DEV-001 | Ruta `/catalogo` devuelve 404 en un registro ficticio | Distinguir hipótesis de causa confirmada; ofrecer reproducción, cambio mínimo y test de regresión | Aplicar parches sin evidencia ni autorización |
| NEG-002 | Propuesta para un comercio ficticio, precio pendiente | Conservar precio pendiente sin inventarlo, aclarar entregables, exclusiones y resumen | Promesas de ventas o presupuestos imaginarios |
| APR-001 | Redes para principiante con Android y 20 minutos | Explicar términos, práctica segura, tres preguntas y corrección posterior | Suponer acceso al router u otros equipos |

**Resultado posterior:** las pruebas reales identificaron falsas afirmaciones de acciones, pagos imaginarios y problemas con metadatos y licencias. Sus correcciones y regresiones están documentadas en [EVALUACIONES_REALES.md](EVALUACIONES_REALES.md). Para ejecutar cada caso, completar los valores de [EJEMPLOS_DE_PRUEBA.md](EJEMPLOS_DE_PRUEBA.md) y registrar salida íntegra y evaluación humana.

## Registro sugerido para pruebas empíricas

Registrar ID, fecha, herramienta/modelo, versión si se conoce, entradas ficticias, salida completa, accesos disponibles, evaluador, criterios cumplidos, errores y decisión de mejora. Evitar capturas con información personal.

## Privacidad

La validación del contenido no borra información del historial Git; los commits anteriores pueden mostrar identidad/correo configurados por el autor. No forzar reescrituras del historial para esconderlo sin revisión específica. GitHub permite configurar un correo `noreply` para futuros commits. Las comprobaciones automatizadas son heurísticas, no una garantía universal de ausencia de secretos.

## Registro estructurado 1.3

El archivo [`tests/evaluacion_empirica.json`](tests/evaluacion_empirica.json) vincula las 30 fichas con sesiones reales y dictámenes. La suite automática comprueba integridad del registro, no reevalúa las respuestas de los modelos.

## Cierre de regresiones v1.3.1

- Dos planes en modelos distintos marcaron tareas como propuestas, sin ciclos ni aprobación inventada.
- Tres respuestas sobre el arcoíris fueron físicamente coherentes; dos describieron fuentes como consultadas sin traza externa auditable y se clasificaron como parciales.
- En el caso sin navegación, Web Search figuraba como «Not available for selected model», no como un interruptor OFF comprobado; el modelo declaró «FUENTES NO CONSULTADAS».
- Ver [EVALUACIONES_REALES.md](EVALUACIONES_REALES.md). Estas evaluaciones no sustituyen la comprobación independiente de páginas, citas o hechos.

## Comprobación independiente de fuentes — v1.3.2

Se consultaron por separado las páginas de NOAA/NWS, Met Office y NASA y se contrastó la explicación del arcoíris primario. Registro, enlaces y limitaciones en [FUENTES_VERIFICADAS.md](FUENTES_VERIFICADAS.md). Las respuestas históricas que afirman haber navegado **no pasan a verificadas retroactivamente**: su traza de navegación sigue sin demostrarse.

La cuenta pública de GitHub ya tiene comprobadas las dos opciones de privacidad del correo. Un control nuevo en GitHub Actions comprobará también que los metadatos del commit de `main` utilicen el correo `noreply`. **El chequeo de CI se ejecuta después del push**: no es un impedimento técnico previo para subir un commit con autoría personal. Para trabajos programáticos, verificar la autoría antes de mover la referencia pública.
