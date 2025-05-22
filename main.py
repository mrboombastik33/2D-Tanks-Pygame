import pygame as pg
from Sprites.Tank import Tank
from Sprites.Block import Block
from additional.settings import *
from Timer import Timer
from additional import Direction

class Game:
    def __init__(self, round_time, total_rounds):
        # Ініціалізація гри
        pg.init()
        pg.display.set_caption('Танки')
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        self.clock = pg.time.Clock()
        self.__running = True
        self.current_round = 0
        self.__round_time = round_time
        self.total_rounds = total_rounds
        self.game_timer = None

        # Групи та списки для об'єктів
        self.all_sprites = pg.sprite.Group()
        self.tanks = []
        self.bullets = []
        self.list_of_blocks = []
        self.winners = []

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
        # Створення спрайтів та додавання їх в групи
        self.list_of_blocks = []
        self.create_map_blocks()

        tank1 = Tank(f'{SPRITE_IMAGES}/tank_blue.png', 90, 100, 2, 1, 3, Direction.DOWN.value)
        tank2 = Tank(f'{SPRITE_IMAGES}/tank_red.png', 600, 500, 2, 2, 3, Direction.UP.value)

        self.tanks = [tank1, tank2]
        self.all_sprites.add(tank1)
        self.all_sprites.add(tank2)


    def __create_boundary(self): # Створення границі мапи (алгоритм)
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                if i == 0 or i == 9 or j == 0 or j == 9:
                    self.map[i][j] = 1

    def create_map_blocks(self): # Заповнення мапи
        self.__create_boundary()
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

    def start_round(self): #Початок нового раунда
        self.current_round += 1

        self.init_objects()

        self.game_timer = Timer(self.__round_time)

        self.__running = True

        # Об'єднюємо всі спрайти в групу
        self.all_sprites = pg.sprite.Group(self.tanks + self.list_of_blocks)

    def run(self):
        while self.current_round < self.total_rounds:
            self.start_round()
            while self.__running:
                self.clock.tick(FPS)
                self.handle_events()
                self.update()
                pg.display.update()

        pg.quit()
        return self.winners

    def handle_events(self): #
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.__running = False
            if event.type == pg.USEREVENT:
                if not self.game_timer.update_timer(pg.USEREVENT):  # Перевірка таймера
                    self.winners.append(0)
                    self.reset_game()


    def reset_game(self):
        self.tanks.clear()
        self.bullets.clear()
        self.list_of_blocks.clear()
        self.__running = False

    def update(self):
        self.screen.fill((80, 80, 80))
        key = pg.key.get_pressed()

        # Рух танку
        for tank in self.tanks:
            direction = tank.get_direction(key)
            tank.do_move(direction, self.all_sprites)

            # Механіка пострілу
            bullet = tank.shoot(key)
            if bullet:
                self.bullets.append(bullet)
                self.all_sprites.add(bullet)

            # Механіка руху кулі
            for index, bullet in enumerate(self.bullets):
                if bullet.do_move(self.bullets, self.all_sprites):
                    bullet.kill()
                    self.bullets.pop(index)

            # Видалити об'єкт якщо здоров'я танка дорівнює нулю
            if tank.get_health() == 0:
                self.tanks.pop(self.tanks.index(tank))
                self.winners.append(self.tanks[0].get_number())
                self.reset_game()


        timer_surf = self.game_timer.render()
        self.all_sprites.draw(self.screen)
        self.screen.blit(timer_surf, (250, 60))

    def get_round_time(self):
        return self.__round_time

