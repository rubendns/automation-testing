import pytest
import pytest_html
from pathlib import Path
import base64


def pytest_html_report_title(report):
    report.title = "TalentoLab - Reporte de Testing Clase 13"


def pytest_html_results_table_header(cells):
    # Agregar una columna llamada URL
    cells.insert(2, "URL")


def pytest_html_results_table_row(report, cells):
    # Mostrar la URL registrada por el test
    cells.insert(2, getattr(report, "page_url", "-"))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Esperar el resultado de Pytest
    outcome = yield
    report = outcome.get_result()

    # Conservar la URL para el reporte HTML
    report.page_url = getattr(item, "page_url", "-")

    # Capturar solamente cuando falla el test
    if report.when == "call" and report.failed:
        # Buscar el navegador de Selenium
        driver = item.funcargs.get("driver")

        if driver is not None:
            # Crear la carpeta de capturas
            carpeta = Path("Clase13/reportes/screens")
            carpeta.mkdir(parents=True, exist_ok=True)

            # Crear la ruta de la imagen
            nombre_archivo = f"{item.name}.png"
            ruta = carpeta / nombre_archivo

            # Guardar la captura en el disco
            driver.save_screenshot(str(ruta))

            print(f"\nCaptura guardada en: {ruta}")

            # Obtener la captura en formato PNG

            imagen = driver.get_screenshot_as_png()

            # Convertir los bytes a Base64
            imagen_base64 = base64.b64encode(imagen).decode("utf-8")

            # Adjuntar la imagen al reporte HTML
            extras = getattr(report, "extras", [])
            extras.append(pytest_html.extras.png(imagen_base64))
            report.extras = extras
