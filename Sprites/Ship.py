import pygame
from Sprites.SpkSprite import SpkSprite
from Sprites.Bullet import Bullet
from Settings.Settings import Settings

class Ship(SpkSprite):

    def __init__(self, COLOR, moving_speed):
        super().__init__()
        self.moving_speed = moving_speed
        #self.image = pygame.Surface((50, 40))
        #self.image.fill(COLOR)
        self.image = Settings.PLAYER_IMG.convert()
        self.image = pygame.transform.scale(self.image, (40,50))
        self.image.set_colorkey(Settings.BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = Settings.SCREEN_WIDTH / 2
        self.rect.bottom = Settings.SCREEN_HEIGHT - 10
        self.speedx = 0

    def update(self):
        super().update()
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -self.moving_speed
        if keystate[pygame.K_RIGHT]:
            self.speedx = self.moving_speed
        self.rect.x += self.speedx
        if self.rect.right > Settings.SCREEN_WIDTH:
            self.rect.right = Settings.SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

    def shoot(self):
        self.bullet = Bullet(self.rect.centerx, self.rect.top)
        Settings.ALL_SPRITES.add(self.bullet)
        Settings.BULLETS.add(self.bullet)
