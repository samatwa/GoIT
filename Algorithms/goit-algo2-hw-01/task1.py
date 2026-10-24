def find_min_max(arr: list) -> tuple:
    """
    Функція знаходить мінімальний та максимальний елементи в масиві 
    за допомогою методу "розділяй і володарюй".
    
    Args:
        arr: масив (список) чисел
        
    Returns:
        tuple (мінімум, максимум)
    """
    # Базовий випадок: масив з одного елемента
    if len(arr) == 1:
        return (arr[0], arr[0])
    
    # Базовий випадок: масив з двох елементів
    if len(arr) == 2:
        return (min(arr[0], arr[1]), max(arr[0], arr[1]))
    
    # Розділяємо масив на дві половини
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Рекурсивно знаходимо мінімуми та максимуми в обох половинах
    left_min, left_max = find_min_max(left_half)
    right_min, right_max = find_min_max(right_half)
    
    # Об'єднуємо результати
    return (min(left_min, right_min), max(left_max, right_max))

# Приклади використання:
test_arrays = [
    [5, 2, 9, 1, 7, 3, 8, 4, 6],
    [10],
    [4, 3],
    [-5, -10, 0, 5, 10],
    [7, 7, 7, 7]
]

for i, arr in enumerate(test_arrays):
    min_val, max_val = find_min_max(arr)
    print(f"Масив {i+1}: {arr}")
    print(f"Мінімум: {min_val}, Максимум: {max_val}")
    print()