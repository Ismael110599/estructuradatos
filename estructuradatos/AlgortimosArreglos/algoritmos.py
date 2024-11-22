# Búsqueda del elemento mayor o menor en un arreglo usando una función más compacta
def buscar_mayor_menor(arr):
    if not arr:
        return None, None  # Devuelve None si el arreglo está vacío
    return max(arr), min(arr)  # Utiliza las funciones max() y min() de Python

# Bubble Sort (Implementación con optimización para detección de cambios)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):  # Solo iterar hasta n-1
        intercambio = False
        for j in range(n - 1 - i):  # Los últimos elementos ya están ordenados
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambio
                intercambio = True
        if not intercambio:  # Si no hubo intercambio, ya está ordenado
            break
    return arr

# Selection Sort (Usando un enfoque diferente para la selección del mínimo)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        # Encuentra el índice del valor mínimo en el arreglo no ordenado
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambiar el valor mínimo con el valor actual
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Pruebas
if __name__ == "__main__":
    datos = [74, 24, 15, 22, 42, 110, 80]
    print("Arreglo original:", datos)

    # Encontrar mayor y menor usando max() y min()
    mayor, menor = buscar_mayor_menor(datos)
    print(f"Mayor: {mayor}, Menor: {menor}")

    # Bubble Sort
    datos_bubble = datos[:]
    print("Ordenado con Bubble Sort:", bubble_sort(datos_bubble))

    # Selection Sort
    datos_selection = datos[:]
    print("Ordenado con Selection Sort:", selection_sort(datos_selection))
