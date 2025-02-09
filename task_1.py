import networkx as nx
import matplotlib.pyplot as plt

# Створення графа міської транспортної мережі
G = nx.Graph()

# Додавання вузлів (районів міста)
nodes = ["Центр", "Північний", "Східний", "Західний", "Південний", "Передмістя"]
G.add_nodes_from(nodes)

# Додавання доріг між районами (ребер)
edges = [
    ("Центр", "Північний"),
    ("Центр", "Східний"),
    ("Центр", "Західний"),
    ("Північний", "Східний"),
    ("Східний", "Передмістя"),
    ("Західний", "Південний"),
    ("Південний", "Передмістя"),
]
G.add_edges_from(edges)

# Візуалізація графа
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=12)
plt.title("Транспортна мережа міста")
plt.show()

# Аналіз характеристик графа
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())

# Виведення ступенів вершин
degrees = dict(G.degree())
print("Ступінь вершин:", degrees)
