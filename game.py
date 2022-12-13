import pygame as pg
import pygame.draw as dr
from random import randint as rint

pg.init()


def esc_exit():
    """
    exit game by escape pressing
    :return: None
    """
    global finished, event
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            finished = True
            exit()


def player():
    """
    Makes a player movement object
    :return: None
    """
    global x, y
    pers_speed = 5

    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT]:
        x -= pers_speed
    if keys[pg.K_RIGHT]:
        x += pers_speed
    if keys[pg.K_UP]:
        y -= pers_speed
    if keys[pg.K_DOWN]:
        y += pers_speed

    screen.fill('Black')
    dr.circle(screen, 'Red', (x, y), 10)


def new_ball_moves():
    global x1, y1, speed_x, speed_y
    if x1 > 495:
        speed_x = -5
        speed_y = rint(-5, 6)
    if x1 < 5:
        speed_x = 5
        speed_y = rint(-5, 6)
    if y1 > 495:
        speed_y = -5
        speed_x = rint(-5, 6)
    if y1 < 5:
        speed_y = 5
        speed_x = rint(-5, 6)
    x1 += speed_x
    y1 += speed_y
    dr.circle(screen, 'White', (x1, y1), 10)


FPS = 20
size = [500, 500]
screen = pg.display.set_mode(size)

x, y = 250, 250
x1, y1 = 300, 250
speed_x, speed_y = 5, 0
finished = False

pg.display.update()
clock = pg.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        esc_exit()
    player()
    new_ball_moves()

    pg.display.update()
