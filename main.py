import pygame
import sys
import os
import sqlite3
from board import Board

pygame.init()
size = height, weight = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('3072 GAME')
clock = pygame.time.Clock()
fps = 60
# Подключение бд
con_scores = sqlite3.connect(os.path.join('data\db', 'scores_db.sqlite'))
cur = con_scores.cursor()
con_save = sqlite3.connect(os.path.join('data\db', 'save_game_db.sqlite'))
cur2 = con_save.cursor()
# текстовая информация
font = pygame.font.Font(None, 72)
title = font.render('3072', 1, (18, 30, 19))
font1 = pygame.font.Font(None, 50)
is_continue = 0


def terminate():
    con_save.close()
    con_scores.close()
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
        elif 690 > pos[0] > 630 and 80 > pos[1] > 20:
            return 'restart'
        return False


def db_save_delete(flag):
    if flag == 'lose':
        if board.get_size() == (4, 4):
            cur.execute("INSERT INTO scores_4x4 (score) VALUES (?)", (board.get_current_score(),))
            cur2.execute("DELETE FROM saves_4x4")
        elif board.get_size() == (5, 5):
            cur.execute("INSERT INTO scores_5x5 (score) VALUES (?)", (board.get_current_score(),))
            cur2.execute("DELETE FROM saves_5x5")
        elif board.get_size() == (6, 6):
            cur.execute("INSERT INTO scores_6x6 (score) VALUES (?)", (board.get_current_score(),))
            cur2.execute("DELETE FROM saves_6x6")
    elif flag == 'restart':
        if board.get_size() == (4, 4):
            cur2.execute("DELETE FROM saves_4x4")
        elif board.get_size() == (5, 5):
            cur2.execute("DELETE FROM saves_5x5")
        elif board.get_size() == (6, 6):
            cur2.execute("DELETE FROM saves_6x6")
    elif flag == 'menu':
        if board.get_size() == (4, 4):
            cur2.execute("DELETE FROM saves_4x4")
            cur2.execute("INSERT INTO saves_4x4 (positions) VALUES (?)", (str(board.get_board()),))
        elif board.get_size() == (5, 5):
            cur2.execute("DELETE FROM saves_5x5")
            cur2.execute("INSERT INTO saves_5x5 (positions) VALUES (?)", (str(board.get_board()),))
        elif board.get_size() == (6, 6):
            cur2.execute("DELETE FROM saves_6x6")
            cur2.execute("INSERT INTO saves_6x6 (positions) VALUES (?)", (str(board.get_board()),))


def lose_screen():
    global is_continue
    # сохранение счета в бд
    db_save_delete('lose')
    con_scores.commit()
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
    global best_score, best_score_text
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
                    if board.get_size() == (4, 4):
                        best_score = cur.execute("SELECT MAX(score) FROM scores_4x4").fetchall()[0][0]
                        if cur2.execute("SELECT COUNT(*) FROM saves_4x4 WHERE positions IS NOT NULL;").fetchall()[0][0]:
                            loaded_board = cur2.execute("SELECT * FROM saves_4x4 "
                                                        "ORDER BY positions DESC LIMIT 1").fetchall()[0][0]
                            board.load_board(loaded_board)
                    elif board.get_size() == (5, 5):
                        best_score = cur.execute("SELECT MAX(score) FROM scores_5x5").fetchall()[0][0]
                        if cur2.execute("SELECT COUNT(*) FROM saves_5x5 WHERE positions IS NOT NULL;").fetchall()[0][0]:
                            loaded_board = cur2.execute("SELECT * FROM saves_5x5 "
                                                        "ORDER BY positions DESC LIMIT 1").fetchall()[0][0]
                            board.load_board(loaded_board)
                    elif board.get_size() == (6, 6):
                        best_score = cur.execute("SELECT MAX(score) FROM scores_6x6").fetchall()[0][0]
                        if cur2.execute("SELECT COUNT(*) FROM saves_6x6 WHERE positions IS NOT NULL;").fetchall()[0][0]:
                            loaded_board = cur2.execute("SELECT * FROM saves_6x6 "
                                                        "ORDER BY positions DESC LIMIT 1").fetchall()[0][0]
                            board.load_board(loaded_board)
                    best_score_text = font1.render(f"Рекорд: {best_score}", 1, (0, 0, 0))
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
btn_restart = pygame.transform.scale(load_image("restart.png"), (60, 60))
# Запуск начального экрана
start_screen()
# Флаг победы
w = 0
# Игровой цикл
running = True
while running:
    current_score_text = font1.render(f"Очки: {board.get_current_score()}", 1, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            cur2.execute("DELETE FROM saves_4x4")
            cur2.execute("INSERT INTO saves_4x4 (positions) VALUES (?)", (str(board.get_board()),))
            con_save.commit()
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
            # Если на поле есть квадрат 3072 и пользователь до этого не нажимал 'продолжить', то флаг победы равен 1
            if board.check_win() and is_continue == 0:
                w = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            if check_coords('game', event.pos) == 'menu':
                db_save_delete('menu')
                con_scores.commit()
                con_save.commit()
                start_screen()
            if check_coords('game', event.pos) == 'restart':
                db_save_delete('restart')
                size = board.get_size()
                board = Board(*size)
    screen.fill((220, 220, 220))
    board.render(screen)
    # Отрисовка заголовка игры
    screen.blit(title, (340, 70))
    # Отрисовка кнопки меню
    screen.blit(btn_menu, (710, 20))
    # Отрисовка кнопки старта
    screen.blit(btn_restart, (630, 20))
    # Отрисовка текущего счета
    screen.blit(current_score_text, (15, 15))
    # Отрисовка лучшего счета
    screen.blit(best_score_text, (15, 50))
    # Проверка победы и проигрыша
    if w:
        w = 0
        win_screen()
    if board.is_lose():
        lose_screen()
    pygame.display.flip()
    clock.tick(fps)

con_scores.close()
con_save.close()
pygame.quit()
