def procesar_accion(ubicacion, accion, tiene_llave):
    """
    Procesa la acción del jugador y devuelve:
     nueva ubicación
     estado de la llave
     si el juego sigue activo
    mensaje a mostrar
    """
    accion = accion.lower().strip()

    if ubicacion == "entrada":
        if accion == "ir al norte":
            return "pasillo", tiene_llave, True, "Avanzas hacia el pasillo."
        elif accion == "salir":
            return "entrada", tiene_llave, False, "Has huido de la aventura. Juego terminado"
        else:
            return "entrada", tiene_llave, True, "Acción no reconocida."

    elif ubicacion == "pasillo":
        if accion == "ir al norte":
            return "sala del cofre", tiene_llave, True, "Avanzas hacia la sala del cofre."
        elif accion == "buscar":
            return "pasillo", True, True, "Encontraste una llave brillante"
        else:
            return "pasillo", tiene_llave, True, "Acción no reconocida."

    elif ubicacion == "sala del cofre":
        if accion == "abrir cofre":
            if tiene_llave:
                return "sala del cofre", tiene_llave, False, "Has abierto el cofre y encontrado el tesoro Ganaste"
            else:
                return "sala del cofre", tiene_llave, False, "El cofre está cerrado. Necesitas una llave."
        elif accion == "volver":
            return "pasillo", tiene_llave, True, "Regresas al pasillo."
        else:
            return "sala del cofre", tiene_llave, True, "Acción no reconocida."

    return ubicacion, tiene_llave, True, "Acción inválida."


def aventura_texto():
    ubicacion = "entrada"
    tiene_llave = False
    juego_activo = True

    print("Bienvenido a la Aventura del Cofre Mágico")
    print("Estás en la entrada de una cueva misteriosa...")

    while juego_activo:
        accion = input(f"Estás en {ubicacion}. ¿Qué haces?: ")
        ubicacion, tiene_llave, juego_activo, mensaje = procesar_accion(ubicacion, accion, tiene_llave)
        print(mensaje)


def main(value=None):
    aventura_texto()


if __name__ == "__main__":
    main()

