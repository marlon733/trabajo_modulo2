def encontrar_indices(frase, letra):
    """
    Devuelve una lista con los índices donde aparece la letra en la frase.
    La búsqueda  entre mayúsculas y minúsculas.
    """
    if not isinstance(frase, str) or not isinstance(letra, str):
        raise TypeError("frase y letra deben ser cadenas de texto")

    return [i for i, caracter in enumerate(frase) if caracter.lower() == letra.lower()]


def main(value=None):
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese la letra: ")
    resultado = encontrar_indices(frase, letra)
    print(f"La letra '{letra}' aparece en las posiciones: {resultado}")


if __name__ == "__main__":
    main()