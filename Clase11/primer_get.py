import requests

# Dirección de la API que vamos a consultar
URL = "https://api.github.com/"

# Enviar una petición GET
respuesta = requests.get(URL, timeout=10)

# Mostrar el código de estado HTTP
print("Código de estado:", respuesta.status_code)

# Mostrar el tipo de contenido recibido
print("Tipo de contenido:", respuesta.headers.get("Content-Type"))

# Convertir el JSON recibido a un diccionario de Python
datos = respuesta.json()

# Mostrar un dato de la respuesta
print("URL del usuario actual:", datos["current_user_url"])