import pygame
import sys
import os
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
is_continue = 0

def terminate():
    pygame.quit()
    sys.exit()

def win_screen():
    global is_continue
    font = pygame.font.Font(None, 80)
    text_congratulations = font.render('Вы победили!', 1, (255, 0, 0))
    btn_restart = pygame.transform.scale(load_image("restart.png"), (120, 120))
    btn_continue = pygame.transform.scale(load_image("continue.png"), (120, 120))
    choosing = True
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_coords('win', event.pos) == 'restart':
                    start_screen()
                    return
                elif check_coords('win', event.pos) == 'continue':
                    is_continue = 1
                    return
        screen.blit(text_congratulations, (200, 110))
        screen.blit(btn_restart, (230, 300))
        screen.blit(btn_continue, (430, 300))
        pygame.display.flip()
        clock.tick(60)

def load_image(name, colorkey=None):
    fullname = os.path.join('data\images', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def check_coords(who, pos):
    global board
    if who == 'start':
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
    elif who == 'win':
        if 350 > pos[0] > 230 and 420 > pos[1] > 300:
            return 'restart'
        elif 550 > pos[0] > 430 and 420 > pos[1] > 300:
            return 'continue'
        return False
    elif who == 'lose':
        if 600 > pos[0] > 300 and 600 > pos[1] > 300:
            return 'restart'
        return False
    elif who == 'game':
        if 770 > pos[0] > 710 and 80 > pos[1] > 20:
            return 'menu'
        return False

def lose_screen():
    global is_continue
    font = pygame.font.Font(None, 80)
    text_lose = font.render('Вы проиграли!', 1, (255, 0, 0))
    btn_restart = pygame.transform.scale(load_image("restart.png"), (200, 200))
    choosing = True
    while choosing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_coords('lose', event.pos) == 'restart':
                    is_continue = 0
                    start_screen()
                    return
        screen.blit(text_lose, (200, 105))
        screen.blit(btn_restart, (300, 300))
        pygame.display.flip()
        clock.tick(60)

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
                if check_coords('start', event.pos):
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

# Кнопка меню
btn_menu = pygame.transform.scale(load_image("menu.png"), (60, 60))
# Запуск начального экрана
start_screen()
font1 = pygame.font.Font(None, 50)
# Флаг победы
w = 0
# Игровой цикл
running = True
while running:
    current_score_text = font1.render(f"Очки: {board.get_current_score()}", 1, (0, 0, 0))
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
            if board.check_win() and is_continue == 0:
                w = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_coords('game', event.pos) == 'menu':
                start_screen()
    screen.fill((220, 220, 220))
    board.render(screen)
    screen.blit(title, (340, 70))
    screen.blit(btn_menu, (710, 20))
    screen.blit(current_score_text, (15, 15))
    if w:
        w = 0
        win_screen()
    if board.is_lose():
        lose_screen()
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()