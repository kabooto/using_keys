import pygame as pg
import pygame.draw as dr

pg.init()


def esc_exit():
    global finished, event
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            finished = True
            pg.quit()


FPS = 1
size = [500, 500]
screen = pg.display.set_mode(size)

finished = False

pg.display.update()
clock = pg.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        esc_exit()
