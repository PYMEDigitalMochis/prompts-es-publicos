# Informe de validación y límites — v1.2.0

## Alcance de las pruebas

- **Validación automática:** un conjunto de 14 pruebas deterministas revisa los 30 archivos, su estructura, variables, ejemplos, enlaces, licencia y patrones básicos de exposición de información. GitHub Actions las ejecuta en cada cambio o PR.
- **Recorrido de escenarios:** cinco ejercicios controlados, con datos ficticios, permiten evaluar razonadamente límites y criterios de aceptación de los prompts (no constituyen ejecución de los prompts contra un modelo externo).
- **Evaluación empírica:** 23 conversaciones reales, nueve prompts y tres modelos diferentes, con cuatro fallos iniciales y ocho regresiones posteriores aprobadas. Véase [EVALUACIONES_REALES.md](EVALUACIONES_REALES.md).
- **Pendiente:** realizar pruebas empíricas de los 21 prompts restantes y verificar de forma independiente todas las fuentes. Las muestras no justifican una tasa de éxito global.

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
