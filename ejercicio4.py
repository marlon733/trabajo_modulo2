
import random

def jugar_ronda(persona: str, computadora: str) -> str:
    """
    Devuelve el resultado de una ronda:
    "empate"
     "persona"
     "computadora"
    """
    if persona == computadora:
        return "empate"
    elif (persona == "piedra" and computadora == "tijera") or \
         (persona == "papel" and computadora == "piedra") or \
         (persona == "tijera" and computadora == "papel"):
        return "persona"
    else:
        return "computadora"


def main():
    victoria_persona = 0
    victoria_computadora = 0
    juego = ["piedra", "papel", "tijera"]

    print("JUEGO DE PIEDRA, PAPEL O TIJERA")
    while victoria_persona < 3 and victoria_computadora < 3:
        persona = input("Ingresa para jugar: ").lower().strip()
        if persona not in juego:
            print("Opción inválida. Intente nuevamente.\n")
            continue

        aleatorio = random.choice(juego)
        print(f"La computadora eligió {aleatorio}")
        resultado = jugar_ronda(persona, aleatorio)

        if resultado == "empate":
            print("Es un empate")
        elif resultado == "persona":
            print("¡Ganaste esta ronda!")
            victoria_persona += 1
        else:
            print("Gana la computadora")
            victoria_computadora += 1

        print(f"Marcador:\n Tú {victoria_persona}\n Computadora {victoria_computadora}")

    if victoria_persona == 3:
        print(" Felicidades, has ganado")
    else:
        print(" La computadora ganó")


if __name__ == "__main__":
    main()



