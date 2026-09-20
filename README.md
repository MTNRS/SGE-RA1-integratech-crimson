# Integra Tech | Crimson

Proyecto práctico del RA1 de **0491 - Sistemas de gestión empresarial**. Parte
de la interfaz sencilla y dividida en componentes de `jocarsa | crimson` y la
aplica al análisis del ERP-CRM real de **Integra Tech Consulting**.

## Objetivo

Comparar varios ERP-CRM, sus licencias, sistemas operativos y gestores de datos;
justificar la solución apropiada para Integra Tech; y verificar mediante un
programa reproducible la configuración del entorno local de demostración.

## Relación con Integra Tech Consulting

El repositorio privado real `IntTecCon/integra-tech-platform`, revisión
`fb82959`, contiene un backend Python con FastAPI y conexión PostgreSQL mediante
`psycopg2`. También incluye los modelos de clientes, proyectos, facturas,
documentos y módulos SaaS. Esta entrega utiliza esa arquitectura como caso real,
sin copiar secretos, datos empresariales ni información de clientes.

La conclusión del estudio es conservar la plataforma propia: ya cubre ERP y CRM,
permite adaptar los módulos a los servicios de la empresa y evita una migración.

## Ejecución

No necesita librerías externas.

```bash
python verificar_sistema.py
python -m unittest discover -v
python -m http.server 8000
```

Después, abre `http://localhost:8000`.

## Criterios de evaluación

| Criterio | Evidencia |
|---|---|
| a | La aplicación presenta Integra Tech Platform, Odoo, ERPNext y Dynamics 365 Business Central. |
| b | `datos/sistemas.json` y la tabla web identifican licencias abiertas, privadas y por suscripción. |
| c | La tabla compara características y requisitos de los cuatro sistemas. |
| d | Cada alternativa indica el sistema operativo o modalidad cloud adecuada. |
| e | Cada alternativa identifica PostgreSQL, MariaDB, Azure SQL o SQL Server según corresponda. |
| f | `verificar_sistema.py` comprueba SO, Python, SQLite, integridad de una base temporal y archivos del prototipo. La configuración real se contrasta con el código de Integra Tech sin acceder a producción. |
| g | `README.md` y `INFORME.md` documentan las operaciones. |
| h | `INCIDENCIAS.md` registra las incidencias y sus soluciones. |

## Fuentes consultadas

- [Odoo 19: instalación desde código](https://www.odoo.com/documentation/19.0/administration/on_premise/source.html)
- [Odoo 19: licencias](https://www.odoo.com/documentation/19.0/legal/licenses.html)
- [Frappe: licencias de ERPNext y Frappe CRM](https://docs.frappe.io/legal/others/license-and-trademark)
- [ERPNext: requisito de MariaDB](https://github.com/frappe/helm/blob/main/erpnext/README.md)
- [Business Central: opciones de despliegue](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/deployment/deployment)
- [Business Central: licencias](https://www.microsoft.com/licensing/guidance/Dynamics-365-Business-Central)
- [Business Central: Azure SQL](https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/service-overview)

Fuentes revisadas el 20 de septiembre de 2026.

## Decisiones técnicas

La interfaz mantiene el estilo didáctico de Crimson: HTML, CSS y JavaScript sin
frameworks, navegación lateral, tarjetas y una tabla de clientes transformada en
tabla comparativa. Los datos se separan en JSON para poder revisarlos sin tocar
la presentación.

SQLite se emplea únicamente en la prueba local porque forma parte de Python y
permite comprobar operaciones reales sin levantar servicios ni usar producción.
PostgreSQL sigue siendo el gestor seleccionado para la plataforma empresarial.

## Uso de IA

Se ha utilizado IA como apoyo para localizar fuentes oficiales, ordenar la
comparación, preparar la primera versión del código y revisar las pruebas. El
alumno debe ejecutar el proyecto, contrastar las fuentes y poder explicar la
elección de sistema operativo, licencia y gestor de datos de cada alternativa.
