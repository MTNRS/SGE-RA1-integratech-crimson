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
