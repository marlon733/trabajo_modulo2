
from ejercicio_2 import procesar_opcion
import pytest

def test_guardar_archivo():
    assert procesar_opcion("guardar archivo") == "guardando archivo"

def test_buscar_archivo():
    assert procesar_opcion("buscar") == "buscando archivo"

def test_eliminar_archivo():
    assert procesar_opcion("eliminar archivo") == "eliminando archivo"

def test_salir():
    assert procesar_opcion("salir") == "saliendo"

def test_opcion_invalida():
    assert "Invalido" in procesar_opcion("opcion desconocida")

def test_mayusculas_y_espacios():
    """Debe ignorar mayúsculas y espacios extras"""
    assert procesar_opcion("   GUARDAR ARCHIVO   ") == "guardando archivo"
