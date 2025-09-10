
def analizar_numero(numero: int) -> dict:

    if numero < 0:
        return {"negativo": True, "par": None, "multiplo_5": None}

    return {
        "negativo": False,
        "par": numero % 2 == 0,
        "multiplo_5": numero % 5 == 0,
    }


def main():
    print("Bienvenido")

    while True:
        try:
            numero = int(input("Ingrese un número: "))

            resultado = analizar_numero(numero)

            if resultado["negativo"]:
                print("El número es negativo. Intenta de nuevo.")
                continue

            print(f"{numero} es {'par' if resultado['par'] else 'no es par'}")
            print(
                f"{numero} es {'múltiplo de 5' if resultado['multiplo_5'] else 'no es múltiplo de 5'}"
            )

        except ValueError:
            print("Ese número es inválido. Intente nuevamente.")


if __name__ == "__main__":
    main()




