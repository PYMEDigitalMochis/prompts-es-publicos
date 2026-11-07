---
id: ESP-003
titulo: "Organizar proyecto audiovisual y licencias"
version: 1.2.0
estado: evaluacion-parcial
actualizado: 2026-11-06
categoria: 08_casos_practicos
etiquetas: [audiovisual, licencias, edicion]
---

# Organizar proyecto audiovisual y licencias

**Para qué sirve:** Coordinar narración, escenas y recursos visuales con control de calidad y permisos.

**Campos a personalizar:** `[OBJETIVO]`, `[AUDIOS]`, `[GUION]`, `[RECURSOS_VISUALES]`, `[DESTINO]`

## Prompt listo para copiar

Organiza un proyecto audiovisual. Objetivo y público: [OBJETIVO]. Grabaciones disponibles: [AUDIOS]. Guion: [GUION]. Material visual candidato: [RECURSOS_VISUALES]. Formato y destino final: [DESTINO].

Ordena y verifica las pistas de voz, la duración total, la correspondencia escena-guion y la continuidad sonora. Para cada recurso visual consigna procedencia, permiso o licencia exacta y requisitos de atribución. No consideres una imagen o videoclip reutilizable sin evidencia de su licencia. Genera un plan de montaje, lista de recursos y lista de comprobaciones; procesa archivos únicamente cuando existan y sean accesibles. Distingue lo producido de lo recomendado o pendiente.

### Barrera de metadatos y derechos

Si los nombres de archivos se mencionan pero **no se adjuntan ni se pueden abrir**, indica **ESTADO: SIN ARCHIVOS VERIFICABLES**. Para cada pista muestra **Duración: NO MEDIDA**, **Contenido: DESCONOCIDO** y **Función: NO CONFIRMADA**; no atribuyas duraciones aproximadas, tipo de audio, contenido, orden, licencia ni mejoras realizadas. Una duración objetivo del video no equivale a duración medida del audio. No inventes marcas de tiempo ni ajustes ejecutados.

Para recursos visuales, **no equipares el nombre de una plataforma con una licencia**: no afirmes que todas las imágenes de bancos de material usan CC0 o CC BY. Comprueba **la página de cada recurso**, la licencia específica aplicable, limitaciones, fecha de consulta y atribución requerida. Si no puedes verificarlo, anota **LICENCIA NO VERIFICADA — NO UTILIZAR**. Prohíbe descargar o distribuir el recurso mientras falte permiso comprobable.

Separa siempre tres estados: **VERIFICADO** (con evidencia concreta), **PROPUESTO** (plan no ejecutado) y **BLOQUEADO** (falta de archivos o derechos).

## Comprobación del resultado

- ¿El resultado responde al objetivo con datos reales y verificables?
- ¿Se distinguen acciones ejecutadas, propuestas, restricciones y pendientes?
- ¿La entrega permite continuar de forma segura y autónoma?
