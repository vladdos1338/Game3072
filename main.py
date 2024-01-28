import pygame
import sys
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

def terminate():
    pygame.quit()
    sys.exit()

def check_coords(pos):
    global board
    if 271 > pos[0] > 121 and 382 > pos[1] > 232:
        board = Board(4, 4)
        return True
    elif 471 > pos[0] > 321 and 382 > pos[1] > 232:
        board = Board(5, 5)
        return True
    elif 671 > pos[0] > 521 and 382 > pos[1] > 232:
        board = Board(6, 6)
        return True
    return False

def start_screen():
    font = pygame.font.Font(None, 80)
    choosing = True
    board_4 = font.render('4x4', 1, (0, 0, 0))
    board_5 = font.render('5x5', 1, (0, 0, 0))
    board_6 = font.render('6x6', 1, (0, 0, 0))
    font = pygame.font.Font(None, 72)
    text_tip = font.render('Выбери размер поля', 1, (0, 0, 0))
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_coords(event.pos):
                    return
        screen.fill((220, 220, 220))
        screen.blit(text_tip, (140, 85))
        for i in range(3):
            pygame.draw.rect(screen, (223, 227, 216), (121 + i * 200, 232, 150, 150))
            pygame.draw.rect(screen, (88, 73, 73), (121 + i*200, 232, 150, 150), 5)
        screen.blit(board_4, (150, 280))
        screen.blit(board_5, (350, 280))
        screen.blit(board_6, (550, 280))
        pygame.display.flip()
        clock.tick(60)

start_screen()
board.generate_square()
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