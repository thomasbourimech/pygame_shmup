import pygame
from Settings.Settings import Settings
from Sprites.SpkSprite import SpkSprite

class Bullet(SpkSprite):


    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 20))
        self.image.fill(Settings.YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        super().update()
        self.rect.y += self.speedy

        if self.rect.bottom < 0:
            self.kill()