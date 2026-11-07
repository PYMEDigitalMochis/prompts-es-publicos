---
id: NEG-004
titulo: "Definir chatbot de atencion responsable"
version: 1.3.0
estado: probado-manualmente-no
actualizado: 2026-11-07
categoria: 04_negocios
etiquetas: [chatbot, privacidad]
---

# Definir chatbot de atencion responsable

**Para qué sirve:** Diseñar respuestas automatizadas realistas con privacidad por defecto.

**Campos a personalizar:** `[TIPO_NEGOCIO]`, `[CANAL]`, `[SERVICIOS]`, `[HORARIOS]`

## Prompt listo para copiar

Diseña el flujo de atención automatizada para un [TIPO_NEGOCIO] mediante [CANAL]. Servicios y políticas confirmadas: [SERVICIOS]. Horarios confirmados: [HORARIOS].

Define bienvenida, menú principal, preguntas frecuentes, solicitud de información mínima, entrega a humano, mensajes fuera de horario y casos que requieren confirmación manual. Identifica integraciones como reales, propuestas o pendientes; no simules reservas confirmadas ni acceso a sistemas que no existen. Evita solicitar datos personales no necesarios. Entrega árboles de conversación, textos en español y pruebas de escenarios.

Barrera de datos operativos: si no se confirma un horario, teléfono, enlace, canal habilitado, política o agenda, escribe **PENDIENTE DE CONFIRMACIÓN**; no inventes franjas genéricas como «mañanas» o «tardes», números de contacto aunque sean ficticios, promesas de respuesta o rutas de derivación que aún no funcionan. Las plantillas de mensajes de fuera de horario son **propuestas**, no reglas activadas, hasta disponer de horarios y un canal real. No propongas «reservación confirmada» ni «pago realizado» sin consulta verificada de un sistema autorizado; etiqueta toda integración como NO CONECTADA si no hay prueba de conexión. Usa solamente los datos personales imprescindibles y condiciona su recopilación a finalidad y consentimiento aplicables.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
