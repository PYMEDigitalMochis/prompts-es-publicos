# Evaluación empírica con modelos de IA — noviembre de 2026

**Ámbito:** prompts públicos, entradas ficticias, sin documentos privados ni credenciales. **Modalidad:** conversaciones reales nuevas en [Duck.ai](https://duck.ai), gestionadas por un navegador automatizado. Las respuestas se observaron mediante el agente del navegador y se contrastaron con criterios predefinidos; los enlaces siguientes permiten revisar cada ejecución. No son simulaciones de respuestas ni llamadas a API. Las salidas completas no se guardaron como ficheros independientes, por lo que las citas breves son evidencias parciales y la evaluación debe entenderse como una muestra.

## Cobertura

- Modelos utilizados: Claude Haiku 5.5, Mistral Small 4 y GPT-5.4 mini (denominaciones mostradas en el servicio durante las pruebas).
- Categorías cubiertas: las nueve de esta biblioteca, mediante nueve prompts representativos: `META-001`, `INV-003`, `PROY-001`, `DEV-001`, `NEG-002`, `APR-001`, `ESC-002`, `EMP-001`, `ESP-003`.
- La validación automática local revisa los 30 prompts, **pero solo estos nueve han sido probados empíricamente**. No extrapolar los resultados a los otros 21 ni asegurar rendimiento en todas las versiones de los modelos.

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
