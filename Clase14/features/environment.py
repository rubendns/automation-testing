import os
from selenium.webdriver.chrome.options import Options
from pathlib import Path
from selenium import webdriver


def before_scenario(context, scenario):
    if "ui" in scenario.effective_tags:
        opciones = Options()

        if os.getenv("CI") == "true":
            opciones.add_argument("--headless=new")
            opciones.add_argument("--no-sandbox")
            opciones.add_argument("--disable-dev-shm-usage")
            opciones.add_argument("--window-size=1920,1080")

        context.driver = webdriver.Chrome(options=opciones)
        context.driver.maximize_window()


def after_scenario(context, scenario):
    if not hasattr(context, "driver"):
        return

    try:
        if scenario.status == "failed":
            carpeta = Path("Clase14/reports/screens")
            carpeta.mkdir(parents=True, exist_ok=True)

            nombre = "".join(
                caracter if caracter.isalnum() or caracter in "-_" else "_"
                for caracter in scenario.name
            )

            archivo = carpeta / f"{nombre}.png"
            context.driver.save_screenshot(str(archivo))

            print(f"\nCaptura de error guardada en: {archivo}")
    finally:
        context.driver.quit()
