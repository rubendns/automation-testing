import pytest
import requests
from faker import Faker


fake = Faker("es_AR")


@pytest.mark.api
@pytest.mark.regression
def test_crear_post_con_faker(posts_url):
    # Generar datos de prueba
    payload = {
        "title": fake.sentence(nb_words=5),
        "body": fake.paragraph(nb_sentences=3),
        "userId": 1,
    }

    # Enviar una petición POST
    respuesta = requests.post(posts_url, json=payload, timeout=10)

    # Validar el código HTTP
    assert respuesta.status_code == 201

    # Validar el tipo de contenido
    assert "application/json" in respuesta.headers.get("Content-Type", "")

    # Convertir la respuesta a JSON
    datos = respuesta.json()

    # Validar la estructura y los tipos de datos
    assert isinstance(datos, dict)
    assert isinstance(datos["id"], int)
    assert isinstance(datos["title"], str)
    assert isinstance(datos["body"], str)
    assert isinstance(datos["userId"], int)

    # Validar los valores recibidos
    assert datos["title"] == payload["title"]
    assert datos["body"] == payload["body"]
    assert datos["userId"] == payload["userId"]

    # Medir el tiempo de respuesta
    tiempo_respuesta = respuesta.elapsed.total_seconds()

    print(f"\nTítulo generado: {payload['title']}")
    print(f"ID devuelto: {datos['id']}")
    print(f"Tiempo POST: {tiempo_respuesta:.3f} segundos")

    assert tiempo_respuesta < 3.0


@pytest.mark.api
@pytest.mark.regression
def test_actualizar_post_con_faker(post_by_id_url):
    # Generar un título nuevo
    nuevo_titulo = fake.sentence(nb_words=6)

    payload = {"title": nuevo_titulo}

    # Enviar PATCH a un post existente
    respuesta = requests.patch(post_by_id_url, json=payload, timeout=10)

    # Validar el estado HTTP
    assert respuesta.status_code == 200

    # Validar la cabecera
    assert "application/json" in respuesta.headers.get("Content-Type", "")

    datos = respuesta.json()

    # Validar estructura y tipos
    assert isinstance(datos, dict)
    assert isinstance(datos["id"], int)
    assert isinstance(datos["title"], str)

    # Validar el título actualizado
    assert datos["id"] == 1
    assert datos["title"] == nuevo_titulo

    # Medir rendimiento
    tiempo_respuesta = respuesta.elapsed.total_seconds()

    print(f"\nNuevo título: {nuevo_titulo}")
    print(f"Tiempo PATCH: {tiempo_respuesta:.3f} segundos")

    assert tiempo_respuesta < 3.0


@pytest.mark.api
@pytest.mark.regression
def test_eliminar_post_ejercicio(post_by_id_url):
    # Enviar la solicitud DELETE
    respuesta = requests.delete(post_by_id_url, timeout=10)

    # Nivel 1: código HTTP
    assert respuesta.status_code == 200

    # Nivel 2: cabeceras
    assert "application/json" in respuesta.headers.get("Content-Type", "")

    # Nivel 3 y 4: estructura y contenido
    datos = respuesta.json()

    assert isinstance(datos, dict)
    assert datos == {}

    # Nivel 5: rendimiento
    tiempo_respuesta = respuesta.elapsed.total_seconds()

    print(f"\nTiempo DELETE: {tiempo_respuesta:.3f} segundos")

    assert tiempo_respuesta < 3.0
