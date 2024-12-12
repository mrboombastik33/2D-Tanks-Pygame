import pygame as pg
import sys
from Tank import Tank
from Direction import Direction
from Block import Block
from settings import *
from calling_functions import *
from Timer import Timer

class Game:
    def __init__(self, round_time, total_rounds):
        pg.init()
        pg.display.set_caption('Танки')
        # Ініціалізація гри
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.running = True
        self.current_round = 0
        self.round_time = round_time
        self.total_rounds = total_rounds
        self.game_timer = None

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
        tank = Tank(f'{SPRITE_IMAGES}/tank_blue.png', 100, 100, 2, 1, 3)
        tank2 = Tank(f'{SPRITE_IMAGES}/tank_red.png', 300, 300, 2, 2, 3)

        self.tanks.append(tank)
        self.all_sprites.add(tank)

        self.tanks.append(tank2)
        self.all_sprites.add(tank2)


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

    def start_round(self):
        self.current_round += 1
        self.game_timer = Timer(self.round_time)

        # Ресет об'єктів
        for tank in self.tanks:
            tank.reset()  # Ресетимо позицію танка

        for bullet in self.bullets:
            bullet.kill()
        self.bullets = []

        self.all_sprites = pg.sprite.Group(self.tanks + self.list_of_blocks)

    def run(self):
        while self.current_round < self.total_rounds:
            self.start_round()
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
            if event.type == pg.USEREVENT:
                if not self.game_timer.update_timer(pg.USEREVENT):  # Перевірка чи гра закінчилась
                    self.running = False  # Закінчення гри

    def update(self):
        self.screen.fill((80, 80, 80))
        key = pg.key.get_pressed()

        # Рух танку
        for tank in self.tanks:
            direction = get_tank_direction(key, tank.number)
            tank.do_move(direction, self.all_sprites)

            # Механіка пострілу
            bullet = tank_shoot(tank, key)
            if bullet:
                self.bullets.append(bullet)
                self.all_sprites.add(bullet)

            # Механіка руху кулі
            for index, bullet in enumerate(self.bullets):
                if bullet.do_move(self.bullets, self.all_sprites):
                    bullet.kill()
                    self.bullets.pop(index)

            if tank.health == 0:
                tank.kill()

        timer_surf = self.game_timer.render()
        self.all_sprites.draw(self.screen)
        self.screen.blit(timer_surf, (250, 60))
