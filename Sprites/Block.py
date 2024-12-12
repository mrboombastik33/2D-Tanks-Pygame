import pygame
from My_Project_OOP.Sprites.Sprite import Sprite
from My_Project_OOP.additional.settings import *

class Block(Sprite):
    def __init__(self, image_link, x, y, breakable):
        super().__init__(image_link, x, y)
        self.image = pygame.transform.scale_by(self.image, SCALING_BLOCKS)
        self.rect = self.rect.scale_by(SCALING_BLOCKS)
        self.breakable = breakable

    def __str__(self):
        return f"Block(type={self.block_type}, position=({self.rect.x}, {self.rect.y}))"







