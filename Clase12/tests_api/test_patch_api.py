import pytest
import requests


@pytest.mark.api
@pytest.mark.regression
def test_actualizar_titulo_con_patch(post_by_id_url):
    url = post_by_id_url

    # Obtener los datos originales mediante GET
    respuesta_original = requests.get(url, timeout=10)

    assert respuesta_original.status_code == 200

    datos_originales = respuesta_original.json()

    # Preparar solamente el campo que queremos modificar
    payload = {"title": "Título actualizado por PATCH"}

    # Enviar la petición PATCH
    respuesta = requests.patch(url, json=payload, timeout=10)

    # Nivel 1: código de estado
    assert respuesta.status_code == 200

    # Nivel 2: cabeceras
    assert "application/json" in respuesta.headers.get("Content-Type", "")

    # Nivel 3: estructura JSON
    datos = respuesta.json()

    campos_esperados = {"id", "title", "body", "userId"}

    assert campos_esperados <= set(datos.keys())

    # Nivel 4: contenido
    assert datos["title"] == payload["title"]

    # Verificar que los campos no enviados conservan sus valores
    assert datos["id"] == datos_originales["id"]
    assert datos["body"] == datos_originales["body"]
    assert datos["userId"] == datos_originales["userId"]

    # Nivel 5: rendimiento
    tiempo_respuesta = respuesta.elapsed.total_seconds()

    print(f"\nTiempo de respuesta PATCH: {tiempo_respuesta:.3f} segundos")

    assert tiempo_respuesta < 1.5, f"PATCH tardó {tiempo_respuesta:.3f} segundos"
