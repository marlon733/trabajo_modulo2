import pytest
from ejercicio_12 import simular_dados


def test_frecuencias_suma_en_rango():
    """Todas las sumas deben estar entre 2 y 12"""
    resultado = simular_dados(1000)
    assert all(2 <= k <= 12 for k in resultado.keys())
def test_lanzamientos_float():
    """Si se pasa un float, debe fallar con TypeError"""
    with pytest.raises(TypeError):
        simular_dados(5.5)

def test_claves_incluyen_todos_los_posibles():
    """Deben existir todas las sumas posibles de 2 a 12 (aunque algunas con 0)"""
    resultado = simular_dados(100)
    for i in range(2, 13):
        assert i in resultado


def test_lanzamientos_no_entero():
    """Si se pasa un string, debe fallar con TypeError"""
    with pytest.raises(TypeError):
        simular_dados("mil")

def test_lanzamientos_negativos():
    """Si se pasa un número negativo, debe devolver un diccionario vacío"""
    resultado = simular_dados(-10)
    assert resultado == {}

def test_numero_total_lanzamientos():
    """La suma de frecuencias debe ser igual al número de lanzamientos"""
    n = 5000
    resultado = simular_dados(n)
    assert sum(resultado.values()) == n