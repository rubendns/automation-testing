from behave import given, when, then, use_step_matcher
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Usamos el parser normal para los pasos habituales.
use_step_matcher("parse")


@given("que el navegador abre la página de login")
def step_abrir_login(context):
    context.driver.get("https://www.saucedemo.com/")


# Cambiamos a expresiones regulares solamente para las credenciales.
use_step_matcher("re")


@when(r'ingreso usuario "(?P<username>[^"]*)" y clave "(?P<password>[^"]*)"')
def step_ingresar_credenciales(context, username, password):
    context.driver.find_element(By.ID, "user-name").send_keys(username)

    context.driver.find_element(By.ID, "password").send_keys(password)

    context.driver.find_element(By.ID, "login-button").click()


# IMPORTANTE: volvemos al parser normal ANTES de los @then.
use_step_matcher("parse")


@then('la URL contiene "{texto}"')
def step_validar_url(context, texto):
    WebDriverWait(context.driver, 10).until(EC.url_contains(texto))

    assert texto in context.driver.current_url


@then('veo el título "{titulo}"')
def step_validar_titulo(context, titulo):
    elemento = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "title"))
    )

    assert elemento.text == titulo


@then('veo el mensaje de error "{mensaje_esperado}"')
def step_validar_error_login(context, mensaje_esperado):
    elemento_error = WebDriverWait(context.driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '[data-test="error"]'))
    )

    mensaje_obtenido = elemento_error.text

    assert mensaje_esperado in mensaje_obtenido, (
        f"Esperaba encontrar: '{mensaje_esperado}', pero apareció: '{mensaje_obtenido}'"
    )
