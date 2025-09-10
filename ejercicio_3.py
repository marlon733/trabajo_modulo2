

def validar_contraseña(contra):
    errores = []

    if len(contra) < 8:
        errores.append("Por favor ingrese una contraseña de al menos 8 caracteres.")
    if not any(char.isupper() for char in contra):
        errores.append("No se encuentra ninguna mayúscula. Ingrese la contraseña de nuevo.")
    if not any(char.isdigit() for char in contra):
        errores.append("No se encuentra ningún número. Ingrese la contraseña de nuevo.")
    if not any(char.islower() for char in contra):
        errores.append("No se encuentra ninguna minúscula. Ingrese la contraseña de nuevo.")

    return errores

def mostrar_errores(errores):
    print("\n".join(errores))
    print("Intente nuevamente.\n")

def main():
    mostrar_bienvenida()

    while True:
        contra = solicitar_contraseña()
        errores = validar_contraseña(contra)

        if not errores:
            print("¡Bien hecho! Contraseña bien escrita.")
            break
        else:
            mostrar_errores(errores)

if __name__ == "__main__":
    main()


