import os
from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver
from utils.logger import obtener_logger

logger = obtener_logger()


@pytest.fixture
def driver():
    opciones = Options()

    if os.getenv("CI") == "true":
        opciones.add_argument("--headless=new")
        opciones.add_argument("--no-sandbox")
        opciones.add_argument("--disable-dev-shm-usage")
        opciones.add_argument("--window-size=1920,1080")

    navegador = webdriver.Chrome(options=opciones)

    yield navegador

    navegador.quit()


@pytest.mark.ui
def test_captura_automatica(driver):
    logger.info("Iniciando prueba UI")

    logger.info("Abriendo SauceDemo")
    driver.get("https://www.saucedemo.com/")

    logger.info("Verificando título de la página")

    try:
        assert "Swag Labs" in driver.title

    except AssertionError:
        logger.error("ERROR: El título de la página no es el esperado")
        raise

    logger.info("Prueba UI finalizada correctamente")
