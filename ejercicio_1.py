# ejercicio_1.py

def calcular_entrada(edad, estudiante):
    if edad < 12:
        precio = 10000
    elif edad < 17:
        precio = 15000
    elif edad < 100:
        precio = 20000
    else:
        raise ValueError("Edad no válida")

    if estudiante == "si":
        descuento = precio * 0.10
        return precio - descuento
    elif estudiante == "no":
        return precio
    else:
        raise ValueError("Respuesta inválida para estudiante")

def main():
    print("Bienvenido")
    try:
        nombre = input("Ingrese el nombre: ").strip().lower()
        edad = int(input("Ingrese la edad: "))
        estudiante = input("¿Eres estudiante? (si/no): ").strip().lower()
        total = calcular_entrada(edad, estudiante)
        print(f"{nombre}, debes pagar: ${total:.2f}")
    except ValueError:
        print("Por favor ingrese datos válidos")

if __name__ == "__main__":
    main()




