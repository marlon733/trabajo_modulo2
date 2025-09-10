
def validar_cedula(cedula_str):
    """
    Valida si la suma de los dígitos de la cédula es par.
    Retorna True si es válida, False si no.
    """
    suma = 0
    for digito in cedula_str:
        if digito.isdigit():
            suma += int(digito)
        else:
            return False
    return suma % 2 == 0
def main(value=None):
    while True:
        cedula = input("Ingrese su número de cédula: ")
        if validar_cedula(cedula):
            print(" Cédula válida. Bienvenido.")
            break
        else:
            print(" Cédula inválida. La suma de los dígitos debe ser par. Intente de nuevo.")
if __name__ == "__main__":
    main()