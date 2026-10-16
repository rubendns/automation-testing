import pytest
import requests


@pytest.mark.api
@pytest.mark.smoke
def test_eliminar_post(post_by_id_url):
    url = post_by_id_url

    # Enviar la petición DELETE
    respuesta = requests.delete(url, timeout=10)

    # Nivel 1: código de estado
    assert respuesta.status_code == 200

    # Nivel 2: cabeceras
    assert "application/json" in respuesta.headers.get("Content-Type", "")

    # Nivel 3 y 4: estructura y contenido
    datos = respuesta.json()

    assert isinstance(datos, dict)
    assert datos == {}

    # Nivel 5: rendimiento
    tiempo_respuesta = respuesta.elapsed.total_seconds()

    print(f"\nTiempo de respuesta DELETE: {tiempo_respuesta:.3f} segundos")

    assert tiempo_respuesta < 1.5, f"DELETE tardó {tiempo_respuesta:.3f} segundos"
