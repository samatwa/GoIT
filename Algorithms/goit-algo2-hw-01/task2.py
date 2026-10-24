import random

def quick_select(arr: list, k: int) -> int:
    """
    Знаходить k-й найменший елемент у несортованому масиві за допомогою 
    алгоритму Quick Select з випадковим вибором опорного елемента.
    
    Args:
        arr: несортований масив чисел
        k: індекс найменшого елемента для пошуку (починаючи з 1)
        
    Returns:
        k-й найменший елемент масиву
    """
    # Перевіряємо, чи допустиме значення k
    if not 1 <= k <= len(arr):
        raise ValueError("k має бути в межах від 1 до довжини масиву")
    
    # Вибираємо випадковий опорний елемент для кращого розподілу
    pivot = random.choice(arr)
    
    # Поділяємо елементи на три частини
    lows = [el for el in arr if el < pivot]      # Елементи менші за опорний
    pivots = [el for el in arr if el == pivot]   # Елементи рівні опорному
    highs = [el for el in arr if el > pivot]     # Елементи більші за опорний
    
    # Визначаємо, в якій частині шукати k-й елемент
    if k <= len(lows):
        # Якщо k-й елемент у групі менших за опорний
        return quick_select(lows, k)
    elif k <= len(lows) + len(pivots):
        # Якщо k-й елемент - це один з опорних елементів
        return pivot
    else:
        # Якщо k-й елемент у групі більших за опорний
        # Коригуємо k: віднімаємо кількість елементів у lows та pivots
        return quick_select(highs, k - len(lows) - len(pivots))


# Приклади використання
test_arrays = [
    [5, 3, 8, 1, 9, 2, 7, 6, 4],  
    [10, 10, 10, 10],             
    [1],                          
    [5, 1],                       
    [-5, 10, 0, -10, 5]           
]

# Для відтворюваності результатів встановлюємо seed
random.seed(42)

for i, arr in enumerate(test_arrays):
    print(f"Масив {i+1}: {arr}")
    if len(arr) >= 3:
        print(f"3-й найменший елемент: {quick_select(arr[:], 3)}")
    
    print(f"1-й найменший елемент: {quick_select(arr[:], 1)}")
    print(f"{len(arr)}-й найменший елемент: {quick_select(arr[:], len(arr))}")
    print()