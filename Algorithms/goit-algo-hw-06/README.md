# goit-algo-hw-06

## Task 3: DFS and BFS traversal

Both depth-first search (DFS) and breadth-first search (BFS) visited every vertex, in different orders:

- DFS: ['A', 'B', 'C', 'D', 'E', 'F', 'G']
- BFS: ['A', 'B', 'D', 'C', 'E', 'G', 'F']

The iterative BFS implementation uses `set(graph[vertex]) - visited`. Python sets do not guarantee traversal order, so vertices within a level can appear in a different order.

DFS explores a branch deeply before backtracking and does not generally find the shortest path. BFS explores consecutive distance levels and finds a shortest path in an unweighted graph.
