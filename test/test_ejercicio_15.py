import pytest
from ejercicio_15 import crear_tablero, colocar_barco, convertir_coordenada, main




def test_convertir_coordenada_fuera_rango():
    assert convertir_coordenada("A6") is None
    assert convertir_coordenada("F1") is None


def test_convertir_coordenada_formato_invalido():
    assert convertir_coordenada("AA") is None
    assert convertir_coordenada("3B") is None
    assert convertir_coordenada("") is None

def test_tablero_dimensiones():
    tablero, _ = main()
    assert len(tablero) == 5
    assert all(len(fila) == 5 for fila in tablero)

def test_barco_tres_casillas():
    _, barco = main()
    assert len(barco) == 3



def test_barco_dentro_tablero():
    _, barco = main()
    for fila, col in barco:
        assert 0 <= fila < 5
        assert 0 <= col < 5

def test_convertir_coordenada_valida():
    assert convertir_coordenada("A1") == (0, 0)
    assert convertir_coordenada("E5") == (4, 4)


