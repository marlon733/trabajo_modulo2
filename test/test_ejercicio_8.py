import pytest
from ejercicio_8 import procesar_numeros

def test_lista_mixta():
    numeros = [-5, 10, -15]
    resultado = procesar_numeros(numeros)
    assert resultado["positivos"] == [10]
    assert resultado["cuadrados"] == [25, 100, 225]
    assert resultado["clasificacion"] == ["negativo", "positivo", "negativo"]

def test_lista_todos_positivos():
    numeros = [1, 2, 3]
    resultado = procesar_numeros(numeros)
    assert resultado["positivos"] == [1, 2, 3]
    assert resultado["clasificacion"] == ["positivo", "positivo", "positivo"]

def test_lista_vacia():
    numeros = []
    resultado = procesar_numeros(numeros)
    assert resultado["positivos"] == []
    assert resultado["cuadrados"] == []
    assert resultado["clasificacion"] == []


def test_parametro_no_lista():
    with pytest.raises(TypeError):
        procesar_numeros("no_es_lista")

def test_elemento_no_numerico():
    with pytest.raises(ValueError):
        procesar_numeros([1, "dos", 3])

def test_elemento_none():
    with pytest.raises(ValueError):
        procesar_numeros([1, None, 3])
