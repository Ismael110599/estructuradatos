def bubble_sort(arr):
    """
    Ordena un arreglo utilizando bubble sort optimizado.
    :param arr: List[int] - Arreglo de enteros.
    :return: List[int] - Arreglo ordenado.
    """
    n = len(arr)
    for i in range(n):
        intercambiado = False  # Indicador para detectar si se hizo algún intercambio
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambio de elementos
                intercambiado = True
        if not intercambiado:
            break  # Si no hubo intercambio, el arreglo ya está ordenado
    return arr

# Ejemplo de uso
if __name__ == "__main__":
    array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Bubble Sort: {bubble_sort(array)}")
