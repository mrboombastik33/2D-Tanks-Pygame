import pygame as pg
import sys
from Tank import Tank
from Direction import Direction
from Block import Block
from settings import *
import json
from calling_functions import *



class Game:
    def __init__(self):
        pg.init()

        # Ініціалізація гри
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True

        # Групи та списки для об'єктів
        self.all_sprites = pg.sprite.Group()
        self.tanks = []
        self.bullets = []
        self.list_of_blocks = []


        self.map = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 2, 0, 0, 1, 0, 2, 0, 0],
                    [0, 0, 2, 0, 0, 0, 0, 2, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # Загружаємо ассети програми
        self.init_objects()

    def init_objects(self):
        self.create_map_blocks()

        # Танк
        tank = Tank(f'{SPRITE_IMAGES}/tank_blue.png', 100, 100, 2, 1)
        tank2 = Tank(f'{SPRITE_IMAGES}/tank_red.png', 300, 300, 2, 2)

        self.tanks.append(tank)
        self.all_sprites.add(tank)

        self.tanks.append(tank2)
        self.all_sprites.add(tank2)

        # # Статичні блоки
        # unbreakable = Block(f'{SPRITE_IMAGES}/tankBody_green.png', 200, 200, 1)
        # breakable = Block(f'{SPRITE_IMAGES}/sandbagBrown.png', 300, 300, 0)
        # self.all_sprites.add(unbreakable, breakable)
        # self.list_of_blocks.append(unbreakable)
        # self.list_of_blocks.append(breakable)

    def _create_boundary(self):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if i == 0 or i == 9 or j == 0 or j == 9:
                    self.map[i][j] = 1

    def create_map_blocks(self):
        self._create_boundary()
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                x = j * cell_size
                y = i * cell_size
                if self.map[i][j] == 1:
                    block = Block(f'{SPRITE_IMAGES}/barricadeWood.png', x, y, 1)
                if self.map[i][j] == 2:
                    block = Block(f'{SPRITE_IMAGES}/sandbagBrown.png', x, y, 0)
                self.list_of_blocks.append(block)
        self.all_sprites.add(self.list_of_blocks)

    def run(self):
        while self.running:
            self.clock.tick(FPS)
            self.handle_events()
            self.update()
            pg.display.update()
        pg.quit()
        sys.exit()

    def handle_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False

    def update(self):
        self.screen.fill((80, 80, 80))
        key = pg.key.get_pressed()

        # Рух танку
        for tank in self.tanks:
            direction = get_tank_direction(key, tank.number)
            tank.do_move(direction, self.all_sprites)

            # Механіка пострілу
            bullet = tank_shoot(tank, key, tank.number)
            if bullet:
                self.bullets.append(bullet)
                self.all_sprites.add(bullet)

            # Механіка руху кулі
            for index, bullet in enumerate(self.bullets):
                if bullet.do_move(self.bullets, self.all_sprites):
                    bullet.kill()
                    self.bullets.pop(index)

        self.all_sprites.draw(self.screen)


if __name__ == '__main__':
    game = Game()
    game.run()
