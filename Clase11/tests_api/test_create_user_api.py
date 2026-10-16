from datetime import datetime, timezone
import pytest
import requests


@pytest.mark.api
@pytest.mark.parametrize(
    "nombre, trabajo",
    [
        ("Matias QA", "tester"),
        ("Ana Lopez", "developer"),
        ("Carlos Perez", "analyst"),
    ],
)
def test_crear_usuario(nombre, trabajo):
    url = "https://reqres.in/api/users"

    # Preparar los datos del usuario
    nuevo_usuario = {"name": nombre, "job": trabajo}

    # Enviar una petición POST
    respuesta = requests.post(url, json=nuevo_usuario, timeout=10)

    # Verificar el código de estado
    assert respuesta.status_code == 201

    # Convertir la respuesta JSON
    datos = respuesta.json()

    # Verificar que la API devolvió los datos enviados
    assert datos["name"] == nombre
    assert datos["job"] == trabajo

    # Verificar los campos generados por la API
    assert "id" in datos
    assert "createdAt" in datos
