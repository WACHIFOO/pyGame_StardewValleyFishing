import pygame


class Player:
    def __init__(self):
        self.x = 380
        self.y = 370
        self.ancho = 30
        self.largo = 90
        self.max_abajo = 370
        self.max_arriba = 37
        self.gravity = 8
        self.force = 5

    def draw(self, screen):
        pygame.draw.rect(
            screen,
            (130, 229, 0),
            pygame.Rect(
                self.x,
                self.y,
                self.ancho,
                self.largo,
            )
        )

    def __check_limits(self):
        """
        Controlamos que no se pase del ux
        """
        if self.y > self.max_abajo:
            self.y = self.max_abajo
        elif self.y < self.max_arriba:
            self.y = self.max_arriba

    def movement(self, key_pressed):
        """
        Al pulsar espacio movemos el rectangulo y le aplicamos gravedad
        :param key_pressed: pygame.key.get_pressed()
        """
        if self.max_abajo >= self.y >= self.max_arriba:
            if key_pressed[pygame.K_SPACE]:
                self.y -= self.force
            else:
                # Le ponemos gravedad al rectangulo
                if self.y < self.max_abajo:
                    self.y += self.gravity
        self.__check_limits()
