import pygame
from My_Project_OOP.Bullet import Bullet
from Sprite import Sprite
from Direction import Direction

class Tank(Sprite):
    def __init__(self, image_link, x, y, speed):
        super().__init__(image_link, x, y)
        self.speed = speed
        self.direction = Direction.DOWN.value

    def set_rotation(self, direction):
        self.direction = direction
        super().set_rotation(self.direction)

    def fire(self, image_link):
        bullet_offsets = {
            Direction.UP.value: (self.rect.center[0], self.rect.top),  # Top-center
            Direction.DOWN.value: (self.rect.center[0], self.rect.bottom),  # Bottom-center
            Direction.LEFT.value: (self.rect.left, self.rect.center[1]),  # Middle-left
            Direction.RIGHT.value: (self.rect.right, self.rect.center[1]),  # Middle-right
        }
        # Отримати координати пулі в залежності від її поточного місцезнаходження
        bullet_coord = bullet_offsets[self.direction]

        bullet = Bullet(image_link, bullet_coord[0], bullet_coord[1], (3, self.direction))
        return bullet




























