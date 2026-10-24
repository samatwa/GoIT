import heapq

def merge_k_lists_1(lists):
    # Мін-купа для зберігання елементів
    min_heap = []
    
    # Ініціалізація мін-купи з перших елементів кожного списку разом з індексами списків і індексами елементів
    for i, lst in enumerate(lists):
        if lst:  # Перевірка на порожній список
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    merged_list = []
    
    # Поки мін-купа не порожня
    while min_heap:
        # Витягуємо найменший елемент з мін-купи
        val, list_idx, element_idx = heapq.heappop(min_heap)
        merged_list.append(val)
        
        # Якщо існує наступний елемент у тому ж списку, додаємо його до мін-купи
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return merged_list

def merge_k_lists_2(lists):
    # Використовуємо heapq.merge для об'єднання всіх списків
    merged_list = list(heapq.merge(*lists))
    return merged_list

# Test
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list_1 = merge_k_lists_1(lists)
print("Merged list 1:", merged_list_1)
merged_list_2 = merge_k_lists_2(lists)
print("Merged list 2:", merged_list_2)
