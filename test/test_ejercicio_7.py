import pytest
from ejercicio_7 import combinacion

def test_combinacion_correcta():
    estudiantes = ["a", "b", "c"]
    notas = ["10", "20", "30"]
    esperado = {"a": "10", "b": "20", "c": "30"}
    assert combinacion(estudiantes, notas) == esperado

def test_diccionario_vacio():
    assert combinacion([], []) == {}

def test_valores_numericos():
    estudiantes = ["ana", "luis"]
    notas = [100, 95]
    esperado = {"ana": 100, "luis": 95}
    assert combinacion(estudiantes, notas) == esperado


def test_error_parametros_no_listas():
    with pytest.raises(TypeError):
        combinacion("no_lista", ["10", "20"])

def test_error_longitudes_diferentes():
    estudiantes = ["ana", "luis"]
    notas = ["10"]
    with pytest.raises(ValueError):
        combinacion(estudiantes, notas)

def test_error_ambos_no_listas():
    with pytest.raises(TypeError):
        combinacion("ana", "10")
