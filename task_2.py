import networkx as nx
from collections import deque
import matplotlib.pyplot as plt


# Завантажуємо граф із Завдання 1
G = nx.Graph()
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

# Алгоритм DFS (пошук у глибину)
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path.append(start)
    if start == goal:
        return path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path.copy())
            if new_path:
                return new_path
    return None

# Алгоритм BFS (пошук у ширину)
def bfs(graph, start, goal):
    queue = deque([[start]])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        for neighbor in graph.neighbors(node):
            if neighbor not in path:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Пошук маршруту з "Центр" до "Передмістя"
dfs_path = dfs(G, "Центр", "Передмістя")
bfs_path = bfs(G, "Центр", "Передмістя")

print("Шлях DFS:", dfs_path)
print("Шлях BFS:", bfs_path)

# Візуалізація графу та шляхів
pos = nx.spring_layout(G)  # розміщення вершин
plt.figure(figsize=(8, 6))

# Малюємо граф
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='lightblue', font_size=12, font_weight='bold')

# Виділяємо шлях DFS
if dfs_path:
    dfs_edges = list(zip(dfs_path, dfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='red', width=3)

# Виділяємо шлях BFS
if bfs_path:
    bfs_edges = list(zip(bfs_path, bfs_path[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=bfs_edges, edge_color='green', width=3)

# Відображаємо граф
plt.title("Візуалізація графу з шляхами DFS та BFS")
plt.show()
