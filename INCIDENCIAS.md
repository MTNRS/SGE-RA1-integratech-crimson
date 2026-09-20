# Incidencias

## Bloqueo de la base temporal en Windows

**Incidencia:** la primera ejecución no pudo eliminar `prueba.db` porque Windows
la consideraba en uso. El contexto de transacción de `sqlite3` confirma o revierte
los cambios, pero no cierra automáticamente la conexión.

**Resolución:** se añadió un bloque `try/finally` que ejecuta `conexion.close()`
antes de abandonar la carpeta temporal. La verificación y las pruebas finalizaron
correctamente después del cambio.

## Alcance de la verificación

**Incidencia:** el ERP-CRM real utiliza PostgreSQL en infraestructura privada y
no es correcto incluir credenciales ni conectarse a producción desde un proyecto
académico público.

**Resolución:** se ha verificado el código y la documentación del repositorio
privado `IntTecCon/integra-tech-platform` en la revisión `fb82959`. La prueba
ejecutable se limita al entorno local y utiliza SQLite temporal para comprobar
que Python puede crear, escribir, leer y verificar una base de datos sin tocar
producción.

## Carga de archivos JSON desde el navegador

**Incidencia:** algunos navegadores bloquean `fetch` al abrir `index.html`
directamente mediante `file://`.

**Resolución:** servir la carpeta con `python -m http.server 8000` y abrir
`http://localhost:8000`.
