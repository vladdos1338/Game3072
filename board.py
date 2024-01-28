import pygame
import random
from colors_for_squares import squares_colors

class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        if self.width == 5 and self.height == 5:
            self.left = 200
            self.top = 170
            self.cell_size = 80
        elif self.width == 4 and self.height == 4:
            self.left = 200
            self.top = 170
            self.cell_size = 100
        elif self.width == 6 and self.height == 6:
            self.left = 180
            self.top = 150
            self.cell_size = 73

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
                pygame.draw.rect(screen, color, (x * self.cell_size + self.left + 3,
                                                 y * self.cell_size + self.top + 3,
                                                 self.cell_size - 3, self.cell_size - 3))
                pygame.draw.rect(screen, (88,73,73), (x * self.cell_size + self.left,
                                                 y * self.cell_size + self.top,
                                                 self.cell_size, self.cell_size), 2)
                # Отрисовка значения квадрата
                if value:
                    self.render_value(screen, value, x, y)

    def render_value(self, screen, value, x, y):
        if self.width == 5 and self.height == 5:
            if len(str(value)) == 1:
                font = pygame.font.Font(None, 70)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 26, y * self.cell_size + self.top + 15))
            elif len(str(value)) == 2:
                font = pygame.font.Font(None, 64)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 17, y * self.cell_size + self.top + 18))
            elif len(str(value)) == 3:
                font = pygame.font.Font(None, 58)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 6, y * self.cell_size + self.top + 20))
            elif len(str(value)) == 4:
                font = pygame.font.Font(None, 48)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 3, y * self.cell_size + self.top + 23))
        elif self.width == 4 and self.height == 4:
            if len(str(value)) == 1:
                font = pygame.font.Font(None, 100)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 30, y * self.cell_size + self.top + 15))
            elif len(str(value)) == 2:
                font = pygame.font.Font(None, 86)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 16, y * self.cell_size + self.top + 19))
            elif len(str(value)) == 3:
                font = pygame.font.Font(None, 72)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 5, y * self.cell_size + self.top + 25))
            elif len(str(value)) == 4:
                font = pygame.font.Font(None, 54)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 5, y * self.cell_size + self.top + 30))
        elif self.width == 6 and self.height == 6:
            if len(str(value)) == 1:
                font = pygame.font.Font(None, 70)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 23, y * self.cell_size + self.top + 13))
            elif len(str(value)) == 2:
                font = pygame.font.Font(None, 64)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 12, y * self.cell_size + self.top + 16))
            elif len(str(value)) == 3:
                font = pygame.font.Font(None, 58)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 19))
            elif len(str(value)) == 4:
                font = pygame.font.Font(None, 42)
                text_value = font.render(str(value), 1, (255, 255, 255))
                screen.blit(text_value,
                            (x * self.cell_size + self.left + 2, y * self.cell_size + self.top + 22))

    def move(self, direction):
        if direction == 'left':
            for row in self.board:
                while 0 in row:
                    row.remove(0)
                while len(row) != self.width:
                    row.append(0)
            for y in range(self.height):
                for x in range(self.width - 1):
                    if self.board[y][x] == self.board[y][x+1] and self.board[y][x] != 0:
                        self.board[y][x] *= 2
                        self.board[y].pop(x+1)
                        self.board[y].append(0)

        elif direction == 'right':
            for row in self.board:
                while 0 in row:
                    row.remove(0)
                while len(row) != self.width:
                    row.insert(0, 0)
            for y in range(self.height):
                for x in range(self.width - 1, 0, -1):
                    if self.board[y][x] == self.board[y][x-1] and self.board[y][x] != 0:
                        self.board[y][x] *= 2
                        self.board[y].pop(x-1)
                        self.board[y].insert(0, 0)

        if direction == 'up':
            for x in range(self.width):
                column = [self.board[y][x] for y in range(self.height)]
                while 0 in column:
                    column.remove(0)
                while len(column) != self.height:
                    column.append(0)
                for y in range(self.height - 1):
                    if column[y] == column[y + 1] and column[y] != 0:
                        column[y] *= 2
                        column.pop(y + 1)
                        column.append(0)
                for y in range(self.height):
                    self.board[y][x] = column[y]

        elif direction == 'down':
            for x in range(self.width):
                column = [self.board[y][x] for y in range(self.height)]
                while 0 in column:
                    column.remove(0)
                while len(column) != self.height:
                    column.insert(0, 0)
                for y in range(self.height - 1, 0, -1):
                    if column[y] == column[y - 1] and column[y] != 0:
                        column[y] *= 2
                        column.pop(y - 1)
                        column.insert(0, 0)
                for y in range(self.height):
                    self.board[y][x] = column[y]

        self.generate_square()

    def check_win(self):
        for row in self.board:
            if 3072 in row:
                return True

    def generate_square(self):
        empty_cells = []
        for x in range(self.width):
            for y in range(self.height):
                if self.board[y][x] == 0:
                    empty_cells.append((y, x))
        if empty_cells:
            y, x = random.choice(empty_cells)
            self.board[y][x] = random.choice([3, 6, 1536])

