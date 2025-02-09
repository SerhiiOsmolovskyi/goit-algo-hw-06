import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання зважених ребер
edges = [
    ("Центр", "Північний", 7),
    ("Центр", "Східний", 2),
    ("Центр", "Західний", 3),
    ("Північний", "Східний", 5),
    ("Східний", "Передмістя", 8),
    ("Західний", "Південний", 4),
    ("Південний", "Передмістя", 6),
]
G.add_weighted_edges_from(edges)

# Алгоритм Дейкстри для знаходження найкоротшого шляху
shortest_path = nx.shortest_path(G, source="Центр", target="Передмістя", weight="weight")
shortest_distance = nx.shortest_path_length(G, source="Центр", target="Передмістя", weight="weight")

print("Найкоротший шлях за Дейкстрою:", shortest_path)
print("Загальна вага (відстань):", shortest_distance)

# Візуалізація графу та найкоротшого шляху
pos = nx.spring_layout(G)  # Розміщення вершин

plt.figure(figsize=(8, 6))

# Малюємо граф
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')

# Виділяємо найкоротший шлях
shortest_edges = list(zip(shortest_path, shortest_path[1:]))
nx.draw_networkx_edges(G, pos, edgelist=shortest_edges, edge_color='red', width=3)

# Додаємо ваги до ребер
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Відображаємо граф
plt.title("Візуалізація графу з найкоротшим шляхом за Дейкстрою")
plt.show()
