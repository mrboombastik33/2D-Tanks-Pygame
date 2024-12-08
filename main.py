import pygame as pg
from Tank import Tank
from enum import Enum
import sys

class Direction(Enum):
    UP = 0
    RIGHT = -90
    LEFT = 90
    DOWN = 180

pg.init()

window = pg.display.set_mode((500, 500))

WIDTH, HEIGHT = pg.display.get_surface().get_size()

done = False

tank = Tank('tank_blue.jpg', 100, 100, 3.5)

group = pg.sprite.Group()
group.add(tank)

clock = pg.time.Clock()

last_direction = 0

while not done:

    window.fill((80, 80, 80))

    group.draw(window)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = False


    direction = pg.key.get_pressed()

    if direction[pg.K_RIGHT] and tank.rect.right < WIDTH:
        tank.move(tank.speed, 0)
        tank.set_rotation(-90)

    if direction[pg.K_LEFT] and tank.rect.left > 0:
        tank.move(-tank.speed, 0)
        tank.set_rotation(90)

    if direction[pg.K_UP] and tank.rect.top > 0:
        tank.move(0, -tank.speed)
        tank.set_rotation(0)

    if direction[pg.K_DOWN] and tank.rect.bottom < HEIGHT:
        tank.move(0, tank.speed)
        tank.set_rotation(180)


    clock.tick(120)

    pg.display.update()


pg.quit()
sys.exit()











