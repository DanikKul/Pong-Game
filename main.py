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
prologOn = True
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


while prologOn:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                prologOn = False
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
    screen.blit(text1, (270, 140))
    screen.blit(text2, (270, 180))
    screen.blit(text3, (270, 220))
    screen.blit(text4, (270, 260))
    screen.blit(text5, (270, 300))
    screen.blit(text6, (270, 340))
    screen.blit(text7, (270, 380))
    screen.blit(text8, (270, 420))
    screen.blit(text9, (270, 500))
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
            elif event.key == K_ESCAPE:
                paused = True

        elif event.type == QUIT:
            exit(0)

    # Collision with player
    if coord_1[0] <= coord_3[0] - 10 <= coord_1[0] + 20 and coord_1[1] <= coord_3[1] <= coord_1[1] + 100:
        percentage = (coord_1[1] + 50 - coord_3[1]) / 100
        angle_ball = -180 * percentage
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
    text_surface = my_font.render(f'PONG SCORE [PLAYER : BOT] [{score[0]} : {score[1]}]', False, (255, 255, 255))
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
