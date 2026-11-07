# Ejemplos de entrada para las 30 fichas

**Estado:** casos de prueba ficticios, aptos para rellenar variables. **No equivalen a una ejecución de un modelo de IA ni demuestran la calidad de sus respuestas.**

Para usar uno, abre la ficha del mismo ID y sustituye sus variables por los valores siguientes. Verifica siempre el contenido producido.

## META-001

Ficha: [META-001_convertir-una-idea-en-prompt-eficaz.md](prompts/00_meta/META-001_convertir-una-idea-en-prompt-eficaz.md)

| Variable | Valor de ejemplo |
|---|---|
| `[IDEA]` | Quiero organizar una sesión semanal de lectura |
| `[CONTEXTO]` | Participan cinco personas; presupuesto cero; duración 45 minutos |
| `[DESTINATARIO]` | Asistente de texto |
| `[FORMATO]` | Texto compatible con ATS |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## META-002

Ficha: [META-002_auditar-y-mejorar-un-prompt-existente.md](prompts/00_meta/META-002_auditar-y-mejorar-un-prompt-existente.md)

| Variable | Valor de ejemplo |
|---|---|
| `[PROMPT_ORIGINAL]` | Ayúdame a estudiar mejor |
| `[OBJETIVO]` | Elaborar un plan con evidencias y entregables |
| `[PROBLEMA]` | No indica objetivo ni restricciones |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## META-003

Ficha: [META-003_elegir-el-prompt-adecuado.md](prompts/00_meta/META-003_elegir-el-prompt-adecuado.md)

| Variable | Valor de ejemplo |
|---|---|
| `[TAREA]` | Preparar un plan de aprendizaje de 4 semanas |
| `[INVENTARIO]` | APR-001 tutoría; PROY-004 planificación |
| `[RESTRICCIONES]` | Sin gasto; móvil solamente |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## INV-001

Ficha: [INV-001_investigar-con-fuentes-verificables.md](prompts/01_investigacion/INV-001_investigar-con-fuentes-verificables.md)

| Variable | Valor de ejemplo |
|---|---|
| `[PREGUNTA]` | ¿Cómo se forma un arcoíris? |
| `[LUGAR]` | Contexto general |
| `[PERIODO]` | Conocimiento establecido; fecha de consulta |
| `[PROFUNDIDAD]` | Síntesis con fuentes educativas |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## INV-002

Ficha: [INV-002_comparar-opciones-con-criterios-ponderados.md](prompts/01_investigacion/INV-002_comparar-opciones-con-criterios-ponderados.md)

| Variable | Valor de ejemplo |
|---|---|
| `[OPCIONES]` | Plan A: estudiar 15 minutos al día; Plan B: 45 minutos tres veces por semana |
| `[CRITERIOS]` | Disponibilidad, continuidad, esfuerzo |
| `[PRIORIDADES]` | Continuidad 50%; esfuerzo 30%; flexibilidad 20% |
| `[CONTEXTO]` | Participan cinco personas; presupuesto cero; duración 45 minutos |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## INV-003

Ficha: [INV-003_verificar-una-afirmacion-viral.md](prompts/01_investigacion/INV-003_verificar-una-afirmacion-viral.md)

| Variable | Valor de ejemplo |
|---|---|
| `[AFIRMACION]` | Una publicación afirma que el agua fría hierve antes que la caliente en cualquier circunstancia |
| `[ORIGEN]` | Publicación sin autor identificado |
| `[FECHA]` | Dentro de cuatro semanas |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## INV-004

Ficha: [INV-004_radar-de-cambios-con-impacto-practico.md](prompts/01_investigacion/INV-004_radar-de-cambios-con-impacto-practico.md)

| Variable | Valor de ejemplo |
|---|---|
| `[SECTOR]` | Herramientas digitales educativas |
| `[REGION]` | México |
| `[VENTANA]` | Últimos 30 días |
| `[PERFIL]` | Persona que estudia desde Android |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## PROY-001

Ficha: [PROY-001_retomar-un-proyecto-desde-el-ultimo-avance.md](prompts/02_gestion_proyectos/PROY-001_retomar-un-proyecto-desde-el-ultimo-avance.md)

| Variable | Valor de ejemplo |
|---|---|
| `[PROYECTO]` | Sitio demostrativo ficticio para una biblioteca |
| `[FUENTES]` | README y bitácora adjuntos de ejemplo |
| `[OBJETIVO_ACTUAL]` | Completar revisión de enlaces internos |
| `[RESTRICCIONES]` | Sin gasto; móvil solamente |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## PROY-002

Ficha: [PROY-002_auditar-estado-y-detectar-discrepancias.md](prompts/02_gestion_proyectos/PROY-002_auditar-estado-y-detectar-discrepancias.md)

| Variable | Valor de ejemplo |
|---|---|
| `[PROYECTO]` | Sitio demostrativo ficticio para una biblioteca |
| `[FUENTES]` | README y bitácora adjuntos de ejemplo |
| `[ESTADO_OBJETIVO]` | Versión de prueba con rutas válidas |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## PROY-003

Ficha: [PROY-003_registro-de-decisiones-y-avances.md](prompts/02_gestion_proyectos/PROY-003_registro-de-decisiones-y-avances.md)

| Variable | Valor de ejemplo |
|---|---|
| `[PROYECTO]` | Sitio demostrativo ficticio para una biblioteca |
| `[SESION]` | Revisión de documentación de esta semana |
| `[EVIDENCIA]` | Registro de pruebas de muestra |
| `[DECISIONES]` | Conservar el sitio de producción sin cambios |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## PROY-004

Ficha: [PROY-004_plan-de-ejecucion-por-dependencias.md](prompts/02_gestion_proyectos/PROY-004_plan-de-ejecucion-por-dependencias.md)

| Variable | Valor de ejemplo |
|---|---|
| `[OBJETIVO]` | Crear un sitio de demostración en cuatro semanas |
| `[CONTEXTO]` | Participan cinco personas; presupuesto cero; duración 45 minutos |
| `[RECURSOS]` | Android y documentos Markdown |
| `[FECHA]` | Dentro de cuatro semanas |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## DEV-001

Ficha: [DEV-001_diagnosticar-y-corregir-un-error.md](prompts/03_desarrollo/DEV-001_diagnosticar-y-corregir-un-error.md)

| Variable | Valor de ejemplo |
|---|---|
| `[SINTOMA]` | La página de ejemplo muestra 404 al recargar una ruta interna |
| `[REPRODUCCION]` | Abrir /catalogo y recargar |
| `[ENTORNO]` | Sitio estático en entorno de prueba |
| `[CODIGO]` | Log ficticio: GET /catalogo -> 404 |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## DEV-002

Ficha: [DEV-002_revisar-un-pull-request-y-sus-pruebas.md](prompts/03_desarrollo/DEV-002_revisar-un-pull-request-y-sus-pruebas.md)

| Variable | Valor de ejemplo |
|---|---|
| `[REPOSITORIO]` | Repositorio demostrativo autorizado, sin datos de clientes |
| `[PR]` | PR demostrativo #1 |
| `[REQUISITOS]` | Rutas válidas y sin exposición de datos |
| `[CONDICIONES]` | Checks aprobados y autorización previa |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## DEV-003

Ficha: [DEV-003_validar-despliegue-preview-y-rutas-http.md](prompts/03_desarrollo/DEV-003_validar-despliegue-preview-y-rutas-http.md)

| Variable | Valor de ejemplo |
|---|---|
| `[URL_PREVIEW]` | https://example.org/preview/ |
| `[RUTAS]` | / ; /catalogo ; /no-existe |
| `[COMPORTAMIENTO_ESPERADO]` | 200, 200 y 404 respectivamente |
| `[RAMA]` | rama de pruebas |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## DEV-004

Ficha: [DEV-004_documentar-cambio-tecnico-reproducible.md](prompts/03_desarrollo/DEV-004_documentar-cambio-tecnico-reproducible.md)

| Variable | Valor de ejemplo |
|---|---|
| `[CAMBIO]` | Actualizar navegación del catálogo |
| `[ARCHIVOS]` | README.md y CATALOGO.md |
| `[PRUEBAS]` | Validación estructural local con resultado registrado |
| `[LIMITACIONES]` | Sin acceso al despliegue externo |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## NEG-001

Ficha: [NEG-001_preparar-prospeccion-comercial-local.md](prompts/04_negocios/NEG-001_preparar-prospeccion-comercial-local.md)

| Variable | Valor de ejemplo |
|---|---|
| `[SECTOR]` | Herramientas gratuitas para productividad |
| `[CIUDAD]` | Ciudad ficticia Villa Ejemplo |
| `[SERVICIO]` | Página informativa móvil |
| `[PRESUPUESTO]` | Cero, únicamente investigación pública |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## NEG-002

Ficha: [NEG-002_crear-propuesta-profesional-a-cliente.md](prompts/04_negocios/NEG-002_crear-propuesta-profesional-a-cliente.md)

| Variable | Valor de ejemplo |
|---|---|
| `[CLIENTE]` | Comercio ficticio Tienda Ejemplo |
| `[NECESIDAD]` | Mostrar horarios y ubicación |
| `[ALCANCE]` | Página informativa, sin pagos |
| `[PRECIO]` | Importe por confirmar; sin cotización vinculante |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## NEG-003

Ficha: [NEG-003_disenar-catalogo-de-sitios-de-demostracion.md](prompts/04_negocios/NEG-003_disenar-catalogo-de-sitios-de-demostracion.md)

| Variable | Valor de ejemplo |
|---|---|
| `[SECTORES]` | Comercio local, servicios y restaurante ficticios |
| `[IDENTIDAD]` | Paleta azul marino y blanco de ejemplo |
| `[FORMATOS]` | HTML y presentación |
| `[FUNCIONES]` | Navegación y formulario simulado |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## NEG-004

Ficha: [NEG-004_definir-chatbot-de-atencion-responsable.md](prompts/04_negocios/NEG-004_definir-chatbot-de-atencion-responsable.md)

| Variable | Valor de ejemplo |
|---|---|
| `[TIPO_NEGOCIO]` | Librería ficticia |
| `[CANAL]` | Chat de demostración |
| `[SERVICIOS]` | Consulta de catálogo; sin compras |
| `[HORARIOS]` | Lunes a viernes de 10:00 a 18:00, ficticio |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## APR-001

Ficha: [APR-001_ensenar-con-practica-adaptativa.md](prompts/05_aprendizaje/APR-001_ensenar-con-practica-adaptativa.md)

| Variable | Valor de ejemplo |
|---|---|
| `[TEMA]` | Conceptos básicos de redes |
| `[NIVEL]` | Principiante |
| `[EQUIPO]` | Un teléfono Android |
| `[TIEMPO]` | 20 |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## APR-002

Ficha: [APR-002_corregir-ejercicios-y-avanzar.md](prompts/05_aprendizaje/APR-002_corregir-ejercicios-y-avanzar.md)

| Variable | Valor de ejemplo |
|---|---|
| `[TEMA]` | Conceptos básicos de redes |
| `[PREGUNTAS]` | ¿Qué es DNS? Respuesta: sistema de nombres de dominio |
| `[RESPUESTAS]` | DNS relaciona nombres y direcciones IP |
| `[PROGRESO]` | Se completó la introducción |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## APR-003

Ficha: [APR-003_diagnosticar-conexion-desde-android.md](prompts/05_aprendizaje/APR-003_diagnosticar-conexion-desde-android.md)

| Variable | Valor de ejemplo |
|---|---|
| `[SINTOMA]` | Un video pierde resolución por las noches |
| `[MEDICIONES]` | Latencia de ejemplo 50 ms, pérdida 0% |
| `[APLICACIONES]` | Una plataforma de video, resto de sitios sin problema |
| `[HORARIO]` | Noches |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## ESC-001

Ficha: [ESC-001_editar-texto-conservando-la-voz.md](prompts/06_escritura/ESC-001_editar-texto-conservando-la-voz.md)

| Variable | Valor de ejemplo |
|---|---|
| `[TEXTO]` | La tecnología cambia todo. Es bueno aprender. |
| `[PUBLICO]` | Lectores generales |
| `[TONO]` | Informativo y claro |
| `[LIMITE]` | 100 palabras |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## ESC-002

Ficha: [ESC-002_crear-guion-divulgativo-verificable.md](prompts/06_escritura/ESC-002_crear-guion-divulgativo-verificable.md)

| Variable | Valor de ejemplo |
|---|---|
| `[TEMA]` | Por qué cambia la forma de la Luna |
| `[DURACION]` | 2 minutos |
| `[AUDIENCIA]` | Estudiantes de secundaria |
| `[ESTILO]` | Explicación divulgativa sin datos inventados |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## EMP-001

Ficha: [EMP-001_buscar-y-filtrar-vacantes-vigentes.md](prompts/07_empleo/EMP-001_buscar-y-filtrar-vacantes-vigentes.md)

| Variable | Valor de ejemplo |
|---|---|
| `[PUESTOS]` | Auxiliar administrativo y atención al cliente |
| `[UBICACION]` | Remoto desde México |
| `[EXPERIENCIA]` | Un año de prácticas ficticias |
| `[RESTRICCIONES]` | Sin gasto; móvil solamente |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## EMP-002

Ficha: [EMP-002_adaptar-cv-a-una-vacante.md](prompts/07_empleo/EMP-002_adaptar-cv-a-una-vacante.md)

| Variable | Valor de ejemplo |
|---|---|
| `[CV]` | Resumen ficticio: atención a clientes, organización de expedientes |
| `[VACANTE]` | Puesto ficticio de auxiliar administrativo |
| `[LOGROS]` | Registro exacto de 20 expedientes por semana, ejemplo |
| `[FORMATO]` | Currículum de una página, sin inventar experiencia |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## ESP-001

Ficha: [ESP-001_verificar-cambios-antes-de-produccion.md](prompts/08_casos_practicos/ESP-001_verificar-cambios-antes-de-produccion.md)

| Variable | Valor de ejemplo |
|---|---|
| `[REPOSITORIO]` | Repositorio demostrativo autorizado, sin datos de clientes |
| `[CAMBIO]` | Actualizar navegación del catálogo |
| `[URL_PREVIEW]` | https://example.org/preview/ |
| `[RUTAS]` | / ; /catalogo ; /no-existe |
| `[CRITERIOS_PUBLICACION]` | Códigos HTTP y enlaces comprobados; aprobación expresa |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## ESP-002

Ficha: [ESP-002_crear-catalogo-de-productos-con-identidad-visual.md](prompts/08_casos_practicos/ESP-002_crear-catalogo-de-productos-con-identidad-visual.md)

| Variable | Valor de ejemplo |
|---|---|
| `[MARCA_O_PROYECTO]` | Marca ficticia Muestra |
| `[PRODUCTOS]` | Cuaderno modelo A y libreta modelo B, ficticios |
| `[PALETA_APROBADA]` | Azul #123456 y blanco #FFFFFF |
| `[IMAGENES]` | No proporcionadas |
| `[FICHAS_TECNICAS]` | Medidas aún por confirmar |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## ESP-003

Ficha: [ESP-003_organizar-proyecto-audiovisual-y-licencias.md](prompts/08_casos_practicos/ESP-003_organizar-proyecto-audiovisual-y-licencias.md)

| Variable | Valor de ejemplo |
|---|---|
| `[OBJETIVO]` | Explicar astronomía a estudiantes con recursos libres |
| `[AUDIOS]` | No proporcionados |
| `[GUION]` | Guion ficticio de 90 segundos sobre astronomía |
| `[RECURSOS_VISUALES]` | Sin materiales licenciados confirmados |
| `[DESTINO]` | Video educativo horizontal |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

## ESP-004

Ficha: [ESP-004_revisar-continuidad-de-obra-creativa.md](prompts/08_casos_practicos/ESP-004_revisar-continuidad-de-obra-creativa.md)

| Variable | Valor de ejemplo |
|---|---|
| `[OBRA]` | Relato ficticio La Estación |
| `[DOCUMENTOS]` | Resumen ficticio: dos personajes, una escena en una estación |
| `[CAPITULO]` | Capítulo 2 |
| `[OBJETIVO]` | Escribir una escena coherente con el resumen aportado |

**Criterio de aceptación:** no inventar evidencias ni accesos; respetar los límites y entregar lo solicitado por la ficha.

