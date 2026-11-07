# Guía de uso y mantenimiento

## Uso

Selecciona una ficha en el catálogo, copia el apartado «Prompt listo para copiar», reemplaza las variables `[CAMPO]` y ejecuta la instrucción. Especifica destinatario, objetivo, restricciones y formato de salida cuando corresponda. Evalúa el resultado con la sección final de la ficha.

## Regla de verificación

No supongas que la herramienta tiene navegación, acceso a archivos, permiso de escritura o capacidad de ejecutar comandos. Si carece de ellos, la instrucción debe generar un plan verificable, no fingir acciones realizadas.

## Práctica con entradas de ejemplo

Consulta [EJEMPLOS_DE_PRUEBA.md](EJEMPLOS_DE_PRUEBA.md) para los 30 ejemplos ficticios y [PRUEBAS_Y_LIMITACIONES.md](PRUEBAS_Y_LIMITACIONES.md) para conocer qué se comprobó y qué no.

## Añadir o revisar prompts

1. Busca posibles duplicados en [CATALOGO.md](CATALOGO.md).
2. Usa [PLANTILLA_DE_PROMPT.md](PLANTILLA_DE_PROMPT.md) y un nuevo ID único.
3. Mantén metadatos, propósito, variables y criterios de comprobación.
4. Explica las restricciones y, cuando corresponda, advierte de riesgos.
5. Documenta cambios relevantes en [CHANGELOG.md](CHANGELOG.md).
6. Antes de compartir, aplica [SECURITY.md](SECURITY.md).

## Versionado

Se utiliza `MAJOR.MINOR.PATCH`: cambios incompatibles, nuevas capacidades y correcciones. `probado-manualmente-no` significa que no se han recopilado resultados de pruebas manuales; no debe cambiarse sin conservar la evidencia del test.

## Licencia

La reutilización de este material se rige por [CC BY 4.0](LICENSE.md), que permite copia y adaptación con atribución, incluida la actividad comercial.


## Evidencia de pruebas con modelos

Consulta [las 23 conversaciones observadas](EVALUACIONES_REALES.md), con resultados favorables y fallos. Sus resultados no garantizan igual calidad en cualquier modelo ni permiten inventar acceso a archivos o plataformas.
