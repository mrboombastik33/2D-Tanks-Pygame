import pygame
from Sprites.Sprite import Sprite
from additional.settings import *


#Цей клас описує основні атрибути, які має блок (включно з тим чи може він бути знищений)
class Block(Sprite):
    def __init__(self, image_link, x, y, breakable):
        super().__init__(image_link, x, y)
        self.image = pygame.transform.scale_by(self.image, SCALING_BLOCKS)
        self.rect = self.rect.scale_by(SCALING_BLOCKS)
        self.breakable = breakable







