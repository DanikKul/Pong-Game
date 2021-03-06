import pygame
import math
import random

from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1020, 720))
pygame.display.set_caption("DOS PONG")
screen.fill((0, 0, 0))

coord_1 = [150, 310]
coord_2 = [855, 310]
coord_3 = [510, 360]
angle_ball = 0
speed = 20
dx = 5
score = [0, 0]
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
PINK = (255, 0, 255)
ORANGE = (250, 130, 0)
PURPLE = (130, 0, 250)
CYAN = (3, 252, 248)
GRAY = (145, 145, 145)
colors = [RED, GREEN, BLUE, YELLOW, PINK, ORANGE, PURPLE, CYAN, GRAY]
ball_color = RED
left_racket_color = WHITE
right_racket_color = WHITE
background_color = BLACK
borders_color = WHITE
lines_color = WHITE
text_color = WHITE
theme = "DARK"
bot_1_tim = 0
bot_2_tim = 0
final_point = 3
final_speed = 20
motion_1 = "STOP"
motion_2 = "STOP"

gameOn = True
app_bool = True
prologOn1 = False
prologOn2 = False
player = False
bot = False
bot_2 = False
choosePlayer = True
setting = False
winner = False
bools_list = [gameOn, app_bool, prologOn1, prologOn2, player, bot, bot_2, choosePlayer, setting]
pygame.font.init()


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((20, 100))
        self.surf.fill(WHITE)
        self.rect = self.surf.get_rect()


square1 = Square()
square2 = Square()


def goal():
    global motion_1, motion_2, score, coord_1, coord_2, coord_3
    motion_1 = "STOP"
    motion_2 = "STOP"
    stopGame = True
    while stopGame:
        for event1 in pygame.event.get():
            if event1.type == KEYDOWN:
                if event1.key == K_SPACE:
                    stopGame = False
                if event1.key == K_r:
                    stopGame = False
                    score = [0, 0]
            elif event1.type == QUIT:
                exit(0)
    coord_1 = [150, 310]
    coord_2 = [855, 310]
    coord_3 = [510, 360]
    if bot_2:
        coord_2[1] += random.randint(-40, 40)
        coord_1[1] += random.randint(-40, 40)


def pause_game():
    pause = True
    global motion_1, motion_2, score, coord_1, coord_2, coord_3, \
        angle_ball, gameOn, app_bool, prologOn1, \
        prologOn2, player, bot, bot_2, choosePlayer, \
        setting, winner
    motion_1 = "STOP"
    motion_2 = "STOP"
    while pause:
        for event1 in pygame.event.get():
            if event1.type == KEYDOWN:
                if event1.key == K_SPACE:
                    pause = False
                if event1.key == K_r:
                    coord_1 = [150, 310]
                    coord_2 = [855, 310]
                    coord_3 = [510, 360]
                    score = [0, 0]
                    pause = False
                if event1.key == K_q:
                    score = [3, 3]
                    coord_1 = [150, 310]
                    coord_2 = [855, 310]
                    coord_3 = [510, 360]
                    angle_ball = 0
                    pause = False
                    gameOn = False
                    app_bool = True
                    prologOn1 = False
                    prologOn2 = False
                    player = False
                    bot = False
                    bot_2 = False
                    choosePlayer = True
                    setting = False
                    winner = False
                    print(bools_list)
            elif event1.type == QUIT:
                exit(0)


def choosing_a_player():
    global choosePlayer, prologOn1, prologOn2, bot, player, setting, bot_2, gameOn
    while choosePlayer:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_1:
                    prologOn1 = True
                    prologOn2 = False
                    bot = True
                    bot_2 = False
                    player = False
                    choosePlayer = False
                    gameOn = True
                    setting = False
                elif event.key == K_2:
                    prologOn2 = True
                    prologOn1 = False
                    bot = False
                    bot_2 = False
                    player = True
                    choosePlayer = False
                    gameOn = True
                    setting = False
                elif event.key == K_3:
                    prologOn1 = False
                    prologOn2 = False
                    bot_2 = True
                    bot = False
                    player = False
                    choosePlayer = False
                    gameOn = True
                    setting = False
                elif event.key == K_i:
                    setting = True
                    return
            elif event.type == QUIT:
                exit(0)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text1 = font.render(f'PONG GAME', False, YELLOW)
        text2 = font.render(f'[1] Player vs BOT', False, BLUE)
        text3 = font.render(f'[2] Player vs Player', False, BLUE)
        text4 = font.render(f'[3] BOT_1 vs BOT_2', False, BLUE)
        text5 = font.render(f'[I] Settings', False, BLUE)
        screen.blit(text1, (390, 290))
        screen.blit(text2, (350, 330))
        screen.blit(text3, (350, 370))
        screen.blit(text4, (350, 410))
        screen.blit(text5, (350, 450))
        pygame.display.flip()


def prolog_1():
    global prologOn1
    if prologOn1:
        while prologOn1:
            screen.fill(BLACK)
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        prologOn1 = False
                elif event.type == QUIT:
                    exit(0)
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text1 = font.render(f'Hi, it\'s a PONG game, where you have to beat', False, BLUE)
            text2 = font.render(f'a bot hitting his wall with a red ball', False, BLUE)
            text3 = font.render(f'Instructions', False, GREEN)
            text4 = font.render(f'[W] to move up your racket', False, GREEN)
            text5 = font.render(f'[S] to move down your racket', False, GREEN)
            text6 = font.render(f'[R] to rematch after goal or in pause', False, GREEN)
            text7 = font.render(f'[SPACE] to continue game after goal or in pause', False, GREEN)
            text8 = font.render(f'[ESC] to pause game', False, GREEN)
            text9 = font.render(f'NOW PRESS [SPACE] FOR A MATCH', False, RED)
            screen.blit(text1, (200, 140))
            screen.blit(text2, (200, 180))
            screen.blit(text3, (200, 220))
            screen.blit(text4, (200, 260))
            screen.blit(text5, (200, 300))
            screen.blit(text6, (200, 340))
            screen.blit(text7, (200, 380))
            screen.blit(text8, (200, 420))
            screen.blit(text9, (240, 500))
            pygame.display.flip()


def prolog_2():
    global prologOn2
    if prologOn2:
        while prologOn2:
            screen.fill((0, 0, 0))
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        prologOn2 = False
                elif event.type == QUIT:
                    exit(0)
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text1 = font.render(f'Hi, it\'s a PONG game, where you have to beat', False, BLUE)
            text2 = font.render(f'a player hitting his wall with a red ball', False, BLUE)
            text3 = font.render(f'Instructions (1 button - left racket, 2 button - right racket)', False, GREEN)
            text4 = font.render(f'[W], [KEY_UP] to move up your racket', False, GREEN)
            text5 = font.render(f'[S], [KEY_DOWN] to move down your racket', False, GREEN)
            text6 = font.render(f'[R] to rematch after goal or in pause', False, GREEN)
            text7 = font.render(f'[SPACE] to continue game after goal or in pause', False, GREEN)
            text8 = font.render(f'[ESC] to pause game', False, GREEN)
            text9 = font.render(f'NOW PRESS [SPACE] FOR A MATCH', False, RED)
            screen.blit(text1, (100, 140))
            screen.blit(text2, (100, 180))
            screen.blit(text3, (100, 220))
            screen.blit(text4, (100, 260))
            screen.blit(text5, (100, 300))
            screen.blit(text6, (100, 340))
            screen.blit(text7, (100, 380))
            screen.blit(text8, (100, 420))
            screen.blit(text9, (240, 500))
            pygame.display.flip()


def winners():
    global winner
    while winner:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    winner = False
                    return
            elif event.type == QUIT:
                exit(0)
        font = pygame.font.SysFont('Comic Sans MS', 50)
        if score[0] == final_point and score[1] == final_point:
            return
        if score[0] == final_point:
            text = font.render(f'The winner is left player :)', False, BLUE)
        else:
            text = font.render(f'The winner is right player :)', False, BLUE)
        text1 = font.render(f'The score is {score[0]} : {score[1]}', False, BLUE)
        text2 = font.render(f'To continue press [SPACE]', False, RED)
        screen.fill(BLACK)
        screen.blit(text, (200, 220))
        screen.blit(text1, (200, 300))
        screen.blit(text2, (200, 500))
        pygame.display.flip()


def game():
    global motion_1, motion_2, gameOn, app_bool, coord_1, coord_2, \
        coord_3, speed, dx, angle_ball, bot_1_tim, \
        bot_2_tim, choosePlayer, bot_2, bot, prologOn1, \
        prologOn2, player, setting, final_point, winner
    if bot_2:
        coord_2[1] += random.randint(-40, 40)
        coord_1[1] += random.randint(-40, 40)
    elif bot:
        coord_2[1] += random.randint(-40, 40)
    motion_1 = "STOP"
    motion_2 = "STOP"
    while gameOn:
        screen.fill(BLACK)
        paused = False
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if not bot_2:
                    if event.key == K_w:
                        motion_1 = "UP"
                    elif event.key == K_s:
                        motion_1 = "DOWN"
                if player:
                    if event.key == K_UP:
                        motion_2 = "UP"
                    elif event.key == K_DOWN:
                        motion_2 = "DOWN"
                elif event.key == K_ESCAPE:
                    paused = True
            elif event.type == KEYUP:
                if event.key in [K_w, K_s]:
                    motion_1 = "STOP"
                if event.key in [K_UP, K_DOWN]:
                    motion_2 = "STOP"
            elif event.type == QUIT:
                exit(0)

        # Left racket motion
        if motion_1 == "UP":
            if 50 < coord_1[1] - 15:
                coord_1 = [coord_1[0], coord_1[1] - dx]
        if motion_1 == "DOWN":
            if 570 > coord_1[1] + 15:
                coord_1 = [coord_1[0], coord_1[1] + dx]

        # Right racket motion
        if motion_2 == "UP":
            if 50 < coord_2[1] - 15:
                coord_2 = [coord_2[0], coord_2[1] - dx]
        if motion_2 == "DOWN":
            if 570 > coord_2[1] + 15:
                coord_2 = [coord_2[0], coord_2[1] + dx]

        # Collision with player
        if coord_1[0] <= coord_3[0] - 10 <= coord_1[0] + 20 and coord_1[1] <= coord_3[1] <= coord_1[1] + 100:
            if bot_2 and bot_1_tim >= 4:
                coord_1[1] += 10
                bot_1_tim = 0
            percentage = (coord_1[1] + 50 - coord_3[1]) / 100
            angle_ball = -180 * percentage
            if speed >= 3:
                speed -= 1
            bot_1_tim += 1

        # Collision with bot
        if coord_2[0] + 20 >= coord_3[0] + 10 >= coord_2[0] and coord_2[1] <= coord_3[1] <= coord_2[1] + 100:
            if bot_2_tim >= 4 and (bot or bot_2):
                coord_2[1] += 10
                bot_2_tim = 0
            percentage = (coord_2[1] + 50 - coord_3[1]) / 100
            angle_ball = - 180 + 180 * percentage
            if angle_ball == 0:
                angle_ball = 180
            elif -75 <= angle_ball <= -90:
                angle_ball = -70
            elif 75 < angle_ball <= 90:
                angle_ball = 70
            bot_2_tim += 1

        # Collision with upper wall
        if 50 - 15 <= coord_3[1] - 10 <= 50 + 15:
            angle_ball = -angle_ball

        # Collision with lower wall
        if 670 + 15 >= coord_3[1] + 10 >= 670 - 15:
            angle_ball = -angle_ball

        # BOT
        if bot or bot_2:
            if coord_3[1] - 30 < coord_2[1] and coord_2[1] >= 50 + 15:
                if not 90 <= angle_ball <= 270:
                    coord_2[1] -= 4
            if coord_3[1] + 30 > coord_2[1] + 100 and coord_2[1] + 100 <= 670 - 15:
                if not -90 >= angle_ball >= -270:
                    coord_2[1] += 4
        if bot_2:
            if coord_3[1] - 30 < coord_1[1] and coord_1[1] >= 50 + 15:
                if not -90 <= angle_ball <= 90:
                    coord_1[1] -= 4
            if coord_3[1] + 30 > coord_1[1] + 100 and coord_1[1] + 100 <= 670 - 15:
                if not -270 >= angle_ball >= -450:
                    coord_1[1] += 4

        # Coordinates of a ball
        coord_3[0] += round(dx * math.cos(math.radians(angle_ball)))
        coord_3[1] += round(dx * math.sin(math.radians(angle_ball)))

        # Rackets
        square1.surf.fill(left_racket_color)
        square2.surf.fill(right_racket_color)
        screen.blit(square1.surf, coord_1)
        screen.blit(square2.surf, coord_2)

        # Borders of a field
        pygame.draw.line(screen, WHITE, (100, 50), (100, 677), 14)
        pygame.draw.line(screen, WHITE, (100, 670), (927, 670), 14)
        pygame.draw.line(screen, WHITE, (920, 670), (920, 44), 14)
        pygame.draw.line(screen, WHITE, (920, 50), (94, 50), 14)

        # Internal lines of field
        pygame.draw.line(screen, WHITE, (509, 50), (509, 670), 6)
        pygame.draw.circle(screen, WHITE, (510, 360), 100, 6)
        pygame.draw.circle(screen, WHITE, (510, 360), 15, 15)

        # Ball
        pygame.draw.circle(screen, ball_color, coord_3, 10, 10)

        # Score
        my_font = pygame.font.SysFont('Comic Sans MS', 30)
        player_1 = 'PLAYER_1'
        player_2 = 'BOT'
        if player:
            player_2 = 'PLAYER_2'
        if bot_2:
            player_1 = 'BOT_1'
            player_2 = 'BOT_2'
        text_surface = my_font.render(f'PONG SCORE [{player_1} : {player_2}] [{score[0]} : {score[1]}]', False, WHITE)
        screen.blit(text_surface, (250, 0))

        # Collision with left wall
        if coord_3[0] - 10 <= 100:
            score[1] += 1
            coord_3 = [510, 360]
            angle_ball = 180
            speed = final_speed
            if not bot_2:
                font = pygame.font.SysFont('Comic Sans MS', 30)
                text = font.render(f'[SPACE] to continue or [R] to restart', False, RED)
                screen.blit(text, (250, 130))
                pygame.display.flip()
                goal()

        # Collision with right wall
        if coord_3[0] + 10 >= 920:
            score[0] += 1
            coord_3 = [510, 360]
            angle_ball = 0
            speed = final_speed
            if not bot_2:
                font = pygame.font.SysFont('Comic Sans MS', 30)
                text = font.render(f'[SPACE] to continue or [R] to restart', False, RED)
                screen.blit(text, (250, 130))
                pygame.display.flip()
                goal()

        # Pause
        if paused:
            font = pygame.font.SysFont('Comic Sans MS', 30)
            text = font.render(f'[SPACE] continue', False, RED)
            text1 = font.render(f'[R] restart', False, RED)
            text2 = font.render(f'[Q] return to main menu', False, RED)
            screen.blit(text, (120, 70))
            screen.blit(text1, (120, 110))
            screen.blit(text2, (120, 150))
            pygame.display.flip()
            pause_game()

        # Cycle
        pygame.time.delay(speed)
        pygame.display.flip()
        if final_point in score:
            gameOn = False
            app_bool = True
            choosePlayer = True
            prologOn1 = False
            prologOn2 = False
            player = False
            bot = False
            bot_2 = False
            choosePlayer = True
            winner = True
            setting = False
            winners()


def settings():
    global speed, dx, angle_ball, ball_color, \
        left_racket_color, right_racket_color, \
        setting, final_point, speed, final_speed
    speed = 20
    while setting:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    if 150 - 15 <= event.pos[1] <= 150 + 15 and 335 <= event.pos[0] <= 770:
                        ball_color = colors[(event.pos[0] - 335) // 50]
                    elif 220 - 15 <= event.pos[1] <= 220 + 15 and 335 <= event.pos[0] <= 770:
                        left_racket_color = colors[(event.pos[0] - 335) // 50]
                    elif 290 - 15 <= event.pos[1] <= 290 + 15 and 335 <= event.pos[0] <= 770:
                        right_racket_color = colors[(event.pos[0] - 335) // 50]
                    elif 360 <= event.pos[1] <= 385 and 345 <= event.pos[0] <= 365:  # point 3
                        final_point = 3
                    elif 360 <= event.pos[1] <= 385 and 385 <= event.pos[0] <= 410:  # point 5
                        final_point = 5
                    elif 360 <= event.pos[1] <= 385 and 435 <= event.pos[0] <= 455:  # point 7
                        final_point = 7
                    elif 360 <= event.pos[1] <= 385 and 480 <= event.pos[0] <= 515:  # point 10
                        final_point = 10
                    elif 435 <= event.pos[1] <= 470 and 330 <= event.pos[0] <= 430:  # speed 20
                        speed = 20
                    elif 435 <= event.pos[1] <= 470 and 450 <= event.pos[0] <= 590:  # speed 15
                        speed = 15
                    elif 435 <= event.pos[1] <= 470 and 610 <= event.pos[0] <= 700:  # speed 10
                        speed = 10
                    elif 435 <= event.pos[1] <= 470 and 720 <= event.pos[0] <= 830:  # speed 5
                        speed = 5
            elif event.type == KEYDOWN:
                if event.key == K_i:
                    setting = False
                    final_speed = speed
                    choosing_a_player()
                if event.key == K_r:
                    setting = False
                    ball_color = RED
                    left_racket_color = WHITE
                    right_racket_color = WHITE
                    choosing_a_player()
            elif event.type == QUIT:
                exit(0)

        # Final point circle coordinates
        final_point_coord = []
        if final_point == 3:
            final_point_coord = [353, 400]
        elif final_point == 5:
            final_point_coord = [397, 400]
        elif final_point == 7:
            final_point_coord = [443, 400]
        elif final_point == 10:
            final_point_coord = [495, 400]

        # Speed circle coordinates
        speed_coord = []
        if speed >= 20:
            speed_coord = [380, 480]
        elif 20 > speed >= 15:
            speed_coord = [520, 480]
        elif 15 > speed >= 10:
            speed_coord = [650, 480]
        elif 10 >= speed:
            speed_coord = [775, 480]

        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'SETTINGS', False, GREEN)
        text1 = font.render(f'Ball: ', False, ball_color)
        text2 = font.render(f'Left racket: ', False, left_racket_color)
        text3 = font.render(f'Right racket: ', False, right_racket_color)
        text4 = font.render(f'Choose final point:   3   5   7   10', False, WHITE)
        text5 = font.render(f'Choose ball speed:  SLOW   MEDIUM   FAST   SONIC', False, WHITE)
        text6 = font.render(f'[I] to save settings', False, RED)
        text7 = font.render(f'[R] to reset settings', False, RED)
        screen.blit(text, (420, 50))
        screen.blit(text1, (100, 130))
        screen.blit(text2, (100, 200))
        screen.blit(text3, (100, 270))
        screen.blit(text4, (60, 350))
        screen.blit(text5, (60, 430))
        screen.blit(text6, (360, 600))
        screen.blit(text7, (360, 650))
        x = 350

        # Chosen final point
        pygame.draw.circle(screen, WHITE, final_point_coord, 5, 5)

        # Chosen speed
        pygame.draw.circle(screen, WHITE, speed_coord, 5, 5)

        # Chosen ball color
        pygame.draw.circle(screen, ball_color, (70, 150), 15, 15)

        # Chosen left racket color
        pygame.draw.circle(screen, left_racket_color, (70, 220), 15, 15)

        # Chosen right racket color
        pygame.draw.circle(screen, right_racket_color, (70, 290), 15, 15)

        for color in colors:
            pygame.draw.circle(screen, color, (x, 150), 15, 15)
            pygame.draw.circle(screen, color, (x, 220), 15, 15)
            pygame.draw.circle(screen, color, (x, 290), 15, 15)
            x += 50

        pygame.display.flip()


if __name__ == "__main__":
    while app_bool:
        print("Choosing_player_screen")
        print(bools_list)
        choosing_a_player()
        while setting:
            print("Settings_screen")
            settings()
        if prologOn1:
            print("Prolog_1_screen")
            prolog_1()
        elif prologOn2:
            print("Prolog_2_screen")
            prolog_2()
        print("Game_screen")
        print(bools_list)
        game()
        score = [0, 0]
