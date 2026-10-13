from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    # Localizadores de la página de inventario
    _TITLE = (By.CLASS_NAME, "title")
    _PRODUCTS = (By.CLASS_NAME, "inventory_item")
    _ADD_BUTTONS = (By.CSS_SELECTOR, "button[data-test*='add-to-cart']")
    _CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    _CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    _MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    _LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    # para mejor la localizacion de un producto
    _PRODUCT_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_titulo(self):
        """Obtiene el título de la página de inventario."""
        return self.driver.find_element(*self._TITLE).text

    def obtener_productos(self):
        """Obtiene la lista de productos disponibles."""
        return self.driver.find_elements(*self._PRODUCTS)

    # para mejorar la localizacion de un producto
    def obtener_nombre_primer_producto(self):
        """Obtiene el nombre del primer producto del inventario."""
        productos = self.obtener_productos()
        return productos[0].find_element(*self._PRODUCT_NAME).text
    

    def agregar_primer_producto(self):
        """Añade el primer producto disponible al carrito."""
        primer_boton = self.driver.find_elements(*self._ADD_BUTTONS)[0]
        primer_boton.click()
        return self

    def obtener_contador_carrito(self):
        """Obtiene el número de productos en el carrito."""
        try:
            badge = self.driver.find_element(*self._CART_BADGE)
            return int(badge.text)
        except:
            return 0

    def ir_al_carrito(self):
        """Navega a la página del carrito."""
        self.driver.find_element(*self._CART_LINK).click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def hacer_logout(self):
        """Cierra la sesión del usuario."""
        self.driver.find_element(*self._MENU_BUTTON).click()
        logout_link = self.wait.until(
            EC.element_to_be_clickable(self._LOGOUT_LINK)
        )
        logout_link.click()
        from pages.login_page import LoginPage
        return LoginPage(self.driver)