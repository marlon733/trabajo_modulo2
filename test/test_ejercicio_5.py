import pytest
from ejercicio_5 import analizar_numero   # cambia "tu_archivo" por el nombre real de tu archivo .py

# --- Casos válidos ---
def test_numero_negativo():
    assert analizar_numero(-7) == {"negativo": True, "par": None, "multiplo_5": None}

def test_numero_par_multiplo_5():
    result = analizar_numero(10)
    assert result["negativo"] is False
    assert result["par"] is True
    assert result["multiplo_5"] is True

def test_numero_impar_no_multiplo_5():
    result = analizar_numero(7)
    assert result["negativo"] is False
    assert result["par"] is False
    assert result["multiplo_5"] is False

# --- Casos inválidos (deben lanzar TypeError) ---
def test_string_lanza_typeerror():
    with pytest.raises(TypeError):
        analizar_numero("hola")

def test_lista_lanza_typeerror():
    with pytest.raises(TypeError):
        analizar_numero([1, 2, 3])

def test_none_lanza_typeerror():
    with pytest.raises(TypeError):
        analizar_numero(None)
