import pygame as pg
from Tank import Tank
import sys
from Direction import Direction
from Block import Block
from settings import *

pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT)) #Встановлюю розмір вікна

last_fire_time, fire_interval = 0, 500
run = True

# Створюю основні об'єкти і закидую їх в групу
tank = Tank(f'{SPRITE_IMAGES}/tank_blue.png', 100, 100, 2)

unbreakable = Block(f'{SPRITE_IMAGES}/tankBody_green.png', 200, 200, 1)
breakable = Block(f'{SPRITE_IMAGES}/sandbagBrown.png', 300, 300, 0)


group = pg.sprite.Group()
group.add(tank)
group.add(unbreakable)
group.add(breakable)


map = [[0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 1 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0, 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0],
       [0, 0, 0, 0 , 0, 0 , 0, 0 , 0, 0]]


# Обмеження для мапи по краям екрану
for i in range(len(map)):
    for j in range(len(map[i])):
        if i == 0 or i == 9 or j == 0 or j == 9:
            map[i][j] = 1

clock = pg.time.Clock() # Клок для ФПС

bullets = []
list_of_blocks = []

for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == 1:  # Блок що можна знищити
            x = j * cell_size
            y = i * cell_size
            list_of_blocks.append(Block(f'{SPRITE_IMAGES}/sandbagBrown.png', x, y, 0))

group.add(list_of_blocks)


while run:
    clock.tick(240)
    current_time = pg.time.get_ticks()

    key = pg.key.get_pressed() # key - зчитує натиснуту клавішу
    dir = 0

    # Рух танку
    if key[pg.K_UP]:
        dir = Direction.UP
    if key[pg.K_DOWN]:
        dir = Direction.DOWN
    if key[pg.K_LEFT]:
        dir = Direction.LEFT
    if key[pg.K_RIGHT]:
        dir = Direction.RIGHT

    tank.do_move(dir, group)

    # Створення пулі при нажатті пробілу
    if key[pg.K_SPACE] and current_time - last_fire_time >= fire_interval:
        last_fire_time = current_time
        bullets.append(tank.fire(f'{SPRITE_IMAGES}/bulletBlue1.png'))
        group.add(bullets[-1])

    # Логіка руху пулі
    for index, bullet in enumerate(bullets):
        if bullet.do_move(bullets, group):
            bullet.kill()
            bullets.pop(index)

    window.fill((80, 80, 80))  # Заповнюю вікно сірим кольором

    # Малюю всі об'єкти, що знахдяться в групі
    group.draw(window)

    # Event-Handler (зчитує всі івенти (нажаття клавіш і тд) один за цикл)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    # Перемальовка кадру
    pg.display.update()

pg.quit()
sys.exit()













