import pygame


class Star(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("assets/star.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.y += 10
        self.rect = self.image.get_rect(center=(self.x, self.y))
        if self.y >= 1080:
            self.kill()