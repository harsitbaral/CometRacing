import pygame


class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        super().__init__()
        self.x = x
        self.y = y
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.angle = 0
        self.speed = 0

    def update(self, screen):
        self.rect.topleft = (int(self.x), int(self.y))
        rotated = pygame.transform.rotate(self.image, self.angle)
        surface_rect = self.image.get_rect(topleft=self.rect.topleft)
        new_rect = rotated.get_rect(center=surface_rect.center)
        screen.blit(rotated, new_rect.topleft)
