from queue import Queue

# Створити чергу заявок
queue = Queue()

# Функція для генерації нових заявок
def generate_request():
    # Створити нову заявку
    new_request = "New Request"
    # Додати заявку до черги
    queue.put(new_request)
    print("Заявка створена та додана до черги.")

# Функція для обробки заявок
def process_request():
    if not queue.empty():
        # Видалити заявку з черги
        request = queue.get()
        print(f"Оброблено заявку: {request}")
    else:
        print("Черга заявок порожня.")

# Головний цикл програми
def main():
    while True:
        # Генерувати нові заявки
        generate_request()
        # Обробити заявки
        process_request()
        # Перерва між циклами (можна змінити за потребою)
        input("Натисніть Enter для продовження...")

if __name__ == "__main__":
    main()
