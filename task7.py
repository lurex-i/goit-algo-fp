# Завдання 7. Використання методу Монте-Карло
# 
# Необхідно написати програму на Python, яка імітує велику кількість кидків кубиків, обчислює суми чисел, 
# які випадають на кубиках, і визначає ймовірність кожної можливої суми.
# 
# Створіть симуляцію, де два кубики кидаються велику кількість разів. Для кожного кидка визначте суму чисел, 
# які випали на обох кубиках. Підрахуйте, скільки разів кожна можлива сума (від 2 до 12) з’являється у процесі 
# симуляції. Використовуючи ці дані, обчисліть імовірність кожної суми.
# 
# На основі проведених імітацій створіть таблицю або графік, який відображає ймовірності кожної суми, виявлені 
# за допомогою методу Монте-Карло.

import random
from collections import defaultdict

def simulate_two_cubes(num_experiments)->dict:
    results = defaultdict(int)
    for _ in range(num_experiments):
        summ = random.randint(1, 6) + random.randint(1, 6)
        results[summ] += 1
    for key in results:
        results[key] = results[key] / num_experiments
    return dict(results)

if __name__ == '__main__':
    numbers = [1000, 10000, 100000, 1000000]
    results = [simulate_two_cubes(qnt) for qnt in numbers]
    # Вирахуємо теоритичні вірогідності
    ideal_prob = { x: (x - 1) / 36 for x in range(2, 8)}
    ideal_prob.update({ x: (13 - x) / 36 for x in range(8, 13)})

    # Заголовок таблиці
    print(f"|  Sum  |   Ideal   |", end='')
    for n in numbers:
        print(f" {n:9} |", end='')
    print('\n' + '-'*(len(numbers)*12 + 12 + 9) )
    # Дані фактичної вірогідності та отримані методом Монте-Карло
    for summ in range(2, 13):
        print(f"| {summ:5} | {ideal_prob[summ]:9.2%} |", end='')
        for ind, _ in enumerate(numbers):
            print(f" {results[ind][summ]:9.2%} |", end='')
        print()
