def obtener_positivos(numeros):
    return [n for n in numeros if n > 0]

def obtener_cuadrados(numeros):
    return [n**2 for n in numeros]

def clasificar_numeros(numeros):
    return ["positivo" if n > 0 else "negativo" for n in numeros]

def procesar_numeros(numeros):
    """
    Devuelve un diccionario con:
    - positivos
    - cuadrados
    - clasificacion
    """
    if not isinstance(numeros, list):
        raise TypeError("El parámetro debe ser una lista")
    if not all(isinstance(n, (int, float)) for n in numeros):
        raise ValueError("Todos los elementos deben ser números")

    return {
        "positivos": obtener_positivos(numeros),
        "cuadrados": obtener_cuadrados(numeros),
        "clasificacion": clasificar_numeros(numeros),
    }

def main():
    numeros = [-5, 10, -15, 20, -25, 30]
    resultado = procesar_numeros(numeros)

    print("Números positivos:", resultado["positivos"])
    print("Cuadrados:", resultado["cuadrados"])
    print("Clasificación:", resultado["clasificacion"])

if __name__ == "__main__":
    main()


