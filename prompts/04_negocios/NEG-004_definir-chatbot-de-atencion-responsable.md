---
id: NEG-004
titulo: "Definir chatbot de atencion responsable"
version: 1.1.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 04_negocios
etiquetas: [chatbot, privacidad]
---

# Definir chatbot de atencion responsable

**Para qué sirve:** Diseñar respuestas automatizadas realistas con privacidad por defecto.

**Campos a personalizar:** `[TIPO_NEGOCIO]`, `[CANAL]`, `[SERVICIOS]`, `[HORARIOS]`

## Prompt listo para copiar

Diseña el flujo de atención automatizada para un [TIPO_NEGOCIO] mediante [CANAL]. Servicios y políticas confirmadas: [SERVICIOS]. Horarios confirmados: [HORARIOS].

Define bienvenida, menú principal, preguntas frecuentes, solicitud de información mínima, entrega a humano, mensajes fuera de horario y casos que requieren confirmación manual. Identifica integraciones como reales, propuestas o pendientes; no simules reservas confirmadas ni acceso a sistemas que no existen. Evita solicitar datos personales no necesarios. Entrega árboles de conversación, textos en español y pruebas de escenarios.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
