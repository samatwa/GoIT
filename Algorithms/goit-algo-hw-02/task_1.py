from queue import Queue

# Створити чергу заявок
queue = Queue()

# Функція для генерації нових заявок
def generate_request():
    # Створити нову заявку
    new_request = "New request"
    # Додати заявку до черги
    queue.put(new_request)
    print("Mew request has been created and added to the queue.")

# Функція для обробки заявок
def process_request():
    if not queue.empty():
        # Видалити заявку з черги
        request = queue.get()
        print(f"Request processed:: {request}")
    else:
        print("The queue is empty")

# Головний цикл програми
def main():
    try:
        while True:
            user_input = input("Press 'Enter' to generate a request (or 'q' to quit): ")
            if user_input.lower() == 'q':
                break
            generate_request()
            process_request()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
