import pygame as pg
from Tank import Tank
import sys
from Direction import Direction
from Block import Block

pg.init()

window = pg.display.set_mode((500, 500)) #Встановлюю розмір вікна
WIDTH, HEIGHT = pg.display.get_surface().get_size()   #Встановлюю фізичні межі вікна

last_fire_time, fire_interval = 0, 500
run = True

# Створюю основні об'єкти і закидую їх в групу
tank = Tank('tank_blue.jpg', 100, 100, 2)

unbreakable = Block('tankBody_green.png', 200, 200, 1)
breakable = Block('sandbagBrown.png', 300, 300, 0)


group = pg.sprite.Group()
group.add(tank)
group.add(unbreakable)
group.add(breakable)



clock = pg.time.Clock() # Клок для ФПС

bullets = []

while run:

    clock.tick(60)
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
        bullets.append(tank.fire('bulletBlue1.png'))
        group.add(bullets[-1])

    # Логіка руху пулі
    for bullet in bullets:
        bullet.do_move(bullets, group)

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













