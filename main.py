import pygame
import random
from board import Board

pygame.init()
size = height, weight = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('3072 GAME')
clock = pygame.time.Clock()
fps = 60
# текстовая информация
font = pygame.font.Font(None, 72)
title = font.render('3072', 1, (18, 30, 19))


board = Board(5, 5)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                board.move('right')
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                board.move('left')
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                board.move('up')
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                board.move('down')
    screen.fill((220, 220, 220))
    board.render(screen)
    screen.blit(title, (340, 70))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()