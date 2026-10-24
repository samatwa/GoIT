import heapq


def min_cost_to_connect_cables(cable_lengths):
    # Створюємо мін-купу з довжин кабелів
    heapq.heapify(cable_lengths)
    print("Min cable heap:", cable_lengths)

    total_cost = 0
    merge_order = []

    # Поки в купі більше одного елемента
    while len(cable_lengths) > 1:
        # Витягуємо два найкоротші кабелі
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # Витрати на об'єднання двох кабелів
        cost = first + second
        total_cost += cost

        # Зберігаємо порядок об'єднання
        merge_order.append((first, second))

        # Поміщаємо новий кабель назад в купу
        heapq.heappush(cable_lengths, cost)

        # Виведення для демонстрації
        print(f"Merge {first} into {second} -> new cable: {cost}")
        print(f"Min cable heap:{cable_lengths}")

    return total_cost, merge_order


# Test
cables = [4, 3, 2, 6, 1, 9, 7, 8, 5]
total_cost, merge_order = min_cost_to_connect_cables(cables)
print("\nMerge order:", merge_order)
print("\nMin cost:", total_cost)
