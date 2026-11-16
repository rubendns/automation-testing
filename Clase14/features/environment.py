from pathlib import Path
from selenium import webdriver


def before_scenario(context, scenario):
    if "ui" in scenario.effective_tags:
        context.driver = webdriver.Chrome()
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
