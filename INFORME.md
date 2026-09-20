# Informe del proyecto: Integra Tech | Crimson

**Módulo:** 0491 - Sistemas de gestión empresarial

**Resultado de aprendizaje:** RA1

**Proyecto:** Identificación y verificación de sistemas ERP-CRM

## Resultado de aprendizaje

Identifica sistemas de planificación de recursos empresariales y de gestión de
relaciones con clientes (ERP-CRM), reconoce sus características y verifica la
configuración del sistema informático.

## Descripción

El proyecto compara Integra Tech Platform, Odoo, ERPNext y Dynamics 365 Business
Central. Estudia sus licencias, sistemas operativos, gestores de datos,
características y requisitos. La decisión se aplica al código real de Integra
Tech Consulting, revisión `fb82959`, que usa Python, FastAPI y PostgreSQL.

La verificación ejecutable se realiza en un entorno local aislado. Comprueba el
sistema operativo, Python, SQLite, la integridad de una base temporal y los
archivos del prototipo. No utiliza credenciales ni se conecta a producción.

Este informe se ha generado con **jocarsa | documentación** desde una copia limpia
de los archivos versionados. Se excluyen `.git`, cachés y librerías. La función
de documentación automática mediante IA del generador está desactivada.

## Árbol del proyecto

```text
proyecto
   +- config
   |  \- requisitos.json
   +- css
   |  \- estilo.css
   +- datos
   |  \- sistemas.json
   +- js
   |  \- aplicacion.js
   +- tests
   |  +- __init__.py
   |  \- test_verificar_sistema.py
   +- INCIDENCIAS.md
   +- index.html
   +- README.md
   +- resultado_verificacion.json
   \- verificar_sistema.py
```

## Archivos del proyecto

### proyecto
#### INCIDENCIAS.md

```markdown
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

```
#### index.html

```html
&lt;!doctype html&gt;
&lt;html lang="es"&gt;
  &lt;head&gt;
    &lt;meta charset="utf-8"&gt;
    &lt;meta name="viewport" content="width=device-width, initial-scale=1"&gt;
    &lt;title&gt;Integra Tech | Crimson&lt;/title&gt;
    &lt;link rel="stylesheet" href="css/estilo.css"&gt;
  &lt;/head&gt;
  &lt;body&gt;
    &lt;header&gt;
      &lt;div&gt;
        &lt;p class="etiqueta"&gt;SGE · RA1&lt;/p&gt;
        &lt;h1&gt;Integra Tech | Crimson&lt;/h1&gt;
        &lt;p&gt;Estudio sencillo de sistemas ERP-CRM para Integra Tech Consulting.&lt;/p&gt;
      &lt;/div&gt;
    &lt;/header&gt;

    &lt;section class="distribucion"&gt;
      &lt;nav aria-label="Secciones"&gt;
        &lt;a href="#resumen"&gt;Resumen&lt;/a&gt;
        &lt;a href="#comparacion"&gt;Comparación&lt;/a&gt;
        &lt;a href="#seleccion"&gt;Selección&lt;/a&gt;
        &lt;a href="#verificacion"&gt;Verificación&lt;/a&gt;
        &lt;a href="#incidencias"&gt;Incidencias&lt;/a&gt;
      &lt;/nav&gt;

      &lt;main&gt;
        &lt;section id="resumen"&gt;
          &lt;h2&gt;Sistemas estudiados&lt;/h2&gt;
          &lt;div id="tarjetas" class="tarjetas"&gt;&lt;/div&gt;
        &lt;/section&gt;

        &lt;section id="comparacion"&gt;
          &lt;h2&gt;Comparación ERP-CRM&lt;/h2&gt;
          &lt;div class="tabla-contenedor"&gt;
            &lt;table&gt;
              &lt;thead&gt;
                &lt;tr&gt;&lt;th&gt;Sistema&lt;/th&gt;&lt;th&gt;Licencia&lt;/th&gt;&lt;th&gt;Sistema operativo&lt;/th&gt;&lt;th&gt;Base de datos&lt;/th&gt;&lt;/tr&gt;
              &lt;/thead&gt;
              &lt;tbody id="tabla-sistemas"&gt;&lt;/tbody&gt;
            &lt;/table&gt;
          &lt;/div&gt;
        &lt;/section&gt;

        &lt;section id="seleccion" class="destacado"&gt;
          &lt;p class="etiqueta"&gt;Decisión razonada&lt;/p&gt;
          &lt;h2&gt;Continuar con Integra Tech Platform&lt;/h2&gt;
          &lt;p&gt;La empresa ya dispone de un ERP-CRM propio con clientes, proyectos,
          facturación y módulos SaaS. Mantener Python, FastAPI y PostgreSQL evita
          una migración innecesaria y conserva el control sobre la adaptación.&lt;/p&gt;
        &lt;/section&gt;

        &lt;section id="verificacion"&gt;
          &lt;h2&gt;Verificación del equipo&lt;/h2&gt;
          &lt;p&gt;Ejecuta &lt;code&gt;python verificar_sistema.py&lt;/code&gt; y recarga esta página.&lt;/p&gt;
          &lt;div id="resultado" class="resultado"&gt;Resultado pendiente.&lt;/div&gt;
        &lt;/section&gt;

        &lt;section id="incidencias"&gt;
          &lt;h2&gt;Incidencias&lt;/h2&gt;
          &lt;p&gt;Las incidencias y su resolución se registran en &lt;a href="INCIDENCIAS.md"&gt;INCIDENCIAS.md&lt;/a&gt;.&lt;/p&gt;
        &lt;/section&gt;
      &lt;/main&gt;
    &lt;/section&gt;

    &lt;footer&gt;Integra Tech Consulting · Proyecto académico con datos técnicos, sin datos de clientes&lt;/footer&gt;
    &lt;script src="js/aplicacion.js"&gt;&lt;/script&gt;
  &lt;/body&gt;
&lt;/html&gt;

```
#### README.md

~~~markdown
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


~~~
#### resultado\_verificacion.json

```json
{
  "sistema": "Prototipo local Integra Tech Crimson",
  "correcto": true,
  "comprobaciones": [
    {
      "nombre": "Sistema operativo",
      "correcto": true,
      "detalle": "Windows 10"
    },
    {
      "nombre": "Python",
      "correcto": true,
      "detalle": "3.11.9"
    },
    {
      "nombre": "SQLite",
      "correcto": true,
      "detalle": "versión 3.45.1; integridad=ok, registros=1"
    },
    {
      "nombre": "Archivo index.html",
      "correcto": true,
      "detalle": "encontrado"
    },
    {
      "nombre": "Archivo css/estilo.css",
      "correcto": true,
      "detalle": "encontrado"
    },
    {
      "nombre": "Archivo js/aplicacion.js",
      "correcto": true,
      "detalle": "encontrado"
    },
    {
      "nombre": "Archivo datos/sistemas.json",
      "correcto": true,
      "detalle": "encontrado"
    }
  ]
}

```
#### verificar\_sistema.py

```python
"""Comprueba el entorno local usado para ejecutar el prototipo Crimson."""

import json
import platform
import sqlite3
import sys
import tempfile
from pathlib import Path


RAIZ = Path(__file__).resolve().parent


def comprobar_sqlite():
    """Crea una base temporal y ejecuta la comprobación de integridad."""
    with tempfile.TemporaryDirectory() as temporal:
        ruta = Path(temporal) / "prueba.db"
        conexion = sqlite3.connect(ruta)
        try:
            conexion.execute("CREATE TABLE clientes (id INTEGER PRIMARY KEY, nombre TEXT)")
            conexion.execute("INSERT INTO clientes (nombre) VALUES (?)", ("Cliente ficticio",))
            integridad = conexion.execute("PRAGMA integrity_check").fetchone()[0]
            cantidad = conexion.execute("SELECT COUNT(*) FROM clientes").fetchone()[0]
        finally:
            conexion.close()
    return integridad == "ok" and cantidad == 1, f"integridad={integridad}, registros={cantidad}"


def verificar(requisitos):
    """Devuelve comprobaciones simples y reproducibles del equipo."""
    sistema = platform.system()
    version_python = sys.version_info[:3]
    version_sqlite = tuple(int(numero) for numero in sqlite3.sqlite_version.split("."))
    sqlite_correcto, detalle_sqlite = comprobar_sqlite()

    comprobaciones = [
        {
            "nombre": "Sistema operativo",
            "correcto": sistema in requisitos["sistemas_operativos"],
            "detalle": f"{sistema} {platform.release()}",
        },
        {
            "nombre": "Python",
            "correcto": version_python >= tuple(requisitos["python_minimo"]),
            "detalle": platform.python_version(),
        },
        {
            "nombre": "SQLite",
            "correcto": version_sqlite >= tuple(requisitos["sqlite_minimo"]) and sqlite_correcto,
            "detalle": f"versión {sqlite3.sqlite_version}; {detalle_sqlite}",
        },
    ]
    for archivo in requisitos["archivos_obligatorios"]:
        comprobaciones.append(
            {
                "nombre": f"Archivo {archivo}",
                "correcto": (RAIZ / archivo).is_file(),
                "detalle": "encontrado" if (RAIZ / archivo).is_file() else "no encontrado",
            }
        )
    return {
        "sistema": requisitos["sistema"],
        "correcto": all(item["correcto"] for item in comprobaciones),
        "comprobaciones": comprobaciones,
    }


def main():
    requisitos = json.loads((RAIZ / "config" / "requisitos.json").read_text(encoding="utf-8"))
    resultado = verificar(requisitos)
    destino = RAIZ / "resultado_verificacion.json"
    destino.write_text(json.dumps(resultado, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    return 0 if resultado["correcto"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

```
#### config
##### requisitos.json

```json
{
  "sistema": "Prototipo local Integra Tech Crimson",
  "sistemas_operativos": ["Windows", "Linux", "Darwin"],
  "python_minimo": [3, 10],
  "sqlite_minimo": [3, 35, 0],
  "archivos_obligatorios": [
    "index.html",
    "css/estilo.css",
    "js/aplicacion.js",
    "datos/sistemas.json"
  ]
}

```
#### css
##### estilo.css

```css
:root {
  --principal: #b51232;
  --oscuro: #171a22;
  --fondo: #f4f5f7;
  --blanco: #ffffff;
  --texto-suave: #5b6270;
  --correcto: #247a4a;
}

* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--fondo); color: var(--oscuro); font-family: Arial, sans-serif; }
header, footer { padding: 24px clamp(20px, 5vw, 70px); background: var(--principal); color: var(--blanco); }
header h1 { margin: 4px 0; }
.etiqueta { margin: 0; font-size: 12px; font-weight: bold; letter-spacing: .12em; text-transform: uppercase; }
.distribucion { display: grid; grid-template-columns: 210px 1fr; min-height: calc(100vh - 190px); }
nav { padding: 24px 14px; background: var(--oscuro); }
nav a { display: block; margin-bottom: 9px; padding: 11px; background: var(--blanco); color: var(--principal); text-decoration: none; }
main { width: min(1100px, 100%); padding: 30px; }
main > section { margin-bottom: 42px; }
.tarjetas { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; }
.tarjeta, .resultado, .destacado { padding: 20px; border-left: 5px solid var(--principal); background: var(--blanco); }
.tarjeta h3 { margin-top: 0; }
.tarjeta p { color: var(--texto-suave); }
.tarjeta a { color: var(--principal); font-weight: bold; }
.tabla-contenedor { overflow-x: auto; }
table { width: 100%; border-collapse: collapse; background: var(--blanco); }
th, td { padding: 12px; border-bottom: 1px solid #dfe1e6; text-align: left; vertical-align: top; }
th { background: var(--principal); color: var(--blanco); }
.destacado { background: #fff4f6; }
.comprobacion { margin: 8px 0; }
.correcto { color: var(--correcto); }
.error { color: var(--principal); }
footer { text-align: center; }

@media (max-width: 720px) {
  .distribucion { grid-template-columns: 1fr; }
  nav { display: flex; gap: 8px; overflow-x: auto; }
  nav a { margin: 0; white-space: nowrap; }
  main { padding: 20px; }
}

```
#### datos
##### sistemas.json

```json
[
  {
    "nombre": "Integra Tech Platform",
    "tipo": "ERP y CRM a medida",
    "licencia": "Código privado de Integra Tech Consulting",
    "sistema_operativo": "Linux en servidor; navegador en el cliente",
    "gestor_datos": "PostgreSQL",
    "caracteristicas": "Clientes, proyectos, facturación, documentos y módulos SaaS",
    "requisitos": "Python, FastAPI, Uvicorn, psycopg2 y PostgreSQL",
    "encaje": "Seleccionado: ya está implantado y permite adaptación directa",
    "fuente": "https://github.com/IntTecCon/integra-tech-platform"
  },
  {
    "nombre": "Odoo 19",
    "tipo": "ERP y CRM modular",
    "licencia": "Community LGPLv3; Enterprise con licencia comercial",
    "sistema_operativo": "Linux, Windows o macOS en instalación desde código",
    "gestor_datos": "PostgreSQL 13 o posterior",
    "caracteristicas": "Amplio catálogo de aplicaciones y módulos",
    "requisitos": "Python 3.10 o posterior y PostgreSQL",
    "encaje": "Alternativa completa, con coste de migración y adaptación",
    "fuente": "https://www.odoo.com/documentation/19.0/administration/on_premise/source.html"
  },
  {
    "nombre": "ERPNext",
    "tipo": "ERP con CRM integrado",
    "licencia": "GPLv3",
    "sistema_operativo": "Servidor Linux; se recomienda Ubuntu LTS",
    "gestor_datos": "MariaDB",
    "caracteristicas": "Ventas, compras, inventario, contabilidad y proyectos",
    "requisitos": "Frappe Framework, MariaDB y servicios de caché y colas",
    "encaje": "Código abierto, pero exige migrar el desarrollo actual",
    "fuente": "https://docs.frappe.io/legal/others/license-and-trademark"
  },
  {
    "nombre": "Dynamics 365 Business Central",
    "tipo": "ERP comercial en la nube o local",
    "licencia": "Suscripción por usuario, dispositivo o tenant",
    "sistema_operativo": "Servicio cloud accesible con navegador; Windows en despliegue local",
    "gestor_datos": "Azure SQL en cloud; SQL Server o Azure SQL en migraciones locales",
    "caracteristicas": "Finanzas, ventas, operaciones, proyectos e integración Microsoft",
    "requisitos": "Tenant Microsoft Entra para cloud; infraestructura Microsoft en local",
    "encaje": "Administración gestionada, con dependencia y coste de licencias",
    "fuente": "https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/deployment/deployment"
  }
]

```
#### js
##### aplicacion.js

```javascript
async function cargarJson(ruta) {
  const respuesta = await fetch(ruta);
  if (!respuesta.ok) throw new Error(`No se pudo cargar ${ruta}`);
  return respuesta.json();
}

function textoSeguro(valor) {
  const elemento = document.createElement("span");
  elemento.textContent = valor;
  return elemento.innerHTML;
}

async function mostrarSistemas() {
  const sistemas = await cargarJson("datos/sistemas.json");
  const tarjetas = document.querySelector("#tarjetas");
  const tabla = document.querySelector("#tabla-sistemas");

  tarjetas.innerHTML = sistemas.map(sistema => `
    <article class="tarjeta">
      <h3>${textoSeguro(sistema.nombre)}</h3>
      <p><strong>${textoSeguro(sistema.tipo)}</strong></p>
      <p>${textoSeguro(sistema.caracteristicas)}</p>
      <a href="${textoSeguro(sistema.fuente)}" target="_blank" rel="noopener">Fuente oficial</a>
    </article>
  `).join("");

  tabla.innerHTML = sistemas.map(sistema => `
    <tr>
      <td>${textoSeguro(sistema.nombre)}</td>
      <td>${textoSeguro(sistema.licencia)}</td>
      <td>${textoSeguro(sistema.sistema_operativo)}</td>
      <td>${textoSeguro(sistema.gestor_datos)}</td>
    </tr>
  `).join("");
}

async function mostrarVerificacion() {
  const contenedor = document.querySelector("#resultado");
  try {
    const resultado = await cargarJson("resultado_verificacion.json");
    const clase = resultado.correcto ? "correcto" : "error";
    contenedor.innerHTML = `<strong class="${clase}">${resultado.correcto ? "Configuración correcta" : "Revisión necesaria"}</strong>`;
    resultado.comprobaciones.forEach(comprobacion => {
      const linea = document.createElement("p");
      linea.className = `comprobacion ${comprobacion.correcto ? "correcto" : "error"}`;
      linea.textContent = `${comprobacion.correcto ? "✓" : "✗"} ${comprobacion.nombre}: ${comprobacion.detalle}`;
      contenedor.appendChild(linea);
    });
  } catch (error) {
    contenedor.textContent = "Ejecuta el verificador desde un servidor local para actualizar el resultado.";
  }
}

mostrarSistemas().catch(error => document.querySelector("#tarjetas").textContent = error.message);
mostrarVerificacion();

```
#### tests
##### \_\_init\_\_.py

```python
"""Pruebas automáticas del proyecto Integra Tech Crimson."""

```
##### test\_verificar\_sistema.py

```python
import unittest

from verificar_sistema import verificar


class PruebasVerificador(unittest.TestCase):
    def test_configuracion_valida(self):
        requisitos = {
            "sistema": "prueba",
            "sistemas_operativos": ["Windows", "Linux", "Darwin"],
            "python_minimo": [3, 10],
            "sqlite_minimo": [3, 35, 0],
            "archivos_obligatorios": ["index.html", "datos/sistemas.json"],
        }
        resultado = verificar(requisitos)
        self.assertTrue(resultado["correcto"])
        self.assertTrue(all(item["correcto"] for item in resultado["comprobaciones"]))

    def test_detecta_archivo_ausente(self):
        requisitos = {
            "sistema": "prueba",
            "sistemas_operativos": ["Windows", "Linux", "Darwin"],
            "python_minimo": [3, 10],
            "sqlite_minimo": [3, 35, 0],
            "archivos_obligatorios": ["archivo-que-no-existe.txt"],
        }
        resultado = verificar(requisitos)
        self.assertFalse(resultado["correcto"])


if __name__ == "__main__":
    unittest.main()

```
