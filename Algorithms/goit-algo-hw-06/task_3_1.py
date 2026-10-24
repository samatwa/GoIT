import networkx as nx
import matplotlib.pyplot as plt


# Створення графа для міста
G = nx.Graph()

# Додавання зупинок та маршрутів автобусів з вагами
bus_stops = ["A", "B", "C", "D", "E", "F", "G"]
bus_routes = [("A", "B", 5), ("B", "C", 7), ("C", "D", 3), ("D", "E", 6), ("E", "F", 4), ("F", "G", 5),
              ("A", "D", 9), ("B", "E", 8), ("C", "F", 5), ("D", "G", 7)]
G.add_nodes_from(bus_stops)
G.add_weighted_edges_from(bus_routes)

# Візуалізація графа
options = {
    "node_color": "lightgreen",
    "node_size": 1000,
    "font_size": 12,
    "font_weight": "bold",
    "width": 2,
    "with_labels": True
}

plt.title("Weighted Bus Routes Network")
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, **options)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Застосування алгоритму Дейкстри
shortest_paths = nx.single_source_dijkstra_path(G, source='A')
shortest_path_lengths = nx.single_source_dijkstra_path_length(G, source='A')

print(shortest_paths)  # виведе найкоротші шляхи від вузла 'A' до всіх інших вузлів
print(shortest_path_lengths)  # виведе довжини найкоротших шляхів від вузла 'A' до всіх інших вузлів