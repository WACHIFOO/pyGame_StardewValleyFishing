import pygame


class Background:
    def __init__(self):
        self.background = pygame.image.load("sprites/background.png")
        self.ux = pygame.image.load("sprites/fishing_UX2.png")
        self.ux_rect = self.ux.get_rect()
        self.ux_rect.x = 300
        self.ux_rect.y = 15

    def blit(self, screen):
        screen.blit(self.background, self.background.get_rect())
        screen.blit(self.ux, self.ux_rect)
