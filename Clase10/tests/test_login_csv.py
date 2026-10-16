from pathlib import Path

import pytest

from Clase10.pages.login_page import LoginPage
from Clase10.utils.datos import leer_csv_login


# Ubicación del archivo de datos
RUTA_CSV = Path(__file__).resolve().parents[1] / "datos" / "login.csv"

# Cargar los casos de prueba
CASOS_LOGIN = leer_csv_login(RUTA_CSV)


@pytest.mark.parametrize(
    "usuario, clave, debe_funcionar",
    CASOS_LOGIN,
    ids=[
        "usuario_valido",
        "usuario_bloqueado",
        "usuario_con_problemas",
        "credenciales_invalidas",
    ],
)
def test_login_desde_csv(driver, usuario, clave, debe_funcionar):

    # Crear el Page Object
    login_page = LoginPage(driver)

    # Abrir SauceDemo
    login_page.abrir()

    # Intentar iniciar sesión
    login_page.login_completo(usuario, clave)

    # Verificar el resultado esperado
    if debe_funcionar:
        assert "/inventory.html" in driver.current_url
    else:
        assert login_page.esta_error_visible()

@pytest.mark.smoke
def test_login_usuario_valido_smoke(driver):
    login = LoginPage(driver)
    login.abrir()
    login.login_completo("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url