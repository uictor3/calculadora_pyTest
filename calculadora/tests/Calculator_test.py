import pytest
from app.Calculator import Calculadora
import math

@pytest.fixture
def calculadora():
    return Calculadora()


def test_soma():
    calculadora = Calculadora()
    assert calculadora.soma(2, 3) == 5
    assert calculadora.soma(-1, 1) == 0
    assert calculadora.soma(-1, -1) == -2

def test_subtracao():
    calculadora = Calculadora()
    assert calculadora.subtracao(5, 3) == 2
    assert calculadora.subtracao(3, 5) == -2
    assert calculadora.subtracao(0, 0) == 0

def test_multiplicacao():
    calculadora = Calculadora()
    assert calculadora.multiplicacao(2, 3) == 6
    assert calculadora.multiplicacao(-2, 3) == -6
    assert calculadora.multiplicacao(0, 5) == 0

def test_divisao():
    calculadora = Calculadora()
    assert calculadora.divisao(6, 3) == 2
    assert calculadora.divisao(5, 2) == 2.5
    with pytest.raises(ValueError):
        calculadora.divisao(5, 0)

def test_potencia():
    calculadora = Calculadora()
    assert calculadora.potencia(2, 3) == 8
    assert calculadora.potencia(5, 0) == 1
    assert calculadora.potencia(10, -1) == 0.1

def test_fatorial_positivo():
    calculadora = Calculadora()
    assert calculadora.fatorial(5) == 120

def test_fatorial_zero():
    calculadora = Calculadora()
    assert calculadora.fatorial(0) == 1

def test_fatorial_negativo():
    calculadora = Calculadora()
    with pytest.raises(ValueError):
        calculadora.fatorial(-5)

def test_fatorial_decimal():
    calculadora = Calculadora()
    with pytest.raises(ValueError):
        calculadora.fatorial(5.5)

def test_raiz_quadrada_positivo():
    calculadora = Calculadora()
    assert calculadora.raiz_quadrada(9) == 3
    assert calculadora.raiz_quadrada(2) == math.sqrt(2)

def test_raiz_quadrada_negativo():
    calculadora = Calculadora()
    with pytest.raises(ValueError):
        calculadora.raiz_quadrada(-9)