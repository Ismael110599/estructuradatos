def selection_sort(arr):
    """
    Ordena un arreglo utilizando el algoritmo de Selection Sort.
    :param arr: List[int] - Arreglo de enteros.
    :return: List[int] - Arreglo ordenado.
    """
    n = len(arr)
    for i in range(n):
        min_index = i  # Inicializa el índice del valor mínimo en la posición actual
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # Si encontramos un valor menor que el mínimo actual
                min_index = j  # Actualizamos el índice del mínimo
        # Si min_index no es igual a i, solo hacemos el intercambio
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Selection Sort: {selection_sort(array)}")
