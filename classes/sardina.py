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
        """
        Mostramos por pantalla la sardina
        """
        screen.blit(self.sardina, self.sardina_rect)

    def colision(self, player):
        """
        Controlamos la colision contra el jugador
        """
        if self.sardina_rect.colliderect(player):
            self.puntuacion += 1
        else:
            if self.puntuacion > 0:
                self.puntuacion -= 1
            else:
                self.puntuacion = 0

    def check_win(self):
        """
        Cuando llegue a 100 reiniciamos la puntacion y cambiamos de sitio
        """
        if self.puntuacion >= 100:
            self.puntuacion = 0
            self.random_position()

    def random_position(self):
        """
        Cambiamos de sitio de manera random en el eje vertical
        """
        self.sardina_rect.y = random.randint(self.max_arriba, self.max_abajo)
