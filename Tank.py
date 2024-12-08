import pygame
from Sprite import Sprite


class Tank(Sprite):
    def __init__(self, image_link, x, y, speed):
        super().__init__(image_link, x, y)
        self.speed = speed

    # def draw(self, window, angle):
    #     rotated_image = pygame.transform.rotate(self.image, self.angle)
    #     rect = rotated_image.get_rect(center = (self.rect.x, self.rect.y))
    #     window.blit(rotated_image, rect.topleft)











