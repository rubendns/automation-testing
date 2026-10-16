import pytest
import requests


@pytest.mark.api
@pytest.mark.regression
def test_actualizar_post_con_put(post_by_id_url):
    url = post_by_id_url

    # Datos completos que queremos enviar
    payload = {
        "id": 1,
        "title": "Automation Testing Guide",
        "body": "Guía completa de testing automatizado",
        "userId": 1,
    }

    # Enviar la petición PUT
    respuesta = requests.put(url, json=payload, timeout=10)

    # Verificar el código de estado HTTP
    assert respuesta.status_code == 200

    # Nivel 2: verificar el tipo de contenido
    assert "application/json" in respuesta.headers.get("Content-Type", "")

    # Convertir la respuesta JSON
    datos = respuesta.json()

    # Nivel 3: verificar que estén todos los campos enviados
    campos_enviados = set(payload.keys())
    campos_recibidos = set(datos.keys())

    assert campos_enviados <= campos_recibidos

    # Verificar que la API devuelve los datos enviados
    assert datos["id"] == payload["id"]
    assert datos["title"] == payload["title"]
    assert datos["body"] == payload["body"]
    assert datos["userId"] == payload["userId"]

    # Nivel 5: medir el tiempo de respuesta
    tiempo_respuesta = respuesta.elapsed.total_seconds()

    print(f"\nTiempo de respuesta PUT: {tiempo_respuesta:.3f} segundos")

    assert tiempo_respuesta < 1.5, (
        f"PUT tardó {tiempo_respuesta:.3f} segundos"
    )  # podria fallar por latencia de la red
