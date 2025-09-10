import pytest
from ejercicio_6 import encontrar_indices


def test_letra_repetida():
    assert encontrar_indices("banana", "a") == [1, 3, 5]

def test_letra_no_presente():
    assert encontrar_indices("python", "z") == []

def test_ignora_mayusculas_minusculas():
    assert encontrar_indices("Banana", "A") == [1, 3, 5]

def test_frase_no_es_string():
    with pytest.raises(TypeError):
        encontrar_indices(["b", "a", "n"], "a")

def test_letra_no_es_string():
    with pytest.raises(TypeError):
        encontrar_indices("banana", 1)

def test_ambos_parametros_invalidos():
    with pytest.raises(TypeError):
        encontrar_indices(None, None)
