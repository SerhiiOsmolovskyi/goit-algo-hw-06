import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(graph, start, target):
    unvisited_nodes = set(graph.nodes)
    distances = {node: float('inf') for node in graph.nodes}
    previous_nodes = {node: None for node in graph.nodes}
    distances[start] = 0
    
    while unvisited_nodes:
        current_node = min(unvisited_nodes, key=lambda node: distances[node])
        unvisited_nodes.remove(current_node)
        
        if current_node == target:
            break
        
        for neighbor in graph.neighbors(current_node):
            if neighbor in unvisited_nodes:
                weight = graph[current_node][neighbor]['weight']
                distance = distances[current_node] + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
    
    path, node = [], target
    while node is not None:
        path.append(node)
        node = previous_nodes[node]
    
    return path[::-1], distances[target]

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

# Використання власноручної реалізації Дейкстри
shortest_path, shortest_distance = dijkstra(G, "Центр", "Передмістя")
print("Найкоротший шлях за Дейкстрою:", shortest_path)
print("Загальна вага (відстань):", shortest_distance)

# Візуалізація графу та найкоротшого шляху
pos = nx.spring_layout(G)
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
