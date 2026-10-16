import pytest
import requests

@pytest.mark.api
@pytest.mark.parametrize(
    "credenciales, codigo_esperado",
    [
        (
            {
                "email": "eve.holt@reqres.in",
                "password": "cityslicka"
            },
            200
        ),
        (
            {
                "email": "eve.holt@reqres.in"
            },
            400
        ),
    ],
    ids=["login_valido", "login_sin_password"]
)
def test_login_api(credenciales, codigo_esperado):

    url = "https://reqres.in/api/login"

    respuesta = requests.post(
        url,
        json=credenciales,
        timeout=10
    )

    # Verificar el código de estado esperado
    assert respuesta.status_code == codigo_esperado

    # Convertir la respuesta a un diccionario
    datos = respuesta.json()

    if codigo_esperado == 200:
        # Login exitoso: debe devolver un token
        assert "token" in datos
        assert len(datos["token"]) > 0

    else:
        # Login rechazado: debe devolver un error
        assert "error" in datos