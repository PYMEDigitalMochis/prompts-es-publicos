---
id: INV-003
titulo: "Verificar una afirmacion viral"
version: 1.0.0
estado: probado-manualmente-no
actualizado: 2026-11-06
categoria: 01_investigacion
etiquetas: [verificacion, investigacion]
---

# Verificar una afirmacion viral

**Para qué sirve:** Separar evidencia de opiniones y mensajes engañosos.

**Campos a personalizar:** `[AFIRMACION]`, `[ORIGEN]`, `[FECHA]`

## Prompt listo para copiar

Verifica esta afirmación: [AFIRMACION]. Origen conocido: [ORIGEN]. Fecha o contexto: [FECHA].

Divide la afirmación en puntos comprobables. Busca fuentes originales y contexto temporal. Clasifica cada punto como confirmado, falso, engañoso o sin evidencia suficiente, explicando las razones y citando fuentes. Si la navegación no está disponible, limita tu respuesta al análisis interno y evita conclusiones categóricas sobre hechos recientes.

## Comprobación del resultado

- ¿Se respondió al objetivo y se completaron las tareas autorizadas?
- ¿Se separaron hechos, inferencias y pendientes, sin inventar accesos, fuentes ni acciones?
- ¿El formato final permite usar el resultado directamente?
