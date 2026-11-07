# Biblioteca abierta de prompts en español

**30 prompts · 9 categorías · Edición pública 1.1.0**

Colección de plantillas editables para investigación, planificación, desarrollo, negocios, aprendizaje, escritura, empleo y casos prácticos. Cada ficha incluye variables, una instrucción lista para copiar y criterios para comprobar su resultado. No se necesitan servicios de pago ni cuentas externas para leer las fichas.

## Acceso rápido

1. [Explorar el catálogo por categoría](CATALOGO.md).
2. Abrir una ficha Markdown y copiar su sección **Prompt listo para copiar**.
3. Reemplazar los valores `[ENTRE_CORCHETES]` por información propia (sin compartir contraseñas ni datos sensibles).
4. Ejecutar la instrucción en una herramienta de IA compatible y verificar el resultado.

Funciona desde un navegador móvil o una computadora; las instrucciones no dependen de un modelo o aplicación específicos.

## Organización

| Carpeta | Tema |
|---|---|
| `00_meta` | Diseño y mejora de prompts |
| `01_investigacion` | Investigación y verificación de afirmaciones |
| `02_gestion_proyectos` | Seguimiento y documentación de proyectos |
| `03_desarrollo` | Desarrollo, revisiones y pruebas |
| `04_negocios` | Prospección, propuestas y catálogos |
| `05_aprendizaje` | Tutoría y ejercicios |
| `06_escritura` | Edición y guiones |
| `07_empleo` | Búsqueda de empleo y currículum |
| `08_casos_practicos` | Flujos y ejemplos generales |

## Calidad y límites

Las fichas **han superado comprobaciones estructurales automáticas**, pero **no tienen pruebas documentadas de ejecución con modelos de IA**. Un prompt no da acceso por sí solo a internet, cuentas, repositorios, dispositivos ni archivos: esas capacidades dependen de la herramienta utilizada y de los permisos disponibles. Comprueba fuentes, datos y resultados antes de actuar; no compartas información privada en ejemplos o incidencias.

## Archivos de referencia

- [Catálogo](CATALOGO.md)
- [Ejemplos de entrada para las 30 fichas](EJEMPLOS_DE_PRUEBA.md)
- [Validación automatizada y límites](PRUEBAS_Y_LIMITACIONES.md)
- [Guía de uso](GUIA_DE_USO.md)
- [Plantilla para nuevas fichas](PLANTILLA_DE_PROMPT.md)
- [Guía de contribuciones](CONTRIBUTING.md)
- [Política de seguridad](SECURITY.md)
- [Historial de versiones](CHANGELOG.md)
- [Licencia Creative Commons Atribución 4.0 Internacional (CC BY 4.0)](LICENSE.md)

## Licencia

Contenido original: © 2026 **PYMEDigitalMochis** (alias público del titular). Licenciado bajo [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Puedes copiar, compartir, adaptar y usar el contenido, incluso comercialmente, siempre que proporciones atribución y señales los cambios. Lee los términos completos en [LICENSE.md](LICENSE.md). Los nombres de servicios y las marcas de terceros pertenecen a sus respectivos titulares.

## Pruebas continuas

Los cambios se comprueban automáticamente con `python -m unittest discover -s tests -p validar_biblioteca.py -v`, sin dependencias externas. Este chequeo verifica integridad y privacidad básica, **no sustituye la ejecución real en un modelo de IA**.
