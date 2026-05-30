# Завдання 4. Візуалізація піраміди
# Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
# Суть завдання полягає у створенні дерева із купи.

import uuid
import networkx as nx
import matplotlib.pyplot as plt
import heapq
import queue


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def build_heap(heaped_buff:list):
    if len(heaped_buff) == 0:
        return None
    root = Node(heapq.heappop(heaped_buff))
    q = queue.Queue()
    q.put(root)
    while len(heaped_buff):
        parent = q.get()
        left = Node(heapq.heappop(heaped_buff))
        parent.left = left
        q.put(left)
        if len(heaped_buff) == 0:
            break
        right = Node(heapq.heappop(heaped_buff))
        parent.right = right
        q.put(right)
    return root

def draw_tree(tree_root, title = ''):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 6))
    plt.title(title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


if __name__ == '__main__':
    sample1 = [7, 3, 0, 18, 1, 9, 13, 22]
    heapq.heapify(sample1)
    root1 = build_heap(sample1)
    draw_tree(root1, 'Перший приклад купи')

    sample2 = [3, 21, 10, 15, 1, 19, 3, 2, 33, 6]
    heapq.heapify(sample2)
    root2 = build_heap(sample2)
    draw_tree(root2, 'Другий приклад купи')
