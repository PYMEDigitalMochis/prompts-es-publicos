# Privacidad de autoría en GitHub

La biblioteca pública solo debe incluir ejemplos sintéticos y el alias público del autor. Las direcciones de correo usadas por Git para la autoría y confirmación de commits no son archivos ordinarios: viven en el **historial**. Eliminar un correo del README o de una ficha no lo borra del historial de Git.

## Prevención para nuevos commits

El titular de la cuenta debe revisar [Settings → Emails](https://github.com/settings/emails) y activar **Keep my email addresses private**. Si usa la línea de comandos, debe configurar además el correo `noreply` que GitHub asigna a esa cuenta. Se recomienda activar **Block command line pushes that expose my email**. Esta preferencia pertenece a la cuenta y no puede considerarse cambiada sin comprobarla en la interfaz autenticada.

## Historial ya publicado

Una reescritura cuidadosa puede sustituir el correo de los commits alcanzables desde la rama principal, pero cambiará las identificaciones SHA y puede invalidar enlaces a commits antiguos. También puede dejar copias o vistas en caché y no garantiza la eliminación global de datos previamente publicados. Para casos graves se puede consultar el procedimiento oficial de [GitHub sobre datos sensibles](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository).

## Comprobación técnica

En un clon autorizado, ejecutar `git log --format='%h %ae %ce %s' main` para revisar la autoría y confirmación visibles. Revisar además ramas y etiquetas si existiesen. **Una salida limpia en la rama principal no demuestra que hayan desaparecido copias de GitHub, forks o clones ajenos.**

El repositorio original privado mantiene su propio historial y no debe modificarse como parte de este proceso.

## Estado de privacidad revisado (7 de noviembre de 2026)

El 7 de noviembre de 2026 se revisó la sesión autenticada de la cuenta pública en GitHub. **Keep my email addresses private** estaba desactivada y se activó; **Block command line pushes that expose my email** ya estaba activada. Al recargar [GitHub Emails](https://github.com/settings/emails) se verificó que **ambas permanecieron activadas**. También se comprobaron ocho commits accesibles de `main` con correo GitHub `noreply` como autor y confirmador. No se modificaron otros repositorios ni ajustes. Esta verificación de configuración de cuenta no prueba la eliminación de copias antiguas.

## Control de las futuras contribuciones

- Mantener habilitadas ambas opciones de privacidad de cuenta. Su presencia debe verificarse desde la sesión autenticada, no deducirse de los commits anteriores.
- **Antes de publicar un nuevo commit**, comprobar el correo de **autor y confirmador**. El conector de GitHub puede crear commits sin permitir escoger explícitamente su autor; la opción de privacidad de cuenta no debe suponerse suficiente para todas las integraciones.
- La validación automatizada de GitHub Actions comprueba metadatos del nuevo `HEAD` tras un push a `main`. Es una **alarma posterior a la publicación**, **no** un bloqueo previo a que el correo quede expuesto.
- Si se usa la API Git de manera programática, se puede crear un commit todavía **sin enlazarlo a una rama**, inspeccionar su autoría y mover la rama solo después de confirmar que ambas direcciones son `noreply`. No anunciar un cambio como publicado hasta verificar la rama.
- No reescribir historia ni forzar publicaciones solamente para ocultar datos sin evaluar clones, etiquetas, enlaces históricos y riesgos de pérdida de trabajo.
