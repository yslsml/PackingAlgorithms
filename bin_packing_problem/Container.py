import numpy as np


class Container:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=bool)
        self.x = None
        self.y = None

    def can_fit(self, item_width, item_height):
        return self.width >= item_width and self.height >= item_height

    def remaining_area(self, item_width, item_height):
        occupied_area = np.sum(self.grid)
        item_area = item_width * item_height
        return self.width * self.height - occupied_area - item_area

    def place(self, item_width, item_height):
        for y in range(self.height - item_height + 1):
            for x in range(self.width - item_width + 1):
                if not self.grid[y:y+item_height, x:x+item_width].any():
                    self.grid[y:y+item_height, x:x+item_width] = True
                    self.x = x
                    self.y = y
                    return