import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_agregar_producto_carrito(driver):
    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login_completo("standard_user", "secret_sauce")

    # Acceder al inventario
    inventario = InventoryPage(driver)

    # Guardar el nombre del primer producto
    #productos_inventario = inventario.obtener_productos()
    #nombre_producto = (
    #    productos_inventario[0].find_element("class name", "inventory_item_name").text
    #)

    # mejoramos la busqueda de un producto
    nombre_producto = inventario.obtener_nombre_primer_producto()


    # Agregar el primer producto al carrito
    inventario.agregar_primer_producto()

    # Verificar el contador del carrito
    assert inventario.obtener_contador_carrito() == 1

    # Ir al carrito
    carrito = inventario.ir_al_carrito()

    # Verificar que haya un producto
    productos = carrito.obtener_productos_en_carrito()
    assert len(productos) == 1

    # Obtener los nombres de los productos
    nombres = carrito.obtener_nombres_productos()

    print("Productos en el carrito:", nombres)

    # Verificar que el producto agregado sea el correcto
    assert nombre_producto in nombres
