import csv
import json
from pathlib import Path


def leer_csv_login(ruta_archivo):
    """
    Lee un archivo CSV y devuelve una lista de tuplas
    para utilizar en tests parametrizados.
    """
    datos = []
    ruta = Path(ruta_archivo)

    with open(ruta, newline="", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)

        for fila in lector:
            debe_funcionar = fila["debe_funcionar"].lower() == "true"

            datos.append((
                fila["usuario"],
                fila["clave"],
                debe_funcionar
            ))

    return datos


def leer_json_productos(ruta_archivo):
    """
    Lee un archivo JSON y devuelve los nombres
    de los productos para parametrizar los tests.
    """
    with open(ruta_archivo, "r", encoding="utf-8") as archivo:
        productos = json.load(archivo)

    nombres = [producto["nombre"] for producto in productos]

    return nombres