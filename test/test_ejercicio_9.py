import pytest
from ejercici_9 import calcular_iva, calcular_precios_con_iva


def test_calculo_iva_un_producto():
    assert calcular_iva(100) == 119

def test_calculo_precios_varios_productos():
    productos = [
        {"nombre": "Camisa", "precio": 100},
        {"nombre": "Pantalón", "precio": 200},
    ]
    resultado = calcular_precios_con_iva(productos)
    assert resultado == {"Camisa": 119, "Pantalón": 238}

def test_calculo_iva_personalizado():
    productos = [{"nombre": "Zapatos", "precio": 100}]
    resultado = calcular_precios_con_iva(productos, iva=0.10)
    assert resultado == {"Zapatos": 110}

def test_parametro_no_lista():
    with pytest.raises(TypeError):
        calcular_precios_con_iva("no_lista")

def test_producto_invalido_falta_nombre():
    with pytest.raises(KeyError):
        calcular_precios_con_iva([{"precio": 100}])

def test_producto_invalido_falta_precio():
    with pytest.raises(KeyError):
        calcular_precios_con_iva([{"nombre": "Camisa"}])