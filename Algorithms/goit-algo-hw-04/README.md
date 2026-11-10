# goit-algo-hw-04

## Conclusions from task_1

1. **Scaling with array size.** All three sorting algorithms take longer as the array grows. Insertion sort grows more sharply because its time complexity is O(n²).
2. **Merge sort versus insertion sort.** Merge sort was consistently faster at the tested sizes. Its O(n log n) complexity makes it more suitable for large inputs.
3. **Timsort.** Timsort outperformed both alternatives in these measurements, particularly on larger arrays. Its adaptive behavior and optimizations help with real-world data.
4. **Practical choice.** Timsort was the strongest option in this benchmark. Merge sort is a reasonable alternative when an explicit, relatively simple implementation is required. Insertion sort is simple but unsuitable for large inputs.
