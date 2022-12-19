import pygame as pg
import pygame.draw as dr
from random import randint

pg.init()


def esc_exit(finished, event):
    """
    exit game by escape pressing
    :return: None
    """
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
    def __init__(self, screen):
        self.x, self.y = 270, 5
        self.size = 10
        dr.circle(screen, 'White', (self.x, self.y), self.size)
        self.speed_x = 0
        self.speed_y = 5

    def moves(self, screen):
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
            self.speed_y = 5
            self.speed_x = randint(-5, 6)
        self.x += self.speed_x
        self.y += self.speed_y
        dr.circle(screen, 'White', (self.x, self.y), self.size)

    def collision(self):
        self.speed_x = -self.speed_x
        self.speed_y = -self.speed_y


def main():
    FPS = 20
    size = [500, 500]
    screen = pg.display.set_mode(size)

    finished = False

    pg.display.update()
    clock = pg.time.Clock()
    player = Player(screen)
    npc = NPC(screen)
    while not finished:
        clock.tick(FPS)
        for event in pg.event.get():
            esc_exit(finished, event)
        player.moves(screen)
        npc.moves(screen)
        if abs(player.x - npc.x) < 11 and abs(player.y - npc.y) < 11:
            npc.collision()
        pg.display.update()


main()
