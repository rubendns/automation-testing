import pytest
from pages.login_page import LoginPage


@pytest.mark.smoke
def test_login_exitoso(driver):
    login_page = LoginPage(driver)

    login_page.abrir()
    login_page.login_completo("standard_user", "secret_sauce")

    assert "/inventory.html" in driver.current_url
