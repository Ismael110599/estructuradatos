def find_max_min(arr):
    """
    Encuentra el valor máximo y mínimo de un arreglo.
    :param arr: List[int] - Arreglo de enteros.
    :return: Tuple[int, int] - (Max, Min)
    """
    if not arr:
        return None, None  # Si el arreglo está vacío, se devuelve None, None
    
    max_val = min_val = arr[0]  # Inicializamos con el primer valor del arreglo
    
    for num in arr:
        if num > max_val:
            max_val = num  # Actualizamos el valor máximo si encontramos un número mayor
        elif num < min_val:
            min_val = num  # Actualizamos el valor mínimo si encontramos un número menor
    
    return max_val, min_val

# Ejemplo de uso
if __name__ == "__main__":
    array = [3, 1, 9, 7, 5, 9]
    max_val, min_val = find_max_min(array)
    print(f"Maximo: {max_val}, Minimo: {min_val}")
