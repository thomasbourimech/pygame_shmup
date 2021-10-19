import pygame
from Sprites.Ship import Ship
from Sprites.Mob import Mob
from Settings.Settings import Settings


class Controller:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Shmup")
        self.clock = pygame.time.Clock()

    def handle_sprites(self):

        self.player = Ship(Settings.GREEN, moving_speed=8)
        Settings.ALL_SPRITES.add(self.player)

        for i in range(30):
            m = Mob()
            Settings.ALL_SPRITES.add(m)
            Settings.MOBS.add(m)

    def sprites_update(self):

        Settings.ALL_SPRITES.update()
        hits = pygame.sprite.groupcollide(Settings.MOBS, Settings.BULLETS, True, True)
        for hit in hits:
            m = Mob()
            Settings.ALL_SPRITES.add(m)
            Settings.MOBS.add(m)

        hits = pygame.sprite.spritecollide(self.player, Settings.MOBS, False)
        if hits:
            self.running = False

    def run_game(self):

        self.running = True

        while self.running:
            self.clock.tick(Settings.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()

            self.sprites_update()

            Settings.SCREEN.fill(Settings.BLUE)
            Settings.ALL_SPRITES.draw(Settings.SCREEN)

            pygame.display.flip()

        pygame.quit()