# Automation Testing — Talento Tech

[![CI Automation Testing](https://github.com/rubendns/automation-testing/actions/workflows/ci.yml/badge.svg)](https://github.com/rubendns/automation-testing/actions/workflows/ci.yml)

## Descripción

Repositorio de prácticas del curso de QA Automation de Talento Tech.

Incluye ejercicios de automatización de pruebas de interfaz, pruebas de API, pruebas BDD e integración continua con GitHub Actions.

## Tecnologías utilizadas

- Python
- Pytest
- Selenium WebDriver
- Requests
- Behave (Gherkin)
- Git y GitHub
- GitHub Actions

## Instalación

Instalar las dependencias del proyecto:

```bash
python -m pip install -r requirements.txt
```

## Ejecutar pruebas

**Pruebas API:**

```bash
python -m pytest Clase12/tests_api/ -v
```

**Pruebas BDD:**

```bash
python -m behave Clase14/features/
```

**Prueba UI con logging:**

```bash
python -m pytest Clase13/tests_ui/test_captura_fallo.py -v
```

## Integración continua (CI)

El proyecto utiliza GitHub Actions para ejecutar automáticamente:

- Pruebas API con Pytest.
- Pruebas BDD de SauceDemo y operaciones matemáticas.
- Pruebas UI con Selenium en modo headless.
- Generación de reportes y logs.

Los resultados se pueden descargar desde la pestaña **Actions**, dentro del artefacto `reportes-clase15`.

## Reportes

- `pytest_report.html`: reporte HTML de pruebas API.
- `behave.json`: resultados de los escenarios BDD.
- `suite.log`: registro de ejecución de las pruebas.

## Autor

Proyecto desarrollado como parte del curso de QA Automation de Talento Tech.