import pytest
from ejercicio_3 import validar_contraseña

def test_contraseña_valida():
    """Debe devolver lista vacía cuando la contraseña cumple todas las condiciones"""
    assert validar_contraseña("Password1") == []

def test_contraseña_muy_corta():
    """Debe fallar si la contraseña tiene menos de 8 caracteres"""
    errores = validar_contraseña("Abc1")
    assert "al menos 8 caracteres" in errores[0]

def test_contraseña_sin_mayuscula():
    """Debe fallar si no hay mayúsculas"""
    errores = validar_contraseña("password1")
    assert any("mayúscula" in e for e in errores)

def test_contraseña_sin_minuscula():
    """Debe fallar si no hay minúsculas"""
    errores = validar_contraseña("PASSWORD1")
    assert any("minúscula" in e for e in errores)

def test_contraseña_sin_numero():
    """Debe fallar si no hay números"""
    errores = validar_contraseña("Password")
    assert any("número" in e for e in errores)

def test_contraseña_varios_errores():
    """Debe devolver múltiples errores cuando hay varias condiciones incumplidas"""
    errores = validar_contraseña("abc")
    assert len(errores) >= 3
    assert any("mayúscula" in e for e in errores)
    assert any("número" in e for e in errores)
    assert any("al menos 8 caracteres" in e for e in errores)
