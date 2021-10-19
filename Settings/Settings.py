import pygame
from os import path
class Settings:

    IMG_DIR = path.join(path.dirname(__file__), '../ressources/img')
    PLAYER_IMG = pygame.image.load(path.join(IMG_DIR, "player.png"))
    ALL_SPRITES = pygame.sprite.Group()
    MOBS = pygame.sprite.Group()
    BULLETS = pygame.sprite.Group()
    SCREEN_WIDTH = 480
    SCREEN_HEIGHT = 600
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    FPS = 60

    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)

