from pathlib import Path

import pytest

from Clase10.pages.login_page import LoginPage
from Clase10.pages.inventory_page import InventoryPage
from Clase10.utils.datos import leer_json_productos


RUTA_JSON = Path(__file__).resolve().parents[1] / "datos" / "productos.json"

PRODUCTOS = leer_json_productos(RUTA_JSON)


@pytest.mark.parametrize("nombre_producto", PRODUCTOS)
def test_agregar_producto_desde_json(driver, nombre_producto):

    # Iniciar sesión en SauceDemo
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")

    # Agregar el producto indicado por el JSON
    inventario = InventoryPage(driver)
    inventario.agregar_producto_por_nombre(nombre_producto)

    # Comprobar el contador del carrito
    assert inventario.obtener_contador_carrito() == 1

    # Abrir el carrito
    carrito = inventario.ir_al_carrito()

    # Obtener los nombres de los productos agregados
    nombres_carrito = carrito.obtener_nombres_productos()

    # Verificar que se agregó el producto correcto
    assert nombre_producto in nombres_carrito

@pytest.mark.smoke
def test_carrito_smoke(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")

    inventario = InventoryPage(driver)
    inventario.agregar_primer_producto()

    assert inventario.obtener_contador_carrito() == 1

    carrito = inventario.ir_al_carrito()

    assert len(carrito.obtener_productos_en_carrito()) == 1