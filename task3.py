# Завдання 3. Дерева, алгоритм Дейкстри
# Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, використовуючи бінарну купу. 
# Завдання включає створення графа, використання піраміди для оптимізації вибору вершин та обчислення 
# найкоротших шляхів від початкової вершини до всіх інших.

import networkx as nx
import matplotlib.pyplot as plt
import heapq

def print_table(distances):
    # Верхній рядок таблиці
    print("{:<10} {:<10}".format("Вершина", "Відстань"))
    print("-" * 30)
    
    # Вивід даних для кожної вершини
    for vertex in distances:
        distance = distances[vertex]
        if distance == float('infinity'):
            distance = "∞"
        else:
            distance = str(distance)
        print("{:<10} {:<10}".format(vertex, distance))
    print("\n")

def dijkstra(graph, start):
    # Make dict with heapq as values
    gr = {key: [(v, k) for k, v in val.items()] for key, val in graph.items()}
    for val in gr.values(): 
        heapq.heapify(val)

    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())
    visited = []

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        while len(gr[current_vertex]):
            weight, neighbor = heapq.heappop(gr[current_vertex]) 
            distance = distances[current_vertex] + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        visited.append(current_vertex)
        unvisited.remove(current_vertex)
    return distances

if __name__ == '__main__':
    # Створення графа
    G = nx.Graph()
    # Приклад графа у вигляді словника
    graph = {
        'A': {'B': 5, 'C': 11},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 11, 'D': 2},
        'D': {'B': 3, 'C': 2, 'E': 4},
        'E': {'D': 4}
    }

    # Додавання вершин і ребер
    for top1, top2 in graph.items():
        for key, val in top2.items():
            G.add_edge(top1, key, weight=val)

    # Візуалізація графа
    pos = nx.spring_layout(G, seed=42)
    nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

    plt.show()

    # Виклик функції для вершини A
    distances = dijkstra(graph, 'A')
    print_table(distances)
