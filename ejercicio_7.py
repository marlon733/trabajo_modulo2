def combinacion(estudiantes, notas):
    """
    Recibe dos listas estudiantes y notas.
    Devuelve un diccionario combinando cada estudiante con su respectiva nota.
    """
    if not isinstance(estudiantes, list) or not isinstance(notas, list):
        raise TypeError("Los parámetros deben ser listas")

    if len(estudiantes) != len(notas):
        raise ValueError("Las listas deben tener la misma longitud")

    reporte = dict(zip(estudiantes, notas))
    for est, nota in reporte.items():
        print(f"El {est} tiene una nota de {nota}")
    return reporte


def main(value=None):
    estudiantes = ["santiago", "cristian", "andres", "alejandro", "maron"]
    notas = ["20", "30", "40", "50", "38"]

    print(combinacion(estudiantes, notas))


if __name__ == "__main__":
    main()
