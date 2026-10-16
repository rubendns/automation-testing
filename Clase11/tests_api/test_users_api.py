import pytest
import requests


@pytest.mark.api
def test_obtener_usuarios():
    url = "https://reqres.in/api/users?page=2"

    respuesta = requests.get(url, timeout=10)

    # Verificar que la petición fue exitosa
    assert respuesta.status_code == 200

    # Verificar que la API devuelve JSON
    assert "application/json" in respuesta.headers.get("Content-Type", "")

    # Convertir el JSON a un diccionario
    datos = respuesta.json()

    # Verificar que recibimos la página solicitada
    assert datos["page"] == 2

    # Verificar que hay usuarios
    assert len(datos["data"]) > 0

    # Verificar la estructura de cada usuario
    for usuario in datos["data"]:
        assert "id" in usuario
        assert "email" in usuario
        assert "first_name" in usuario
        assert "last_name" in usuario

        # Validar el contenido de los datos
        assert usuario["id"] > 0
        assert usuario["email"].endswith("@reqres.in")
        assert len(usuario["first_name"]) > 0
        assert len(usuario["last_name"]) > 0

        # Validar el formato de la imagen de perfil
        assert usuario["avatar"].endswith(".jpg")
