# Завдання 6. Жадібні алгоритми та динамічне програмування
# 
# Необхідно написати програму на Python, яка використовує два підходи — жадібний алгоритм та алгоритм 
# динамічного програмування для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
# 
# Кожен вид їжі має вказану вартість і калорійність. Дані про їжу представлені у вигляді словника, де ключ — назва страви, 
# а значення — це словник з вартістю та калорійністю.

def greedy_algorithm(menu, budget):
    # Make a calories ratio list and sort it
    best_calories = [(menu[name]['calories'] / menu[name]['cost'], name) for name in menu.keys()]
    best_calories.sort(reverse=True)
    spend = 0
    calories = 0
    cart_list = []
    for food in best_calories:
        cost = menu[food[1]]['cost']
        if cost <= budget:
            budget -= cost
            spend += cost
            calories += menu[food[1]]['calories']
            cart_list.append(food[1])
    return (cart_list, spend, calories)


def dynamic_programming(menu, budget):
    # Створюємо таблицю для зберігання оптимальних значень підзадач
    N = len(menu)
    R = [[0] * (budget + 1) for _ in range(N + 1)]
    menu_list = [(menu[m]['cost'], menu[m]['calories'], m) for m in menu]

    for i in range(1, N + 1):
        cost, calories, _ = menu_list[i-1]
        for c in range(budget + 1):
            if cost <= c: 
                R[i][c] = max( calories + R[i-1][c - cost], R[i-1][c] )
            else:
                R[i][c] = R[i-1][c]
    # Відновимо набір страв з оптимальних значень
    cart_list = []
    c = budget
    for i in range(N, 0, -1):
        cost, _, name = menu_list[i - 1]
        # і-ий продукт був куплений
        if R[i][c] != R[i - 1][c]:
            cart_list.append(name)
            c -= cost
    cart_list.reverse()
    spend = sum(menu[name]["cost"] for name in cart_list)
    total_calories = R[N][budget]
    return cart_list, spend, total_calories


if __name__ == '__main__':
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350}
    }

    for bud in [65, 45, 30, 70]:
        print(f"Бюджет {bud} грн.")
        l, spend, calories = greedy_algorithm(items, bud)
        print(f"У жадібного алгроритма: куплено: {l} витрачено: {spend} грн. на: {calories} ккал.")
        l, spend, calories = dynamic_programming(items, bud)
        print(f"У алгроритма динам. прогр.: куплено: {l} витрачено: {spend} грн. на: {calories} ккал.")

