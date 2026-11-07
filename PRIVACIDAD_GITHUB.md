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

La rama `main` accesible del repositorio público se comprobó previamente con correo `noreply` en los commits alcanzables. La configuración privada del correo a nivel de cuenta no es legible ni modificable por el conector disponible; el propietario debe comprobarla autenticado en GitHub. Los datos públicos que hayan aparecido en clones o cachés externos no se pueden borrar garantizadamente. Cada actualización mediante el conector debe verificar nuevamente la autoría del nuevo commit para no reintroducir el correo original.
