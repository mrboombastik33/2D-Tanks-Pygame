import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, image_link, x, y):
        super().__init__()
        self.image = pygame.image.load(image_link)
        self.image = pygame.transform.scale_by(self.image, 1)
        self.rect = self.image.get_rect()
        self.size = self.image.get_size()
        self.rect.x = x
        self.rect.y = y
        self.direction = 0

    def draw(self, window):
        window.blit(self.image, self.rect)

    def get_pos(self):
        return self.rect.x, self.rect.y

    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move(self, x, y):
        self.set_pos(self.rect.x + x, self.rect.y + y)

    def check_collision(self, sprite2):
        return sprite2.rect.colliderect(self.rect)

    def rotate(self, angle):
        self.image = pygame.transform.rotate(self.image, angle)

    def set_rotation(self, value):
        self.direction = value
























