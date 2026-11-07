# Fuentes verificadas independientemente — formación del arcoíris

**Fecha de consulta independiente:** 7 de noviembre de 2026.  
**Ámbito:** ejemplo científico de los prompts `INV-001` e `INV-003`.  
**Método:** apertura y lectura directa de las páginas institucionales, por separado de las conversaciones de Duck.ai. La comprobación se hizo desde las herramientas de investigación de este proyecto, **no mediante el modelo evaluado**.

## Fuentes originales consultadas

| Organismo | Página y dirección consultada | Hallazgo comprobado | Limitación |
|---|---|---|---|
| NOAA / National Weather Service (Estados Unidos) | [How Do Rainbows Form?](https://www.weather.gov/fgz/Rainbow) | La luz se refracta al entrar y salir de la gota; una parte se refleja en la superficie interna. El arco primario requiere una reflexión interna; el secundario, dos. | Página educativa sin fecha explícita de publicación en el contenido consultado; no es un registro de navegación de un modelo de IA. |
| Met Office (Reino Unido) | [Rainbows: optical wonders](https://weather.metoffice.gov.uk/learn-about/weather/optical-effects/rainbows) | Describe la refracción, la separación de colores, la reflexión interna y el efecto de la posición del Sol y el observador. | Página divulgativa sin fecha de publicación explícita en el contenido consultado. |
| NASA Science (Estados Unidos) | [A Full Circle Rainbow over Norway](https://science.nasa.gov/image-article/apod-2022-december-27-a-full-circle-rainbow-over-norway/) | La reflexión interna en las gotas y la posición relativa del observador explican por qué un arcoíris puede aparecer como un círculo completo. | Publicación de 27 de diciembre de 2022; apoya el fenómeno general, no documenta visitas a sitios por asistentes de IA. |

## Resultado contrastado

Para el arcoíris primario, el modelo físico combina **refracción de la luz, dispersión de colores y reflexión interna de una parte de la luz dentro de las gotas**. No es correcto exigir que esa reflexión sea siempre **reflexión interna total**. Las páginas verificadas respaldan esta distinción general; los detalles de trayectorias, índices o ángulos específicos deben verificarse contra la fuente de cada afirmación.

## Qué NO se verificó

- Las respuestas de Mistral Small 4 y GPT-5.4 mini que *afirmaron* consultar páginas no cuentan con una traza independiente que identifique qué páginas abrió efectivamente cada modelo. Por eso sus dictámenes históricos permanecen como **parciales**.
- Verificar que una fuente institucional existe y explica un fenómeno **no prueba** que el modelo la haya abierto o leído.
- No se reprodujeron experimentos de óptica, no se alteraron sus publicaciones y no se realizaron pruebas adicionales de los otros 29 prompts.

## Protocolo reproducible para futuras verificaciones

1. Registrar la afirmación exacta y su origen; diferenciar lo observado de la afirmación del modelo.
2. Abrir desde una herramienta independiente la **URL concreta** citada; anotar URL final, título y fecha de consulta.
3. Comparar el contenido accesible con cada afirmación. Marcarla «corroborada», «contradicha» o «no comprobable».
4. Si es relevante evaluar **si un modelo realmente navegó**, exigir traza de herramientas o registro externo del acceso. No inferir navegación porque incluya una URL o describa una página.
5. Conservar resultados y limitaciones sin reescribir retrospectivamente los dictámenes históricos.

Ver también [evaluaciones empíricas](EVALUACIONES_REALES.md) y [limitaciones](PRUEBAS_Y_LIMITACIONES.md).
