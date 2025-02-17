from Sprites.Bullet import Bullet
from Sprites.Sprite import Sprite
from additional import Direction
from additional.settings import *


class Tank(Sprite):
    def __init__(self, image_link, x, y, speed, number, health):
        super().__init__(image_link, x, y)
        self.__speed = speed
        self.direction = Direction.DOWN.value
        self.number = number
        self.last_fire_time = 0
        self.__health = health
        self.starting_rect = self.rect.copy()

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
                self.rect = old_rect
                return

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

