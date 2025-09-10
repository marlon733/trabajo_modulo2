

def transponer_matriz_comprehension(matriz):
    """Devuelve la transpuesta de una matriz usando list comprehension"""
    return [[fila[i] for fila in matriz] for i in range(len(matriz[0]))]

def main():
    matriz = [[1, 2, 3], [4, 5, 6]]
    print("Transpuesta con list comprehension:", transponer_matriz_comprehension(matriz))

if __name__ == "__main__":
    main()
