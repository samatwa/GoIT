def merge_k_lists(arr):
    if not arr:
        return []

    while len(arr) > 1:
        merged = []
        for i in range(0, len(arr), 2):
            if i + 1 < len(arr):
                merged.append(merge(arr[i], arr[i + 1]))
            else:
                merged.append(arr[i])
        arr = merged
    
    return arr[0]

def merge(left, right):
    merged = []
    left_index = right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted merged list:", merged_list)
