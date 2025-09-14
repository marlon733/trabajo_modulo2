import pytest
from ejercicio_13 import procesar_accion


def test_ir_al_norte_desde_entrada():
    ubicacion, llave, activo, msg = procesar_accion("entrada", "ir al norte", False)
    assert ubicacion == "pasillo"
    assert activo is True
    assert "pasillo" in msg.lower()

def test_buscar_en_pasillo_encuentra_llave():
    ubicacion, llave, activo, msg = procesar_accion("pasillo", "buscar", False)
    assert llave is True
    assert activo is True
    assert "llave" in msg.lower()

def test_abrir_cofre_con_llave():
    ubicacion, llave, activo, msg = procesar_accion("sala del cofre", "abrir cofre", True)
    assert activo is False
    assert "tesoro" in msg.lower()


def test_abrir_cofre_sin_llave():
    ubicacion, llave, activo, msg = procesar_accion("sala del cofre", "abrir cofre", False)
    assert activo is False
    assert "cerrado" in msg.lower()