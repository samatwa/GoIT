def greedy_algorithms(items, budget):
    # Сортуємо страви за спаданням співвідношення калорій до вартості
    sorted_items = sorted(items.items(), key=lambda item: item[1]['calories'] / item[1]['cost'], reverse = True)

    # Ініціалізуємо змінні
    total_cost = 0
    total_calories = 0
    selected_items = []

    # Обчислюємо загальну вартість і калорій
    for item, info in sorted_items:
        if total_cost + info['cost'] <= budget:
            selected_items.append(item)
            total_cost += info['cost']
            total_calories += info['calories']

    return selected_items, total_calories


def dynamic_programming(items, budget):
    # Створюємо таблицю для збереження максимальних калорій на кожний бюджет від 0 до budget
    dp = [0] * (budget + 1)
    selected_items = [[] for _ in range(budget + 1)]

    # Обчислюємо максимальні калорієнти на кожний бюджет
    for item, info in items.items():
        cost, calories = info['cost'], info['calories']
        for b in range(budget, cost -1, -1):
            if dp[b-cost] + calories > dp[b]:
                dp[b] = dp[b-cost] + calories
                selected_items[b] = selected_items[b-cost] + [item]

    # Визначаємо максимальний бюджет та максимальні калорієнти
    max_calories = dp[budget]
    selected_items = selected_items[budget]

    return selected_items, max_calories


def main():
    # Приклад використання
    budget = 100
    items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}
    # Використання алгоритмів
    selected_items_ga, total_calories = greedy_algorithms(items, budget)
    print(f"Greedy algorithm: \nselected items - {selected_items_ga}, \ntotal calories - {total_calories}")
    selected_items_dp, total_calories = dynamic_programming(items, budget)
    print(f"\nDynamic programming: \nselected items - {selected_items_dp}, \ntotal calories - {total_calories}")


if __name__ == "__main__":
    main()