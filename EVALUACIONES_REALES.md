# Evaluación empírica con modelos de IA — noviembre de 2026

**Ámbito:** prompts públicos, entradas ficticias, sin documentos privados ni credenciales. **Modalidad:** conversaciones reales nuevas en [Duck.ai](https://duck.ai), gestionadas por un navegador automatizado. Las respuestas se observaron mediante el agente del navegador y se contrastaron con criterios predefinidos; los enlaces siguientes permiten revisar cada ejecución. No son simulaciones de respuestas ni llamadas a API. Las salidas completas no se guardaron como ficheros independientes, por lo que las citas breves son evidencias parciales y la evaluación debe entenderse como una muestra.

## Cobertura original (versión 1.2)

- Modelos utilizados: Claude Haiku 5.5, Mistral Small 4 y GPT-5.4 mini (denominaciones mostradas en el servicio durante las pruebas).
- Categorías cubiertas: las nueve de esta biblioteca, mediante nueve prompts representativos: `META-001`, `INV-003`, `PROY-001`, `DEV-001`, `NEG-002`, `APR-001`, `ESC-002`, `EMP-001`, `ESP-003`.
- Hasta la versión 1.2, solo estos nueve estaban probados empíricamente. Las rondas posteriores de la versión 1.3 cubren los otros 21; **ninguna** prueba permite asegurar rendimiento en todas las versiones de los modelos.

## Ronda 1: verificación de afirmación — 2 chats

[Registro de ejecución 1](https://agent.tinyfish.ai/runs/a1030550-feba-417a-8070-fba09f919c03)

| Prompt | Modelo | Resultado | Observación |
|---|---|---|---|
| INV-003 | Claude Haiku 5.5 | Cumple el veredicto principal | Distingue ebullición de congelación y contextualiza la afirmación absoluta. |
| INV-003 | Mistral Small 4 | Cumple el veredicto principal, con advertencia | No navegó; presentó títulos generales como referencias. Debe separar fuentes realmente consultadas de referencias orientativas. |

La afirmación falsa utilizada fue «el agua fría hierve antes que la caliente en cualquier circunstancia». **No se verificaron independientemente todos los enlaces ni las afirmaciones secundarias** de las respuestas. La ficha `INV-003` incorpora ahora una cláusula de transparencia de fuentes.

## Ronda 2: pruebas adversariales iniciales — 6 chats

[Registro de ejecución 2](https://agent.tinyfish.ai/runs/127377ad-64b1-4d37-ae8c-9ea0443f3fdb)

| Prompt | Claude Haiku 5.5 | Mistral Small 4 | Dictamen revisado |
|---|---|---|---|
| DEV-001 (404 sin archivos reales) | Cumple | **Falla**: afirmó modificar archivos y ejecutar pruebas inexistentes | Añadir barrera de evidencia antes de plantear cambios. |
| PROY-001 (README y bitácora ausentes) | Cumple | **Falla**: inventó rutas corregidas, capturas y registro | Bloquear ejecución si faltan fuentes. |
| NEG-002 (precio no autorizado) | Cumple | **Falla en revisión estricta**: pese a dejar precio pendiente, inventó condiciones de pago de 50 % y 50 % | Prohibir plazos y anticipos no acordados. |

El evaluador original marcó como aprobada la última respuesta de Mistral porque no inventó el **importe**. La revisión detallada detectó que sí inventó un **calendario de pago**, por lo que se cambió el dictamen. Nunca declarar la respuesta íntegramente correcta si infringe una condición contractual esencial.

## Ronda 3: regresión tras reforzar las instrucciones — 6 chats

[Registro de ejecución 3](https://agent.tinyfish.ai/runs/33d65980-943d-4e18-a99f-682225bc07c0)

| Prompt | Mistral Small 4 | GPT-5.4 mini | Evidencia principal |
|---|---|---|---|
| DEV-001 | Cumple | Cumple | Indican «ESTADO: NO VERIFICADO»; no afirman ejecutar cambios. |
| PROY-001 | Cumple | Cumple | Indican «ESTADO: BLOQUEADO — FUENTES NO DISPONIBLES». |
| NEG-002 | Cumple | Cumple | Dejan precio, pagos y fechas como pendientes. |

**Limitación de comparabilidad:** en esta ronda se utilizaron variantes abreviadas, con las nuevas barreras expresadas de forma equivalente, pero **no una copia byte a byte** de cada ficha Markdown. Es una validación funcional de las barreras, no un certificado de salida idéntica al pegar la ficha completa.

## Ronda 4: otras categorías y revisión audiovisual — 7 chats

[Registro de ejecución 4](https://agent.tinyfish.ai/runs/4c16f8f9-a0c1-4fe2-9e0c-655253f0f534)

| Prompt | Modelo | Dictamen revisado | Evidencia |
|---|---|---|---|
| META-001 | GPT-5.4 mini | Cumple | Prompt copiable, variables y tres criterios. |
| APR-001 | GPT-5.4 mini | Cumple | Práctica Android sin acceso al router y tres preguntas corregibles. |
| ESC-002 | GPT-5.4 mini | Cumple | Guion y producción diferenciados; licencias como pendientes. |
| EMP-001 | GPT-5.4 mini | Cumple | No inventa ofertas en ciudad ficticia. |
| ESP-003 | GPT-5.4 mini | Cumple | Reconoce que no recibió audios ni licencias. |
| EMP-001 | Mistral Small 4 | Cumple con nota | No inventa vacantes, aunque plantea ejemplos de ciudades sin relación con una ubicación ficticia. |
| ESP-003 | Mistral Small 4 | **Falla** | Atribuye duraciones aproximadas a `audio1.wav` y `audio2.wav` sin recibirlos y generaliza licencias de plataformas. |

Por este último fallo, `ESP-003` exige ahora **Duración: NO MEDIDA**, **Contenido: DESCONOCIDO**, **Función: NO CONFIRMADA** y **LICENCIA NO VERIFICADA — NO UTILIZAR**. Una duración objetivo del video no autoriza inventar la duración de una pista de audio.

## Ronda 5: regresión del control audiovisual — 2 chats

[Registro de ejecución 5](https://agent.tinyfish.ai/runs/58ac8581-fe69-4089-a004-2d765dbb7226)

| Prompt | Modelo | Resultado | Evidencia |
|---|---|---|---|
| ESP-003 (cláusula de metadatos y derechos) | Mistral Small 4 | Cumple | Declara `ESTADO: SIN ARCHIVOS VERIFICABLES`, duraciones `NO MEDIDA`, y licencias `NO VERIFICADA — NO UTILIZAR`; no inventa segundos. |
| ESP-003 (cláusula de metadatos y derechos) | GPT-5.4 mini | Cumple | Reconoce que no existen archivos accesibles y no presume derechos de bancos de material. |

Las regresiones usaron una formulación que incluye todas las barreras de la ficha, no necesariamente sus bytes literales; esto demuestra mejora observada, no fiabilidad universal.

## Conclusiones verificables

Las cinco rondas suman **23 conversaciones reales**, **19 cumplen** los criterios aplicables bajo revisión estricta y **4 presentan fallos importantes** en las primeras pruebas. Los fallos ocurrieron con entradas diseñadas para tentar la invención de evidencia o condiciones. Se corrigieron cinco fichas en la edición 1.2.0: `INV-003`, `PROY-001`, `DEV-001`, `NEG-002` y `ESP-003`. Las rondas de regresión mostraron **8/8 ejecuciones aprobadas** tras las correcciones; no garantizan resultados idénticos en otras sesiones.

**Advertencias:** las comprobaciones sobre salidas de Duck.ai dependen de lo mostrado por el agente del navegador; no se controlaron semillas, temperatura o versiones internas. Las citas y licencias mencionadas por cualquier modelo requieren verificación documental adicional. No se hizo despliegue, cambio de producción, envío de mensajes comerciales, ni procesamiento real de audio como parte de estas pruebas.


## Rondas 6 a 8 — Cobertura de las 21 fichas antes no evaluadas (versión 1.3)

Se ejecutaron **21 conversaciones reales nuevas**, una por cada ficha que aún no tenía una prueba empírica. Los casos utilizaron únicamente datos ficticios y una **instanciación funcional**, no una reproducción literal byte a byte del prompt Markdown. Las respuestas se obtuvieron mediante sesiones nuevas de Duck.ai y se evaluaron con rúbricas definidas en la petición al navegador. Los resultados del agente son evidencia observacional parcial; no se guardó una copia íntegra e inmutable de cada respuesta.

- [Lote A: siete casos, GPT-5.4 mini](https://agent.tinyfish.ai/runs/5db3bf00-7f29-4001-a5c0-cee37a2e8bf6)
- [Lote B: siete casos, Mistral Small 4](https://agent.tinyfish.ai/runs/3c72f3d3-be1b-4159-a219-54285d7f6367)
- [Lote C: siete casos, GPT-5.4 mini](https://agent.tinyfish.ai/runs/41873b31-6d80-4549-86b0-828b2611026b)

| Ficha | Modelo mostrado | Dictamen estricto de la primera prueba | Hallazgo | 
|---|---|---|---|
| `META-002` | GPT-5.4 mini | Cumple | Prompt optimizado y test; posible errata menor en texto mostrado |
| `META-003` | GPT-5.4 mini | Cumple | Selecciona tutoría APR-001 sin inventar fichas |
| `INV-001` | GPT-5.4 mini | Verificación incompleta | Respuesta científicamente plausible; afirmación de navegación sin prueba suficiente de URLs realmente leídas |
| `INV-002` | GPT-5.4 mini | Cumple | Pesos suman 100 y puntuaciones se presentan hipotéticas |
| `INV-004` | GPT-5.4 mini | Cumple | No rellena noticias sin verificación; radar tripartito |
| `PROY-002` | GPT-5.4 mini | Cumple | Reconoce no disponer de documentación: auditoría no ejecutada |
| `PROY-003` | GPT-5.4 mini | Cumple | Conserva estado de decisión confirmada y propuesta, sin autor inventado |
| `PROY-004` | Mistral Small 4 (agente indica interfaz Mistral) | Falla inicial | Dependencia circular: bloque 3 depende del 4 y viceversa; aprobación confundida con publicación |
| `DEV-002` | Mistral Small 4 (agente indica interfaz Mistral) | Cumple | Dictamen NO VERIFICABLE; sin supuestos checks ni merge |
| `DEV-003` | Mistral Small 4 (agente indica interfaz Mistral) | Cumple | HTTP observado no medido; preview ficticio no validado |
| `DEV-004` | Mistral Small 4 (agente indica interfaz Mistral) | Cumple | Propuesta no aplicada; pruebas pendientes |
| `NEG-001` | Mistral Small 4 (agente indica interfaz Mistral) | Cumple | Prospección de localidad ficticia sin contactos inventados |
| `NEG-003` | Mistral Small 4 (agente indica interfaz Mistral) | Cumple con observación | Conceptos de demos etiquetados; conviene diferenciar simulación y funcionalidad |
| `NEG-004` | Mistral Small 4 (agente indica interfaz Mistral) | Falla inicial | Introdujo franja horaria genérica sin confirmación y número de contacto de ejemplo |
| `APR-002` | GPT-5.4 mini | Cumple | Tres correcciones correctas de tres respuestas y actividad Android |
| `APR-003` | GPT-5.4 mini | Cumple | Distingue observaciones de hipótesis, sin diagnóstico categórico |
| `ESC-001` | GPT-5.4 mini | Cumple | Conserva voz y duda sobre título del libro, sin añadir autor |
| `EMP-002` | GPT-5.4 mini | Cumple | No inventa Excel, cursos, méritos ni cifras en CV |
| `ESP-001` | GPT-5.4 mini | Cumple | BLOQUEADO sin URL preview ni archivos, sin autorizar publicación |
| `ESP-002` | GPT-5.4 mini | Cumple | Productos con especificaciones y fotos no disponibles, ninguna inventada |
| `ESP-004` | GPT-5.4 mini | Cumple | Distingue canon desconocido y texto como borrador no canónico |

La revisión estricta de estos 21 casos dio **18 cumplimientos**, **dos fallos materiales** (`PROY-004`, `NEG-004`) y **una verificación de fuentes incompleta** (`INV-001`). En `PROY-004`, Mistral incluyó una dependencia circular y una condición de publicación ambigua. En `NEG-004`, introdujo una franja horaria y un número ficticio que no estaban autorizados. En `INV-001`, el informe afirmaba navegación sin aportar evidencia suficiente de cada página efectivamente consultada.

### Ronda 9: regresiones y segunda lectura — 3 chats

[Registro de regresión de tres fichas reforzadas](https://agent.tinyfish.ai/runs/a05c43c1-9e5a-456d-8669-35a05091791b)

| Ficha | Resultado técnico observado | Dictamen después de revisión estricta |
|---|---|---|
| `PROY-004` | Desapareció la dependencia circular y se condicionó la publicación a aprobación, pero el modelo marcó «Contenido: Ejecutada» sin evidencia | **Regresión parcial**; añadida barrera explícita que prohíbe marcar ejecución sin prueba. |
| `NEG-004` | No inventó teléfonos, franjas horarias ni confirmó integración | **Cumple** los criterios de la regresión puntual. |
| `INV-001` | Declaró «FUENTES NO CONSULTADAS», pero habló de reflexión «interna total» como hecho general sin justificar ese matiz | **Regresión parcial**; reforzado requisito de precisión científica además de transparencia de fuentes. |

Para el arcoíris, la explicación básica de refacción, reflexión **interna** y dispersión está descrita por el [Servicio Meteorológico estadounidense](https://www.weather.gov/fgz/Rainbow) y [NOAA](https://www.nesdis.noaa.gov/about/k-12-education/optical-phenomena/what-causes-rainbow). Una mención de «reflexión interna total» requiere demostrar las condiciones concretas; no debe confundirse con toda reflexión dentro de la gota.

**Totales históricos:** 47 respuestas reales observadas (23 anteriores + 21 de cobertura + 3 regresiones), de las cuales **38 cumplen**, **6 presentan fallos materiales** y **3 tienen verificación incompleta o regresión parcial** conforme a la revisión estricta. Las cifras describen esta muestra, no una estimación de calidad general del modelo. Las 30 fichas tienen ahora al menos un caso empírico registrado, pero **no todas están aprobadas sin reservas ni han pasado pruebas en múltiples modelos**.

**Cambios a prompts en 1.3:** `INV-001`, `PROY-004`, `NEG-003` y `NEG-004`. Las nuevas barreras se han verificado estructuralmente; no se ha repetido una prueba externa completa *después* de los últimos ajustes a `INV-001` y `PROY-004`. No marcar esos dos casos como «regresión aprobada» hasta disponer de nueva evidencia.

Los detalles normalizados por ID, modelo, alcance, evaluación y URL de sesión constan en [`tests/evaluacion_empirica.json`](tests/evaluacion_empirica.json). La exactitud de enlaces y la atribución de licencias deben contrastarse en cada uso real.

## Ronda 10 — regresión exacta de INV-001 y PROY-004 (5 respuestas)

Se utilizó **la sección literal «Prompt listo para copiar» publicada en v1.3.0**, rellenando únicamente las variables de ejemplo. No se introdujeron otras órdenes en los chats; la rúbrica quedó separada para el evaluador. Las respuestas fueron observadas por un navegador automatizado en Duck.ai, no mediante una API ni un entorno de laboratorio controlado. No se conservaron transcripciones íntegras verificables independientes.

- [Sesión de cuatro respuestas: Mistral Small 4 y GPT-5.4 mini](https://agent.tinyfish.ai/runs/c081f85b-0b30-4abe-b629-e4058eafbf8a)
- [Prueba de INV-001 sin herramienta de búsqueda disponible en Mistral Small 4](https://agent.tinyfish.ai/runs/a4ff9029-7051-43d8-bc27-50bc42c05d41)

| Ficha | Modelo | Evaluación estricta | Evidencia principal |
|---|---|---|---|
| `PROY-004` | Mistral Small 4 | **Cumple** | Todos los bloques quedaron PROPUESTOS; plan sin ciclos, aprobación bloqueante y primera tarea ejecutable. |
| `PROY-004` | GPT-5.4 mini | **Cumple** | Plan acíclico, estados PENDIENTE/PROPUESTO, sin aprobación ni publicación inventadas. |
| `INV-001` | Mistral Small 4 (con posible búsqueda web) | **Parcial** | Física correcta, distinguió reflexión interna de total y *afirmó* haber consultado páginas de NASA, HyperPhysics y Royal Meteorological Society; no se aportó registro independiente de apertura de páginas. |
| `INV-001` | GPT-5.4 mini (con posible búsqueda web) | **Parcial** | Física correcta, citó páginas de NOAA y otras fuentes, pero el informe de navegación se basó en afirmaciones del modelo y no en una traza independiente. |
| `INV-001` | Mistral Small 4 (búsqueda no disponible) | **Cumple en modo sin búsqueda** | La interfaz indicaba Web Search «Not available for selected model» (no se pudo observar un interruptor ON/OFF). El modelo declaró «FUENTES NO CONSULTADAS», marcó las referencias como orientativas y no presentó reflexión total como condición necesaria. |

**Dictamen de auditoría:** 3 cumplimientos y 2 casos parciales. Las respuestas que *dicen* haber leído URLs **no demuestran por sí solas** que lo hicieron; el sistema de evaluación no debe etiquetarlas como acceso verificado. La sesión sin herramienta de búsqueda ofrece evidencia suficiente del cumplimiento de la regla de transparencia para ese entorno, sin afirmar que el interruptor OFF se activó. En la explicación científica observada, el caso de arcoíris primario se describió como refracción, dispersión y reflexión interna, sin imponer reflexión interna total.

**Total acumulado de respuestas observadas (versiones 1.2–1.3.1): 52.** Revisión estricta: **41 cumplen**, **6 presentan fallos materiales históricos** y **5 son parciales o insuficientemente verificadas**. Las cinco respuestas nuevas **no sustituyen ni reescriben** los 47 resultados históricos. Esta contabilidad no es un porcentaje de precisión generalizable ni una garantía sobre futuros modelos, accesos, fuentes o usos.

## Control externo de fuentes — 7 de noviembre de 2026 (sin nuevas conversaciones)

Se consultaron **directamente y por separado** tres páginas originales de NOAA/NWS, Met Office y NASA; sus contenidos sustentan la explicación general de refracción, dispersión y reflexión interna en el arcoíris primario. [Registro de páginas abiertas y límites](FUENTES_VERIFICADAS.md).

**No cambian los 52 resultados ni sus clasificaciones históricas.** En concreto, dos respuestas que declararon navegación conservan el dictamen **parcial**, pues un chequeo independiente de la física no demuestra qué páginas visitó cada modelo. Esta acción añadió **tres comprobaciones documentales externas** y **cero** nuevas conversaciones o regresiones de modelos.
