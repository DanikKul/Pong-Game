import pygame
import math


from pygame.locals import *


class Square(pygame.sprite.Sprite):
    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((20, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()


pygame.init()

screen = pygame.display.set_mode((1020, 720))
pygame.display.set_caption("DOS PONG")
screen.fill((0, 0, 0))

square1 = Square()
square2 = Square()

coord_1 = [150, 310]
coord_2 = [855, 310]
coord_3 = [510, 360]
angle_ball = 0
speed = 20
dx = 5
score = [0, 0]

gameOn = True
prologOn1 = False
prologOn2 = False
player = False
bot = False
choosePlayer = True
pygame.font.init()


def goal():
    global score, coord_1, coord_2, coord_3
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


def pause_game():
    pause = True
    global score, coord_1, coord_2, coord_3
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
            elif event1.type == QUIT:
                exit(0)


while choosePlayer:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_1:
                prologOn1 = True
                prologOn2 = False
                bot = True
                player = False
                choosePlayer = False
            elif event.key == K_2:
                prologOn2 = True
                prologOn1 = False
                bot = False
                player = True
                choosePlayer = False
        elif event.type == QUIT:
            exit(0)
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text1 = font.render(f'PONG GAME', False, (255, 255, 0))
    text2 = font.render(f'[1] Player vs BOT', False, (0, 0, 255))
    text3 = font.render(f'[2] Player vs Player', False, (0, 0, 255))
    screen.blit(text1, (390, 290))
    screen.blit(text2, (350, 330))
    screen.blit(text3, (350, 370))
    pygame.display.flip()

if prologOn1:
    while prologOn1:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    prologOn1 = False
            elif event.type == QUIT:
                exit(0)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text1 = font.render(f'Hi, it\'s a PONG game, where you have to beat', False, (0, 0, 255))
        text2 = font.render(f'a bot hitting his wall with a red ball', False, (0, 0, 255))
        text3 = font.render(f'Instructions', False, (0, 255, 0))
        text4 = font.render(f'[W] to move up your racket', False, (0, 255, 0))
        text5 = font.render(f'[S] to move down your racket', False, (0, 255, 0))
        text6 = font.render(f'[R] to rematch after goal or in pause', False, (0, 255, 0))
        text7 = font.render(f'[SPACE] to continue game after goal or in pause', False, (0, 255, 0))
        text8 = font.render(f'[ESC] to pause game', False, (0, 255, 0))
        text9 = font.render(f'NOW PRESS [SPACE] FOR A MATCH', False, (255, 0, 0))
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

elif prologOn2:
    while prologOn2:
        screen.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    prologOn2 = False
            elif event.type == QUIT:
                exit(0)
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text1 = font.render(f'Hi, it\'s a PONG game, where you have to beat', False, (0, 0, 255))
        text2 = font.render(f'a player hitting his wall with a red ball', False, (0, 0, 255))
        text3 = font.render(f'Instructions (1 button - left racket, 2 button - right racket)', False, (0, 255, 0))
        text4 = font.render(f'[W], [KEY_UP] to move up your racket', False, (0, 255, 0))
        text5 = font.render(f'[S], [KEY_DOWN] to move down your racket', False, (0, 255, 0))
        text6 = font.render(f'[R] to rematch after goal or in pause', False, (0, 255, 0))
        text7 = font.render(f'[SPACE] to continue game after goal or in pause', False, (0, 255, 0))
        text8 = font.render(f'[ESC] to pause game', False, (0, 255, 0))
        text9 = font.render(f'NOW PRESS [SPACE] FOR A MATCH', False, (255, 0, 0))
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

while gameOn:
    screen.fill((0, 0, 0))
    paused = False
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_w:
                if 50 < coord_1[1] - 30:
                    coord_1 = [coord_1[0], coord_1[1] - 30]
            elif event.key == K_s:
                if 570 > coord_1[1] + 30:
                    coord_1 = [coord_1[0], coord_1[1] + 30]
            if player:
                if event.key == K_UP:
                    if 50 < coord_2[1] - 30:
                        coord_2 = [coord_2[0], coord_2[1] - 30]
                elif event.key == K_DOWN:
                    if 570 > coord_2[1] + 30:
                        coord_2 = [coord_2[0], coord_2[1] + 30]
            elif event.key == K_ESCAPE:
                paused = True

        elif event.type == QUIT:
            exit(0)

    # Collision with player
    if coord_1[0] <= coord_3[0] - 10 <= coord_1[0] + 20 and coord_1[1] <= coord_3[1] <= coord_1[1] + 100:
        percentage = (coord_1[1] + 50 - coord_3[1]) / 100
        angle_ball = -180 * percentage
        if speed >= 5:
            speed -= 1

    # Collision with bot
    if coord_2[0] + 20 >= coord_3[0] + 10 >= coord_2[0] and coord_2[1] <= coord_3[1] <= coord_2[1] + 100:
        percentage = (coord_2[1] + 50 - coord_3[1]) / 100
        angle_ball = - 180 + 180 * percentage
        if angle_ball == 0:
            angle_ball = 180
        elif -75 <= angle_ball <= -90:
            angle_ball = -70
        elif 75 < angle_ball <= 90:
            angle_ball = 70

    # Collision with upper wall
    if 50 - 15 <= coord_3[1] - 10 <= 50 + 15:
        angle_ball = -angle_ball

    # Collision with lower wall
    if 670 + 15 >= coord_3[1] + 10 >= 670 - 15:
        angle_ball = -angle_ball

    # BOT
    if bot:
        if coord_3[1] - 30 < coord_2[1] and coord_2[1] >= 50 + 15:
            if not 90 <= angle_ball <= 270:
                coord_2[1] -= 4
        if coord_3[1] + 30 > coord_2[1] + 100 and coord_2[1] + 100 <= 670 - 15:
            if not -90 >= angle_ball >= -270:
                coord_2[1] += 4


    coord_3[0] += round(dx * math.cos(math.radians(angle_ball)))
    coord_3[1] += round(dx * math.sin(math.radians(angle_ball)))

    screen.blit(square1.surf, coord_1)
    screen.blit(square2.surf, coord_2)

    pygame.draw.line(screen, (255, 255, 255), (100, 50), (100, 677), 14)
    pygame.draw.line(screen, (255, 255, 255), (100, 670), (927, 670), 14)
    pygame.draw.line(screen, (255, 255, 255), (920, 670), (920, 44), 14)
    pygame.draw.line(screen, (255, 255, 255), (920, 50), (94, 50), 14)
    pygame.draw.line(screen, (255, 255, 255), (509, 50), (509, 670), 6)
    pygame.draw.circle(screen, (255, 255, 255), (510, 360), 100, 6)
    pygame.draw.circle(screen, (255, 255, 255), (510, 360), 15, 15)
    pygame.draw.circle(screen, (255, 0, 0), coord_3, 10, 10)

    my_font = pygame.font.SysFont('Comic Sans MS', 30)
    sec_player = 'BOT'
    if player:
        sec_player = 'PLAYER_2'
    text_surface = my_font.render(f'PONG SCORE [PLAYER_1 : {sec_player}] [{score[0]} : {score[1]}]', False, (255, 255, 255))
    screen.blit(text_surface, (250, 0))

    # Collision with left wall
    if coord_3[0] - 10 <= 100:
        score[1] += 1
        coord_3 = [510, 360]
        angle_ball = 180
        speed = 20
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'[SPACE] to continue or [R] to restart', False, (255, 0, 0))
        screen.blit(text, (250, 130))
        pygame.display.flip()
        goal()

    # Collision with right wall
    if coord_3[0] + 10 >= 920:
        score[0] += 1
        coord_3 = [510, 360]
        angle_ball = 0
        speed = 20
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'[SPACE] to continue or [R] to restart', False, (255, 0, 0))
        screen.blit(text, (250, 130))
        pygame.display.flip()
        goal()

    if paused:
        font = pygame.font.SysFont('Comic Sans MS', 30)
        text = font.render(f'[SPACE] to continue', False, (255, 0, 0))
        text1 = font.render(f'[R] to restart', False, (255, 0, 0))
        screen.blit(text, (120, 70))
        screen.blit(text1, (120, 110))
        pygame.display.flip()
        pause_game()

    pygame.time.delay(speed)
    pygame.display.flip()
