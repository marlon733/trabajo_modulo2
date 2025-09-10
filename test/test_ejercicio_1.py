from ejercicio_1 import calcular_entrada
import pytest

def test_nino_sin_descuento():
    assert calcular_entrada(10, "no") == 10000

def test_adolescente_con_descuento():
    assert calcular_entrada(15, "si") == 13500

def test_adulto_con_descuento():
    assert calcular_entrada(30, "si") == 18000

def test_edad_invalida():
    with pytest.raises(ValueError):
        calcular_entrada(150, "no")

def test_respuesta_invalida():
    with pytest.raises(ValueError):
        calcular_entrada(20, "quizás")

