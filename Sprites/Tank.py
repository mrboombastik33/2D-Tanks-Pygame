from Sprites.Bullet import Bullet
from Sprites.Sprite import Sprite
from additional import Direction
from additional.settings import *
import pygame as pg

class Tank(Sprite):
    def __init__(self, image_link, x, y, speed, number, health, direction):
        super().__init__(image_link, x, y)
        self.__speed = speed
        self.direction = direction
        self.number = number
        self.last_fire_time = 0
        self.__health = health
        self.starting_rect = self.rect.copy()

        self.set_rotation(self.direction)


    def set_rotation(self, direction):
        self.direction = direction
        super().set_rotation(self.direction)

    def do_move(self, direction, group):
        # Логіка руху танка
        old_rect = self.rect.copy()

        if direction == Direction.RIGHT:
            self.move(self.__speed, 0)
            self.set_rotation(90)

        if direction == Direction.LEFT:
            self.move(-self.__speed, 0)
            self.set_rotation(-90)

        if direction == Direction.UP:
            self.move(0, -self.__speed)
            self.set_rotation(180)

        if direction == Direction.DOWN:
            self.move(0, self.__speed)
            self.set_rotation(0)

        for obj in group:
            if obj is not self and self.check_collision(obj):
                if isinstance(obj, Bullet) and obj.shooter != self:
                    self.__health -= 1
                self.rect = old_rect
                return

    def get_direction(self, key):
        tank1, tank2 = load_controls(JSON_FILE)
        tank_controls = tank1 if self.number == 1 else tank2
        direction = 0

        if key[tank_controls["KEY_UP"]]:
            direction = Direction.UP
        elif key[tank_controls["KEY_DOWN"]]:
            direction = Direction.DOWN
        elif key[tank_controls["KEY_LEFT"]]:
            direction = Direction.LEFT
        elif key[tank_controls["KEY_RIGHT"]]:
            direction = Direction.RIGHT
        return direction

    def shoot(self, key):
        current_time = pg.time.get_ticks()

        shooter1, shooter2 = load_controls(JSON_FILE)
        tank_controls = shooter1 if self.number == 1 else shooter2

        if key[tank_controls["SHOOT"]] and current_time - self.last_fire_time >= FIRE_INTERVAL:
            self.last_fire_time = current_time
            bullet = self.fire(f'{SPRITE_IMAGES}/bulletBlue1.png') if self.number == 1 else self.fire(
                f'{SPRITE_IMAGES}/bulletRed1.png')
            return bullet
        return None

    def fire(self, image_link):
        bullet_offsets = {
            Direction.UP.value: (self.rect.center[0], self.rect.top),  # Top-center
            Direction.DOWN.value: (self.rect.center[0], self.rect.bottom),  # Bottom-center
            Direction.LEFT.value: (self.rect.left, self.rect.center[1]),  # Middle-left
            Direction.RIGHT.value: (self.rect.right, self.rect.center[1]),  # Middle-right
        }
        # Отримати координати пулі в залежності від її поточного місцезнаходження
        bullet_coord = bullet_offsets[self.direction]

        bullet = Bullet(image_link, bullet_coord[0], bullet_coord[1], (3, self.direction), self)
        return bullet

    def receive_damage(self):
        self.__health -= 1

    def get_health(self):
        return self.__health

    def get_speed(self):
        return self.__speed

    def get_number(self):
        return self.number


    def __str__(self):
        return f'Танк отримав пошкодження. Залишилось 3 здоровя'

