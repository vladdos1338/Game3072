import pygame
import random
from colors_for_squares import squares_colors

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 200
        self.top = 170
        self.cell_size = 80

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                # Значение квадрата
                value = self.board[y][x]
                # Цвет квадрата
                color = squares_colors[value]
                # Отрисовка квадрата
                pygame.draw.rect(screen, (88,73,73), (x * self.cell_size + self.left,
                                                 y * self.cell_size + self.top,
                                                 self.cell_size, self.cell_size), 1)
                pygame.draw.rect(screen, color, (x * self.cell_size + self.left + 3,
                                                                    y * self.cell_size + self.top + 3,
                                                                    self.cell_size - 3, self.cell_size - 3))
                # Отрисовка значения квадрата
                if value:
                    font = pygame.font.Font(None, 72)
                    text_value = font.render(str(value), 1, (255, 255, 255))
                    screen.blit(text_value, (x * self.cell_size + self.left + 25, y * self.cell_size + self.top + 15))

    def move(self, direction):
        if direction == 'right':
            for y in self.board:
                # ненулевые квадраты
                good_value = [value_x for value_x in y if value_x != 0]
                y[:] = [0] * (self.width - len(good_value)) + good_value

                for i in range(self.width - 1, 0, -1):
                    if y[i] == y[i - 1]:
                        y[i] *= 2
                        y[i - 1] = 0

        elif direction == 'left':
            for y in self.board:
                good_value = [value for value in y if value != 0]
                y[:] = good_value + [0] * (self.width - len(good_value))

                for i in range(self.width - 1):
                    if y[i] == y[i + 1]:
                        y[i] *= 2
                        y[i + 1] = 0

        self.generate_square()

    def generate_square(self):
        empty_cells = []
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == 0:
                    empty_cells.append((y, x))
        if empty_cells:
            y, x = random.choice(empty_cells)
            self.board[y][x] = random.choice([3, 6])

