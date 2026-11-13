import pytest
import requests
from pytest_check import check


@pytest.mark.api
def test_soft_assertions_post():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    respuesta = requests.get(url, timeout=10)

    datos = respuesta.json()

    # Soft assertions: todas se comprueban
    check.equal(respuesta.status_code, 200)
    check.equal(datos["id"], 1)
    check.equal(datos["userId"], 1)
    check.is_true(len(datos["title"]) > 0)
    check.is_true(len(datos["body"]) > 0)
