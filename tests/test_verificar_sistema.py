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
