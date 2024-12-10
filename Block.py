import pygame
from Sprite import Sprite

global scaling
scaling = 1.5


class Block(Sprite):
    def __init__(self, image_link, x, y, breakable):
        super().__init__(image_link, x, y)
        self.image = pygame.transform.scale_by(self.image, scaling)
        self.rect = self.rect.scale_by(scaling)
        self.breakable = breakable







