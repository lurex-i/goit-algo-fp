# Завдання 5. Візуалізація обходу бінарного дерева
# Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, 
# яка візуалізує обходи дерева: у глибину та в ширину.
# 
# Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB (приклад #1296F0). 
# Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
# Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.

from task4 import Node, draw_tree, build_heap
import heapq
from collections import deque
import matplotlib.colors as mcolors
import colorsys

def shift_hue(rgb, shift=0.04):
    # переводимо у HSV
    h, s, v = colorsys.rgb_to_hsv(*rgb)
    # зсув тону і кольору
    h_new = (h + shift) % 1.0
    v_new = (v + shift) % 1.0
    # назад у RGB
    rgb_new = colorsys.hsv_to_rgb(h_new, s, v_new)
    return rgb_new


def dfs_walk(root:Node):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [root]
    # Встановимо стартовий колір для кореня
    rgb = mcolors.to_rgb('darkblue')
    root.color = rgb
    while stack:
        # Вилучаємо вершину зі стеку
        curr = stack.pop()  
        if curr not in visited:
            # Трохи відображення послідовності обходу в терміналі
            print(curr.val, end=' -> ')
            # Зсув кольора при обході
            rgb = shift_hue(rgb)
            curr.color = rgb 
            visited.add(curr)
            # Додаємо дітей якщо вони є, в стек, таким чином, щоб лівий був першим для наступного проходу
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
    print()

def bfs_walk(root:Node):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([root])
    # Встановимо стартовий колір для кореня
    rgb = mcolors.to_rgb('darkblue')

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        curr = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if curr not in visited:
            # Трохи відображення послідовності обходу в терміналі
            print(curr.val, end=" -> ")
            # Зсув кольора при обході
            rgb = shift_hue(rgb)
            curr.color = rgb 
            # Додаємо вершину до множини відвіданих вершин
            visited.add(curr)
            # Додаємо дітей якщо вони є, в чергу, таким чином, щоб лівий був першим для наступного проходу
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
    print()
    return visited  

if __name__ == '__main__':
    sample1 = [7, 3, 0, 18, 1, 9, 13, 22]
    heapq.heapify(sample1)
    root1 = build_heap(sample1)

    dfs_walk(root1)
    draw_tree(root1, 'Купа з обходом в глибуну')

    bfs_walk(root1)
    draw_tree(root1, 'Купа з обходом в ширину')