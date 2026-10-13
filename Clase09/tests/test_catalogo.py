import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_catalogo_productos(driver):
    # Iniciar sesión
    login_page = LoginPage(driver)
    login_page.abrir()
    login_page.login_completo("standard_user", "secret_sauce")

    # Crear el objeto de inventario
    inventario = InventoryPage(driver)

    # Verificar el título
    assert inventario.obtener_titulo() == "Products"

    # Verificar que existan productos
    productos = inventario.obtener_productos()
    assert len(productos) > 0

    # Mostrar la cantidad de productos
    print("Cantidad de productos:", len(productos))