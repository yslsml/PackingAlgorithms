import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import random
from Item import Item


class FloorCeilingAlgorithm:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def pack_items(self):
        self.items.sort(key=lambda item: item.width * item.height, reverse=True)
        floor = np.zeros((self.height, self.width), dtype=bool)
        ceiling = np.zeros((self.height, self.width), dtype=bool)

        for item in self.items:
            for y in range(self.height - item.height + 1):
                for x in range(self.width - item.width + 1):
                    if not floor[y:y+item.height, x:x+item.width].any():
                        floor[y:y+item.height, x:x+item.width] = True
                        item.x = x
                        item.y = y
                        break
                if item.x is not None:
                    break

            if item.x is None:
                for y in range(self.height - item.height + 1):
                    for x in range(self.width - item.width + 1):
                        if not ceiling[y:y+item.height, x:x+item.width].any():
                            ceiling[y:y+item.height, x:x+item.width] = True
                            item.x = x
                            item.y = y
                            break
                    if item.x is not None:
                        break

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


algorithm = FloorCeilingAlgorithm(10, 10)
algorithm.add_item(Item(1, 3, 5))
algorithm.add_item(Item(2, 4, 2))
algorithm.add_item(Item(3, 2, 4))
algorithm.add_item(Item(4, 3, 3))
algorithm.add_item(Item(5, 1, 6))

packed_items = algorithm.pack_items()
print_coordinates(packed_items)
visualize_packing(packed_items, algorithm.width, algorithm.height)
