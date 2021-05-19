import pygame
import random


class Sardina:
    def __init__(self):
        self.sardina = pygame.image.load("sprites/Sardine.png")
        self.sardina_rect = self.sardina.get_rect()
        self.max_abajo = 370
        self.max_arriba = 37
        self.sardina_rect.x = 370
        self.sardina_rect.y = random.randint(self.max_arriba, self.max_abajo)
        self.puntuacion = 0

    def blit(self, screen):
        screen.blit(self.sardina, self.sardina_rect)

    def colision(self, player):
        if self.sardina_rect.colliderect(player):
            self.puntuacion += 1
        else:
            self.puntuacion -= 1

    def check_win(self):
        if self.puntuacion >= 100:
            self.puntuacion = 0
            self.random_position()

        # def start(self):
        #     self.check_win()
        #     self.colision()
        """
        check_win()
        colision()
        """
        pass

    def random_position(self):
        self.sardina_rect.y = random.randint(self.max_arriba, self.max_abajo)
