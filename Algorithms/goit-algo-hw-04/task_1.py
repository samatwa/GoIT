import timeit
import random


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


def timsort(arr):
    arr.sort()

# Функція для заміру часу виконання


def measure_time(sort_func, arr):
    setup_code = f"from __main__ import {sort_func}, arr"
    stmt = f"{sort_func}(arr)"
    time = timeit.timeit(stmt, setup=setup_code, number=1)
    return time


# Створення різних наборів даних для тестування
sizes = [100, 1000, 10000]
for size in sizes:
    arr = [random.randint(0, size) for _ in range(size)]
    print(f"Array size: {size}")
    print("Merge Sort:", measure_time('merge_sort', arr))
    print("Insertion Sort:", measure_time('insertion_sort', arr))
    print("Timsort:", measure_time('timsort', arr))
    print()