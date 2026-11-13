import pytest
from selenium import webdriver
from utils.logger import obtener_logger

logger = obtener_logger()


@pytest.fixture
def driver():
    navegador = webdriver.Chrome()
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
