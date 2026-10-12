
import pytest
from Clase3.calculadora import sumar, restar, multiplicar, dividir


# Fixtures
@pytest.fixture
def numeros_enteros():
    return 20, 5

@pytest.fixture
def numeros_decimales():
    return 0.1, 0.2


# Tests de sumar
@pytest.mark.smoke
@pytest.mark.parametrize("a,b,esperado", [
    (2, 3, 5),
    (-2, -3, -5),
    (0, 5, 5)
])
def test_sumar(a, b, esperado):
    assert sumar(a, b) == esperado


@pytest.mark.smoke
def test_sumar_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert sumar(a, b) == pytest.approx(0.3)


# Tests de restar
@pytest.mark.parametrize("a,b,esperado", [
    (5, 3, 2),
    (10, 5, 5),
    (-2, -3, 1)
])
def test_restar(a, b, esperado):
    assert restar(a, b) == esperado


def test_restar_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert restar(b, a) == pytest.approx(0.1)


# Tests de multiplicar
def test_multiplicar(numeros_enteros):
    a, b = numeros_enteros
    assert multiplicar(a, b) == 100


def test_multiplicar_por_cero():
    assert multiplicar(5, 0) == 0


# Tests de dividir
def test_dividir(numeros_enteros):
    a, b = numeros_enteros
    assert dividir(a, b) == 4


@pytest.mark.exception
def test_dividir_por_cero():
    with pytest.raises(ValueError):
        dividir(10, 0)


def test_dividir_decimales(numeros_decimales):
    a, b = numeros_decimales
    assert dividir(a, b) == pytest.approx(0.5)
