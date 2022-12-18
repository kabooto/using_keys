import pygame as pg
import pygame.draw as dr
from random import randint

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


class Player:

    def __init__(self, screen):
        self.x, self.y = 250, 250
        self.size = 10
        dr.circle(screen, 'Red', (self.x, self.y), self.size)

    def moves(self, screen):
        self.pers_speed = 5
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_LEFT]:
            self.x -= self.pers_speed
        if self.keys[pg.K_RIGHT]:
            self.x += self.pers_speed
        if self.keys[pg.K_UP]:
            self.y -= self.pers_speed
        if self.keys[pg.K_DOWN]:
            self.y += self.pers_speed
        screen.fill('Black')
        dr.circle(screen, 'Red', (self.x, self.y), self.size)

    def collision(self):
        pass


class NPC:
    def __init__(self,screen):
        self.x, self.y = 250, 5
        self.size = 10
        dr.circle(screen, 'White', (self.x, self.y), self.size)

    def moves(self, screen):
        self.speed_x = 0
        self.speed_y = 5
        if self.x > 495:
            self.speed_x = -5
            self.speed_y = randint(-5, 6)
        if self.x < 5:
            self.speed_x = 5
            self.speed_y = randint(-5, 6)
        if self.y > 495:
            self.speed_y = -5
            self.speed_x = randint(-5, 6)
        if self.y < 5:
            self.speed_x = 5
            self.speed_x = randint(-5, 6)
        self.x += self.speed_x
        self.y += self.speed_y
        dr.circle(screen, 'White', (self.x, self.y), self.size)

    def collision(self):
        pass
'''def ball_npc():
    """
    Makes not manage ball movements
    :return: None
    """
    global x1, y1, speed_x, speed_y
    if x1 > 495:  # right wall
        speed_x = -5
        speed_y = randint(-5, 6)
    if x1 < 5:  # left wall
        speed_x = 5
        speed_y = randint(-5, 6)
    if y1 > 495:  # Screen top
        speed_y = -5
        speed_x = randint(-5, 6)
    if y1 < 5:  # Screen bottom
        speed_y = 5
        speed_x = randint(-5, 6)
    x1 += speed_x
    y1 += speed_y
    dr.circle(screen, 'White', (x1, y1), 10)'''


def main():
    global event, x1, y1, x2, y2, speed_x, speed_y, speed_x2, speed_y2
    FPS = 20
    size = [500, 500]
    screen = pg.display.set_mode(size)

    x1, y1 = 300, 250
    x2, y2 = 0, 0
    speed_x, speed_y = 5, 0
    speed_x2, speed_y2 = 5, 0
    finished = False

    pg.display.update()
    clock = pg.time.Clock()
    player = Player(screen)
    npc = NPC(screen)
    while not finished:
        clock.tick(FPS)
        for event in pg.event.get():
            esc_exit()
        #ball_player()
        player.moves(screen)
        npc.moves(screen)
        pg.display.update()

main()
