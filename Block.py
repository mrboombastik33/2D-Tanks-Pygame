import pygame
from Sprite import Sprite


class Block(Sprite):
    def __init__(self, image_link, x, y):
        super().__init__(image_link, x, y)
        self.image = pygame.transform.scale_by(self.image, 1.5)

