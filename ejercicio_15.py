import random

def crear_tablero():
    return [["~" for _ in range(5)] for _ in range(5)]

def colocar_barco():
    orientacion = random.choice(["horizontal", "vertical"])
    barco = []

    if orientacion == "horizontal":
        fila = random.randint(0, 4)
        inicio_col = random.randint(0, 2)
        barco = [(fila, inicio_col + i) for i in range(3)]
    else:
        col = random.randint(0, 4)
        inicio_fila = random.randint(0, 2)
        barco = [(inicio_fila + i, col) for i in range(3)]

    return barco

def convertir_coordenada(coordenada, letras_filas=["A", "B", "C", "D", "E"]):
    if len(coordenada) != 2:
        return None
    fila_letra = coordenada[0].upper()
    col_str = coordenada[1]

    if fila_letra in letras_filas and col_str.isdigit():
        fila = letras_filas.index(fila_letra)
        col = int(col_str) - 1
        if 0 <= col < 5:
            return (fila, col)
    return None

def mostrar_tablero(tablero, letras_filas=["A", "B", "C", "D", "E"]):
    print("  1 2 3 4 5")
    for i, fila in enumerate(tablero):
        print(letras_filas[i], " ".join(fila))

def jugar_batalla_naval():

    tablero = crear_tablero()
    barco = colocar_barco()
    disparos_realizados = set()
    partes_tocadas = set()
    turnos = 10

    print(" Bienvenido a Batalla Naval")
    print("Tienes 10 turnos para hundir el barco de 3 casillas.\n")

    while turnos > 0:
        mostrar_tablero(tablero)
        print(f"Turnos restantes: {turnos}")
        coordenada = input("Dispara a una coordenada (ej: A3): ").strip()

        objetivo = convertir_coordenada(coordenada)
        if not objetivo:
            print(" Entrada inválida. Usa formato como 'B2'.")
            continue

        if objetivo in disparos_realizados:
            print(" Ya disparaste ahí. Intenta otra coordenada.")
            continue

        disparos_realizados.add(objetivo)

        if objetivo in barco:
            tablero[objetivo[0]][objetivo[1]] = "X"
            partes_tocadas.add(objetivo)
            print("Tocado")
        else:
            tablero[objetivo[0]][objetivo[1]] = "O"
            print(" Agua.")

        if len(partes_tocadas) == 3:
            print("\n Hundiste el barco Ganaste")
            mostrar_tablero(tablero)
            return

        turnos -= 1

    print("\n Se acabaron los turnos. Has perdido")
    print("La ubicación del barco era:")
    for fila, col in barco:
        tablero[fila][col] = "B"
    mostrar_tablero(tablero)


def main(value=None):
    tablero = crear_tablero()
    barco = colocar_barco()
    return tablero, barco

if __name__ == "__main__":
    main()
