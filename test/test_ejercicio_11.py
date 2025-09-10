import pytest
from ejercicio_11 import validar_cedula

def test_cedula_valida_par():
    """La suma de 2468 = 20 (par), debe ser válida"""
    assert validar_cedula("2468") is True

def test_cedula_valida_impar_suma_par():
    """La suma de 1357 = 16 (par), debe ser válida"""
    assert validar_cedula("1357") is True

def test_cedula_invalida_con_letra():
    """Contiene letra, debe ser inválida"""
    assert validar_cedula("12a4") is False

def test_cedula_vacia():
    """Cadena vacía -> suma = 0 -> par -> válida"""
    assert validar_cedula("") is True

def test_cedula_invalida_con_simbolo():
    """Contiene símbolo no numérico"""
    assert validar_cedula("123#") is False

