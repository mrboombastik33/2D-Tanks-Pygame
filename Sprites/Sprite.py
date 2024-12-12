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
        self.__rotation = 0

    # Малювання об'єкту у вікні
    def draw(self, window: pygame.Surface):
        window.blit(self.image, self.rect)

    # Отримання поточної позиції
    def get_pos(self):
        return self.rect.x, self.rect.y

    # встановлення позиції
    def set_pos(self, x, y):
        self.rect.x = x
        self.rect.y = y

    # Встановлення нової позиції через метод set_pos
    def move(self, x, y):
        self.set_pos(self.rect.x + x, self.rect.y + y)

    # Перевірка колізії
    def check_collision(self, sprite2):
        return self.rect.colliderect(sprite2.rect)

    # повороти
    def rotate(self, angle):
        self.__rotation += angle # Змінюємо значення атрибуту rotation на значення кута
        self.image = pygame.transform.rotate(self.image, angle)

    def set_rotation(self, angle):
        self.image = pygame.transform.rotate(self.image, angle - self.__rotation) # Зміна поточного напрямку
        self.__rotation = angle


