import numpy as np
import random


def generate_items(count, min_weight=1, max_weight=10, min_price=1, max_price=10):
    items = []
    for _ in range(count):
        weight = random.randint(min_weight, max_weight)
        value = random.randint(min_price, max_price)
        items.append((weight, value))
    print(f"Generated items (weight, price): {items}")
    return items


def backpack_algorithm(items, capacity):
    n = len(items)
    costs_array = np.zeros((n + 1, capacity + 1))

    for i in range(1, n + 1):
        weight, price = items[i - 1]
        for current_capacity in range(1, capacity + 1):
            if weight > current_capacity:
                costs_array[i][current_capacity] = costs_array[i - 1][current_capacity]
            else:
                costs_array[i][current_capacity] = max(costs_array[i - 1][current_capacity], costs_array[i - 1][current_capacity - weight] + price)

    chosen_items = []
    current_capacity = capacity
    for i in range(n, 0, -1):
        if costs_array[i][current_capacity] != costs_array[i - 1][current_capacity]:
            weight, price = items[i - 1]
            chosen_items.append((i, weight, price))
            current_capacity -= weight

    max_cost = costs_array[n][capacity]
    return max_cost, chosen_items


def print_results(max_cost, chosen_items):
    print("Max cost:", max_cost)
    print("Chosen items:")
    for item in chosen_items:
        print("  Item", item[0], "- Weight:", item[1], " Price:", item[2])
    print()


items = [(3, 1), (4, 6), (5, 4), (8, 7), (9, 6)]
print("Items (weight, price):", items)
capacity = 13
print("Capacity:", capacity)
max_cost, chosen_items = backpack_algorithm(items, capacity)
print_results(max_cost, chosen_items)

items2 = generate_items(5)
capacity2 = 15
print("Capacity:", capacity2)
max_cost2, chosen_items2 = backpack_algorithm(items2, capacity2)
print_results(max_cost2, chosen_items2)