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

obj = Block('tankBody_green.png', 125, 125)

group = pg.sprite.Group()
group.add(tank)
group.add(obj)

# Клок для ФПС
clock = pg.time.Clock()

bullets = []

while run:
    clock.tick(60)

    key = pg.key.get_pressed() # key - зчитує натиснуту клавішу

    current_time = pg.time.get_ticks()

    # Створення пулі при нажатті пробілу
    if key[pg.K_SPACE] and current_time - last_fire_time >= fire_interval:
        last_fire_time = current_time
        bullets.append(tank.fire('bulletBlue1.png'))
        group.add(bullets[-1])

    # Логіка руху пулі
    for bullet in bullets:
        bullet.do_move(bullets)

    # Логіка руху танка
    if key[pg.K_RIGHT] and tank.rect.right < WIDTH:
        tank.move(tank.speed, 0)
        tank.set_rotation(90)

    if key[pg.K_LEFT] and tank.rect.left > 0:
        tank.move(-tank.speed, 0)
        tank.set_rotation(-90)

    if key[pg.K_UP] and tank.rect.top > 0:
        tank.move(0, -tank.speed)
        tank.set_rotation(180)

    if key[pg.K_DOWN] and tank.rect.bottom < HEIGHT:
        tank.move(0, tank.speed)
        tank.set_rotation(0)

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











