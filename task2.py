# Завдання 2. Рекурсія. Створення фрактала “дерево Піфагора” за допомогою рекурсії

# Необхідно написати програму на Python, яка використовує рекурсію для створення фрактала 
# “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, і користувач 
# повинен мати можливість вказати рівень рекурсії.

import math
import turtle

def draw_pithagoras_layer(t, layer, size, curved = False):
    angles = [55, -35] if curved else [45, -45]
    for angle in angles:
        t.left(angle)
        t.forward(size)
        if layer:
            draw_pithagoras_layer(t, layer - 1, size / math.sqrt(2), curved)
        t.back(size)
        t.right(angle)

def draw_pithagoras_tree(layers, size=100, curved = False):
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(0, -size)
    t.pendown()

    t.left(90)
    t.forward(size)
    draw_pithagoras_layer(t, layers, size, curved)
    window.mainloop()


if __name__ == '__main__':
    layers = int(input('Скільки шарів дерева Піфагора бажаєте? '))
    is_curved = input('Чи бажаєте нахилене дерево y/n: ').lower() == 'y'
    draw_pithagoras_tree(layers, curved=is_curved)
