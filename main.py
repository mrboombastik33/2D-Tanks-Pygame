import pygame as pg
from Tank import Tank
import sys

pg.init()

window = pg.display.set_mode((500, 500)) #Встановлюю розмір вікна

WIDTH, HEIGHT = pg.display.get_surface().get_size()   #Встановлюю фізичні межі вікна

done = False

# Створюю основні об'єкти і закидую їх в групу
tank = Tank('tank_blue.jpg', 100, 100, 2)
#bullet = Bullet('bulletBlue1.png', 200, 150, 3.5)
group = pg.sprite.Group()
group.add(tank)
#group.add(bullet)

# Клок для ФПС
clock = pg.time.Clock()

while not done:

    window.fill((80, 80, 80)) #Заповнюю вікно сірим кольором
    key = pg.key.get_pressed() #direction - зчитує натиснуту клавішу


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


    # Малюю всі об'єкти, що знахдяться в групі
    group.draw(window)

    # Event-Handler (зчитує всі івенти (нажаття клавіш і тд) один за цикл)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = False

    clock.tick(120)

    # Перемальовка кадру
    pg.display.update()

pg.quit()
sys.exit()











