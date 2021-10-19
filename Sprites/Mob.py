import random
import pygame
from Settings.Settings import Settings
from Sprites.SpkSprite import SpkSprite

class Mob(SpkSprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(Settings.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(Settings.SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speedy = random.randrange(0, 8)
        self.speedx = random.randrange(-3, 3)


    def update(self):
        super().update()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > Settings.SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > Settings.SCREEN_WIDTH + 25:
            self.rect.x = random.randrange(Settings.SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(0, 8)

        #self.display_pos()




    def display_pos(self):

        font = pygame.font.Font(None, 17)
        text = font.render('%s %s' % (self.rect.x, self.rect.y), True, (255,
                                                                        255, 255), (159, 182, 205))
        textRect = text.get_rect()
        # Center the rectangle
        textRect.centerx = self.rect.x
        textRect.centery = self.rect.y
        # Blit the text
        Settings.SCREEN.blit(text, textRect)
        pygame.display.update()
