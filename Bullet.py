import pygame
from Sprite import Sprite
from Direction import Direction
from Block import Block

WIDTH, HEIGHT = 500, 500

class Bullet(Sprite):
    def __init__(self, image_link, x, y, vector, shooter):
        super().__init__(image_link, x, y)
        self.image = pygame.transform.scale_by(self.image, 1.75)
        self.vector = vector
        self.set_rotation(vector[1])
        self.shooter = shooter

    def do_move(self, bullets, group):
        self.check_collision(group)

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
        for obj in group:
            if obj is not self and not self.rect.colliderect(self.shooter) and self.rect.colliderect(obj.rect):
                if isinstance(obj, Block) and obj.breakable == 0:
                    obj.kill()
                self.kill()
                break















