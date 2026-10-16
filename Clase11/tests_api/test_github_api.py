import requests


def test_get_github_api():

    # Enviar una petición GET
    respuesta = requests.get(
        "https://api.github.com/",
        timeout=10
    )

    # Verificar el código de estado
    assert respuesta.status_code == 200

    # Verificar que recibimos JSON
    assert "application/json" in respuesta.headers["Content-Type"]

    # Convertir la respuesta a un diccionario
    datos = respuesta.json()

    # Verificar que existe el campo esperado
    assert "current_user_url" in datos

    # Verificar su contenido
    assert datos["current_user_url"] == "https://api.github.com/user"