from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given("que inicié sesión en SauceDemo como usuario estándar")
def step_login_usuario_estandar(context):
    context.driver.get("https://www.saucedemo.com/")

    context.driver.find_element(By.ID, "user-name").send_keys("standard_user")

    context.driver.find_element(By.ID, "password").send_keys("secret_sauce")

    context.driver.find_element(By.ID, "login-button").click()

    WebDriverWait(context.driver, 10).until(EC.url_contains("inventory.html"))


@when('agrego el producto "{nombre_producto}" al carrito')
def step_agregar_producto(context, nombre_producto):
    producto = WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                f'//div[contains(@class, "inventory_item")]'
                f'[.//*[contains(@class, "inventory_item_name") '
                f'and normalize-space()="{nombre_producto}"]]',
            )
        )
    )

    boton_agregar = producto.find_element(By.CSS_SELECTOR, "button.btn_inventory")

    boton_agregar.click()


@then("el carrito muestra {cantidad:d} producto")
def step_validar_carrito(context, cantidad):
    contador = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge"))
    )

    assert int(contador.text) == cantidad, (
        f"Esperaba {cantidad} producto(s), pero el carrito muestra {contador.text}"
    )
