def calcular_iva(precio, iva=0.19):
    """Devuelve el precio con IVA incluido"""
    return round(precio * (1 + iva))

def calcular_precios_con_iva(productos, iva=0.19):
    """Recibe una lista de productos y devuelve un diccionario con IVA aplicado"""
    return {p["nombre"]: calcular_iva(p["precio"], iva) for p in productos}

def main():
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]

    productos_con_iva = calcular_precios_con_iva(productos)
    print("Productos con IVA incluido:")
    for nombre, precio in productos_con_iva.items():
        print(f"{nombre}: {precio}")

if __name__ == "__main__":
    main()

