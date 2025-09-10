import random

def simular_dados(n_lanzamientos=10000):
    frecuencias = {}

    for _ in range(n_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2

        # Actualizar frecuencia usando get()
        frecuencias[suma] = frecuencias.get(suma, 0) + 1
    return frecuencias
def main(value=None):
    resultado = simular_dados()
    print("Frecuencia de cada suma (2 a 12):")
    for suma in range(2, 13):
        print(f"Suma {suma}: {resultado.get(suma, 0)} veces")


if __name__ == "__main__":
    main()
