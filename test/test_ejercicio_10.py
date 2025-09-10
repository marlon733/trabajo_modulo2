
import pytest
from ejercici_10 import transponer_matriz_comprehension   # cambia tu_archivo por el nombre real


def test_matriz_rectangular():
    matriz = [[1, 2, 3], [4, 5, 6]]
    esperado = [[1, 4], [2, 5], [3, 6]]
    assert transponer_matriz_comprehension(matriz) == esperado

def test_matriz_cuadrada():
    matriz = [[1, 2], [3, 4]]
    esperado = [[1, 3], [2, 4]]
    assert transponer_matriz_comprehension(matriz) == esperado

def test_matriz_1xN():
    matriz = [[1, 2, 3, 4]]
    esperado = [[1], [2], [3], [4]]
    assert transponer_matriz_comprehension(matriz) == esperado




def test_filas_no_uniformes():

    with pytest.raises(IndexError):
        transponer_matriz_comprehension([[1, 2, 3], [4, 5]])
