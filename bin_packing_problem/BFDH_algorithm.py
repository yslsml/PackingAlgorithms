import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from Item import Item
from Container import Container


class BestFitDecreasingHeightAlgorithm:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def pack_items(self):
        self.items.sort(key=lambda item: item.height, reverse=True)
        containers = []

        for item in self.items:
            best_container = None
            best_remaining_area = float('inf')

            for container in containers:
                if container.can_fit(item.width, item.height):
                    remaining_area = container.remaining_area(item.width, item.height)
                    if remaining_area < best_remaining_area:
                        best_container = container
                        best_remaining_area = remaining_area

            if best_container is None:
                best_container = Container(self.width, self.height)
                containers.append(best_container)

            best_container.place(item.width, item.height)
            item.x = best_container.x
            item.y = best_container.y

        return self.items


def visualize_packing(items, width, height):
    fig, ax = plt.subplots()
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim([0, width])
    ax.set_ylim([0, height])
    ax.set_xticks(range(width + 1))
    ax.set_yticks(range(height + 1))
    ax.grid(True)

    colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'cyan', 'magenta']
    random.shuffle(colors)

    for item, color in zip(items, colors):
        rect = Rectangle((item.x, item.y), item.width, item.height, facecolor=color, edgecolor='black')
        ax.add_patch(rect)

        ax.annotate(str(item.id), (item.x + item.width / 2, item.y + item.height / 2),
                    color='black', weight='bold', fontsize=8, ha='center', va='center')
    plt.show()


def print_coordinates(items):
    for item in items:
        print(f"Item {item.id} - x: {item.x}, y: {item.y}")


algorithm = BestFitDecreasingHeightAlgorithm(10, 10)
algorithm.add_item(Item(1, 3, 5))
algorithm.add_item(Item(2, 4, 2))
algorithm.add_item(Item(3, 2, 4))
algorithm.add_item(Item(4, 3, 3))
algorithm.add_item(Item(5, 1, 6))

packed_items = algorithm.pack_items()
print_coordinates(packed_items)
visualize_packing(packed_items, algorithm.width, algorithm.height)
