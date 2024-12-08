import pygame
from Sprite import Sprite
from Direction import Direction

WIDTH, HEIGHT = 500, 500

class Bullet(Sprite):
    def __init__(self, image_link, x, y, vector):
        super().__init__(image_link, x, y)
        self.image = pygame.transform.scale_by(self.image, 1.75)
        self.vector = vector
        self.set_rotation(vector[1])

    def do_move(self, bullets):
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

    def check_collision(self, sprite2):
        sprite2.kill()
        self.kill()















