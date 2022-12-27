import pygame as pg
import pygame.draw as dr
import pygame.mouse as mouse
from random import randint

pg.init()


def esc_exit(finished, event):
    """
    :param finished: Variable close the game
    :param event: Variable for game processes
    :return: None
    """
    if event.type == pg.KEYDOWN:
        if event.key == pg.K_ESCAPE:
            finished = True
            exit()


class Object:
    def __init__(self):
        self.x, self.y, self.size = 250, 250, 10
        self.speed = 5  # Object speed


class Keys_player(Object):
    """
    Class for controlling ball
    """

    def moves(self, screen):
        """
        move player method
        :param screen: variable to work on screen
        :return: None
        """
        self.keys = pg.key.get_pressed()
        if self.keys[pg.K_LEFT]:
            self.x -= self.speed
        if self.keys[pg.K_RIGHT]:
            self.x += self.speed
        if self.keys[pg.K_UP]:
            self.y -= self.speed
        if self.keys[pg.K_DOWN]:
            self.y += self.speed

        # If Player ball coming to screen frame:
        if self.x < 5:
            self.x = 495
        if self.x > 495:
            self.x = 5
        if self.y < 5:
            self.y = 495
        if self.y > 495:
            self.y = 5

        screen.fill('Black')
        dr.circle(screen, 'Red', (self.x, self.y), self.size)  # Drawing player ball

    def collision(self):
        pass


class Mouse_player():

    def moves(self, screen):
        self.x, self.y = mouse.get_pos()[0], mouse.get_pos()[1]
        dr.circle(screen, 'Yellow', (self.x, self.y), 20)
        mouse.set_visible(False)


class NPC(Object):
    """
    Class for not control ball
    """
    def __init__(self):
        super().__init__()
        self.y += 12
        self.x += 12
        self.color = (randint(0, 255), randint(0, 255), randint(0, 255))
        self.speed_x = self.speed
        self.speed_y = self.speed

    def moves(self, screen):
        """
        Move NPC method
        :param screen: variable to work on screen
        :return:
        """
        if self.x > 495:  # Right wall
            self.speed_x = -5
            self.speed_y = randint(-5, 6)
        if self.x < 5:
            self.speed_x = 5  # Left wall
            self.speed_y = randint(-5, 6)
        if self.y > 495:  # Bottom
            self.speed_y = -5
            self.speed_x = randint(-5, 6)
        if self.y < 5:  # Top
            self.speed_y = 5
            self.speed_x = randint(-5, 6)
        self.x += self.speed_x
        self.y += self.speed_y
        dr.circle(screen, self.color, (self.x, self.y), self.size)

    def collision(self):
        """
        Method for collisions with Player
        :return: None
        """
        self.speed_x = -self.speed_x
        self.speed_y = -self.speed_y


def main():
    FPS = 20
    size = [500, 500]
    screen = pg.display.set_mode(size)

    finished = False

    pg.display.update()
    clock = pg.time.Clock()
    player = Keys_player()
    mouse_player = Mouse_player()
    npc = [NPC()]
    while not finished:
        clock.tick(FPS)
        for event in pg.event.get():
            esc_exit(finished, event)
        player.moves(screen)
        mouse_player.moves(screen)
        for i in npc:
            i.moves(screen)
            if abs(player.x - i.x) < 11 and abs(player.y - i.y) < 11:
                i.collision()
                npc.append(NPC())
        pg.display.update()


main()
