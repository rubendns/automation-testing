import pytest
import requests


@pytest.fixture
def sesion_api():
    # SETUP: preparar una sesión HTTP
    print("\nSETUP: Creando sesión API")

    sesion = requests.Session()

    # Entregar la sesión al test
    yield sesion

    # TEARDOWN: cerrar la sesión
    sesion.close()

    print("\nTEARDOWN: Sesión API cerrada")


@pytest.mark.api
def test_api_con_teardown(sesion_api):
    print("\nTEST: Consultando API")

    url = "https://jsonplaceholder.typicode.com/posts/1"

    respuesta = sesion_api.get(url, timeout=10)

    assert respuesta.status_code == 200
    assert respuesta.json()["id"] == 1
