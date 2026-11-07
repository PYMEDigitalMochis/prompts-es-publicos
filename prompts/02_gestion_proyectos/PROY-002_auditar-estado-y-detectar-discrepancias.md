---
id: PROY-002
titulo: "Auditar estado y detectar discrepancias"
version: 1.1.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 02_gestion_proyectos
etiquetas: [auditoria, trazabilidad]
---

# Auditar estado y detectar discrepancias

**Para qué sirve:** Conciliar repositorios, documentos y decisiones.

**Campos a personalizar:** `[PROYECTO]`, `[FUENTES]`, `[ESTADO_OBJETIVO]`

## Prompt listo para copiar

Audita [PROYECTO] usando únicamente [FUENTES] a las que tengas acceso. Estado deseado: [ESTADO_OBJETIVO].

Construye una matriz compacta: componente, estado confirmado, evidencia/enlace, discrepancia y acción correctiva. Identifica qué fuente manda para cada tipo de dato, separa material histórico de vigente y no sobrescribas documentación por intuición. Propón correcciones ordenadas por riesgo y dependencia. Realiza cambios solo si están autorizados y son reversibles o controlados; verifica después.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
