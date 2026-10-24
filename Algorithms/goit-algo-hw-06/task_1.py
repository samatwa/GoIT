import networkx as nx
import matplotlib.pyplot as plt

# Створення графа для міста
G = nx.Graph()

# Додавання зупинок та маршрутів автобусів
bus_stops = ["A", "B", "C", "D", "E", "F", "G"]
bus_routes = [
    ("A", "B" ), ("B", "C"), ("C", "D"), ("D", "E"), ("E", "F"), 
    ("F", "G"),("A", "D"), ("B", "E"), ("C", "F"), ("D", "G")
]

G.add_nodes_from(bus_stops)
G.add_edges_from(bus_routes)

# Візуалізація графа
options = {
    "node_color": "lightgreen",
    "node_size": 1000,
    "font_size": 12,
    "font_weight": "bold",
    "width": 2,
    "with_labels": True,
}

plt.title("Bus Routes Network")
nx.draw(G, **options)
plt.show()

# Аналіз основних характеристик графа
print("Number of vertices:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
print("Degree of vertices:")
for node in G.nodes():
    print(node, ":", G.degree(node))

# Перевірка на зв'язність графа
is_connected = nx.is_connected(G)
if is_connected:
    print("The graph is connected.")
else:
    print("The graph is not connected.")
print()