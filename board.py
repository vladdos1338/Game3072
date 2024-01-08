import pygame
import random

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
                color = (93,88,78)
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
            pass

    def get_cell(self, w, h):
        cell_x = w * self.cell_size + self.left
        cell_y = h * self.cell_size + self.top
        return cell_x, cell_y


class Square():
    def __init__(self, wx, hy, value, board):
        self.value = value
        x, y = board.get_cell(wx, hy)
        self.rect = pygame.Rect(x, y, 80, 80)
        self.wx = wx
        self.hy = hy


