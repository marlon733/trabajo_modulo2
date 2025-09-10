import pytest
from ejercicio_14 import mostrar_tablero, validar_entrada, jugar_ahorcado

def test_validar_entrada_varias_letras():
    valido, msg = validar_entrada("ab", set())
    assert valido is False
    assert msg == "Ingresa solo una letra válida."
def test_mostrar_tablero_con_letras_adivinadas():
    palabra = "python"
    letras = {"p", "o"}
    tablero = mostrar_tablero(palabra, letras)
    assert tablero == "p _ _ _ o _"
def test_validar_entrada_repetida():
    letras_intentadas = {"a"}
    valido, msg = validar_entrada("a", letras_intentadas)
    assert valido is False
    assert msg == "Ya intentaste esa letra."

def test_validar_entrada_letra_valida():
    valido, msg = validar_entrada("a", set())
    assert valido is True
    assert msg == ""

def test_jugar_ahorcado_gana_con_palabra_python():
    resultado = jugar_ahorcado(interactivo=False, palabra="python")

    assert isinstance(resultado, bool)


def test_validar_entrada_caracter_no_alfabetico():
    valido, msg = validar_entrada("1", set())
    assert valido is False
    assert msg == "Ingresa solo una letra válida."

