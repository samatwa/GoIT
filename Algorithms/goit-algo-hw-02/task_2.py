from collections import deque

def is_palindrome(string):
    # Перетворюємо вхідний рядок в нижній регістр та видаляємо пробіли
    string = string.lower().replace(" ", "")
    
    # Створюємо двосторонню чергу та додаємо символи рядка в неї
    char_queue = deque()
    for char in string:
        char_queue.append(char)
    
    # Порівнюємо символи з обох кінців черги, поки черга не опустіється
    while len(char_queue) > 1:
        # Порівнюємо перший та останній елементи черги
        if char_queue.popleft() != char_queue.pop():
            return False # Якщо хоча б одна пара не співпадає, рядок не є паліндромом
    return True # Якщо усі пари співпадають, рядок є паліндромом

# Приклад використання:
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))