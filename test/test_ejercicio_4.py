import pytest
from ejercicio4 import jugar_ronda

def test_empate_piedra():
    assert jugar_ronda("piedra", "piedra") == "empate"

def test_empate_papel():
    assert jugar_ronda("papel", "papel") == "empate"

def test_empate_tijera():
    assert jugar_ronda("tijera", "tijera") == "empate"

def test_gana_persona_piedra_contra_tijera():
    assert jugar_ronda("piedra", "tijera") == "persona"

def test_gana_persona_papel_contra_piedra():
    assert jugar_ronda("papel", "piedra") == "persona"

def test_gana_persona_tijera_contra_papel():
    assert jugar_ronda("tijera", "papel") == "persona"

def test_gana_computadora_tijera_contra_papel():
    assert jugar_ronda("papel", "tijera") == "computadora"

def test_gana_computadora_piedra_contra_papel():
    assert jugar_ronda("piedra", "papel") == "computadora"

def test_gana_computadora_tijera_contra_piedra():
    assert jugar_ronda("tijera", "piedra") == "computadora"
