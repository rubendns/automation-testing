# Clase 9 — Page Object Model (POM)

## Objetivo

Aplicar el patrón de diseño **Page Object Model (POM)** para organizar las pruebas automatizadas con Selenium y Pytest.

El patrón POM permite separar las interacciones con las páginas web de las verificaciones realizadas por los tests, facilitando el mantenimiento y la reutilización del código.

## Aplicación utilizada

[SauceDemo](https://www.saucedemo.com/)

## Estructura del proyecto

```text
Clase09/
├── pages/
│   ├── __init__.py
│   ├── login_page.py
│   ├── inventory_page.py
│   └── cart_page.py
├── tests/
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
├── conftest.py
└── README.md
```

## Pruebas automatizadas

- **Login:** verifica que un usuario válido pueda iniciar sesión.
- **Catálogo:** verifica que se muestre el título y que existan productos.
- **Carrito:** agrega un producto y comprueba que aparezca en el carrito con el nombre esperado.

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- pytest-html
- Brave Browser

## Ejecución de pruebas

Desde la carpeta `Clase09`:

**Ejecutar todos los tests:**

```bash
python -m pytest tests/ -v
```

**Ejecutar solamente los tests smoke:**

```bash
python -m pytest tests/ -m smoke -v
```

**Generar un reporte HTML:**

```bash
python -m pytest tests/ -m smoke --html=preentrega_pom.html --self-contained-html -v
```

## Resultados

Las tres pruebas smoke se ejecutaron correctamente.

**Resultado:** 3 pruebas aprobadas.

Se generó el reporte `preentrega_pom.html` para visualizar los resultados en el navegador.

## Conceptos aplicados

- Patrón Page Object Model.
- Separación entre páginas y tests.
- Localizadores centralizados.
- Fixtures de Pytest.
- Marcadores `smoke`.
- Aserciones (`assert`).
- Generación de reportes HTML.