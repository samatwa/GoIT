# goit-algo-hw-09

## Greedy versus dynamic-programming coin change

The `timeit` benchmark compares both algorithms for amount 113 with `number=100000` repetitions.

| Algorithm | Recorded time, seconds |
|---|---:|
| Greedy | 0.083812 |
| Dynamic programming | 6.854841 |

Results depend on the machine and benchmark conditions.

The greedy implementation makes one pass over the denominations, giving O(n) work in this implementation, where n is the number of denominations. It is effective for large amounts when the denomination system supports optimal greedy choices.

Dynamic programming has O(amount × n) time complexity and finds the minimum number of coins for the tested positive integer denomination systems, including cases where greedy choices fail. It can be slower for large amounts.

A greedy algorithm is not optimal for every denomination set. For example, [9, 6, 5, 1] can require a different choice from repeatedly taking the largest coin. Choose greedy for speed when its optimality is established for the denomination system; use dynamic programming when a general minimum-coin guarantee is required.
