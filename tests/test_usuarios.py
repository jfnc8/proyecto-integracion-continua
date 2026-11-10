
import json
import unittest
from urllib.request import urlopen


class TestUsuarios(unittest.TestCase):

    def test_usuarios_mysql(self):
        with urlopen("http://localhost:5000/usuarios", timeout=10) as respuesta:
            self.assertEqual(respuesta.status, 200)
            usuarios = json.load(respuesta)

        self.assertIsInstance(usuarios, list)

        usuarios_esperados = {
            ("Usuario Prueba 1", "usuario1@example.com"),
            ("Usuario Prueba 2", "usuario2@example.com"),
        }

        usuarios_obtenidos = {
            (usuario["nombre"], usuario["correo"])
            for usuario in usuarios
        }

        self.assertTrue(
            usuarios_esperados.issubset(usuarios_obtenidos),
            "Los usuarios no coinciden con los datos esperados"
        )


if __name__ == "__main__":
    unittest.main()

