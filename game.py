import pygame as pg
import pygame.draw as dr

pg.init()


def esc_exit():
    global finished, event
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            finished = True
            pg.quit()


FPS = 10
size = [500, 500]
screen = pg.display.set_mode(size)

finished = False

x, y = 250, 250
pers_speed = 5
pg.display.update()
clock = pg.time.Clock()
while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        esc_exit()

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
    pg.display.update()
