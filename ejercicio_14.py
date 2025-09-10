import random

def seleccionar_palabra():
    palabras_secretas = ["python", "ahorcado", "programa", "desafio", "computador"]
    return random.choice(palabras_secretas)

def mostrar_tablero(palabra, letras_adivinadas):
    tablero = [letra if letra in letras_adivinadas else "_" for letra in palabra]
    return " ".join(tablero)   # 👈 ahora devuelve string en vez de imprimir

def validar_entrada(letra, letras_intentadas):
    if len(letra) != 1 or not letra.isalpha():
        return False, "Ingresa solo una letra válida."
    if letra in letras_intentadas:
        return False, "Ya intentaste esa letra."
    return True, ""

def jugar_ahorcado(interactivo=True, palabra=None):
    if palabra is None:
        palabra = seleccionar_palabra()

    letras_adivinadas = set()
    letras_intentadas = set()
    vidas = 6

    if interactivo:
        print("Bienvenido al juego del Ahorcado")
        print(f"Tienes {vidas} vidas para adivinar la palabra.")

    while vidas > 0:
        tablero = mostrar_tablero(palabra, letras_adivinadas)
        if interactivo:
            print("\nPalabra:", tablero)
            print("Letras intentadas:", ", ".join(sorted(letras_intentadas)))
            letra = input("Ingresa una letra: ").lower()
        else:
            break

        valido, msg = validar_entrada(letra, letras_intentadas)
        if not valido:
            if interactivo:
                print(msg)
            continue

        letras_intentadas.add(letra)

        if letra in palabra:
            letras_adivinadas.add(letra)
            if interactivo:
                print("Bien hecho La letra está en la palabra.")
        else:
            vidas -= 1
            if interactivo:
                print(f"a letra no está. Te quedan {vidas} vidas.")


        if all(letra in letras_adivinadas for letra in palabra):
            if interactivo:
                print("\nPalabra:", mostrar_tablero(palabra, letras_adivinadas))
                print("Felicidades Adivinaste la palabra.")
            return True

    if interactivo:
        print(f"Has perdido. La palabra era: {palabra}")
    return False

def main(value=None):
    if value == "test":

        return jugar_ahorcado(interactivo=False, palabra="python")
    else:
        jugar_ahorcado()

if __name__ == "__main__":
    main()
