def mostrat_menu():
    menu = (
        "BIENVENIDO\n"
        "MENU:\n"
        "guardar archivo\n"
        "buscar\n"
        "eliminar archivo\n"
        "salir\n"
    )
    print(menu)

def procesar_opcion(opcion: str):
    opcion = opcion.strip().lower()
    match (opcion):
            case ("guardar archivo"):
                return ("guardando archivo")

            case ("buscar"):
                return("buscando archivo")

            case("eliminar archivo"):
                return("eliminando archivo")

            case ("salir"):
                return("saliendo")

            case _:
                return("Invalido,por favor ingrese un comando correcto")

def main():
    mostrat_menu()
    while True:
        entrada = input("Ingrese una de las opciones:  ")
        resultado = procesar_opcion(entrada)
        print(resultado)

        if resultado.strip().lower() == "saliendo":
            break


if __name__ == "__main__":
    main()
