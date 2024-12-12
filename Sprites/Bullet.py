import pygame
from My_Project_OOP.Sprites.Sprite import Sprite
from My_Project_OOP.Sprites import Block
from My_Project_OOP.additional.Direction import Direction
from My_Project_OOP.additional.settings import *

class Bullet(Sprite):
    def __init__(self, image_link, x, y, vector, shooter):
        super().__init__(image_link, x, y)
        self.__image = pygame.transform.scale_by(self.image, SCALING_BULLET)
        self.vector = vector
        self.set_rotation(vector[1])
        self.__shooter = shooter

    def do_move(self, bullets, group):
        if self.check_collision(group):
            return True

        if self.vector[1] == Direction.RIGHT.value and self.rect.x < WIDTH:
            self.move(self.vector[0], 0)
        elif self.vector[1] == Direction.LEFT.value and self.rect.x > 0:
            self.move(-self.vector[0], 0)
        elif self.vector[1] == Direction.UP.value and self.rect.y > 0:
            self.move(0, -self.vector[0])
        elif self.vector[1] == Direction.DOWN.value and self.rect.y < HEIGHT:
            self.move(0, self.vector[0])
        else:
            bullets.pop(bullets.index(self))
            self.kill()

    def check_collision(self, group):
        from My_Project_OOP.Sprites.Tank import Tank
        for obj in group:
            if obj is not self and not self.rect.colliderect(self.__shooter) and self.rect.colliderect(obj.rect):
                if isinstance(obj, Block) and obj.breakable == 0:
                    obj.kill()
                if isinstance(obj, Tank) and obj.get_health() >= 0:
                    obj.receive_damage()
                return True


