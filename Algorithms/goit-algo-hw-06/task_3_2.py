graph = {
    'A': {'B':5, 'D':9},
    'B': {'A':5, 'C':7, 'E':8},
    'C': {'B':7, 'D':3, 'F':5},
    'D': {'A':9, 'C':3, 'E':6, 'G':7},
    'E': {'B':8, 'D':6, 'F':4},
    'F': {'C':5, 'E':4, 'G':5},
    'G': {'D':7, 'F':5},
}

def print_table(distances, visited):
    # Верхній рядок таблиці
    print("{:<10} {:<10} {:<10}".format("Vertex", "Distance", "Visited"))
    print("-" * 30)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "Inf"
        else:
            distance = str(distance)
        
        status = "Yes" if vertex in visited else "No"
        print("{:<10} {:<10} {:<10}".format(vertex, distance, status))
    print()

def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
        
        # Вивід таблиці після кожного кроку
        print_table(distances, visited)

    return distances

# Виклик функції для вершини A
print(dijkstra(graph, 'A'))
