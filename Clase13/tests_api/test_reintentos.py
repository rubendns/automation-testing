import pytest
import requests


@pytest.mark.api
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_api_con_reintentos():
    url = "https://jsonplaceholder.typicode.com/posts/1"

    respuesta = requests.get(url, timeout=10)

    assert respuesta.status_code == 200
    assert respuesta.json()["id"] == 1
