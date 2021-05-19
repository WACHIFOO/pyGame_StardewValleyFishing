import pygame


class Player:
    def __init__(self):
        self.max_abajo = 370
        self.max_arriba = 37
        self.gravity = 6
        self.force = 5
        self.player = pygame.image.load("sprites/player.png")
        self.player_rect = self.player.get_rect()
        self.player_rect.x = 380
        self.player_rect.y = 370

    def draw(self, screen):
        screen.blit(self.player, self.player_rect)

    def __check_limits(self):
        """
        Controlamos que no se pase del ux
        """
        if self.player_rect.y > self.max_abajo:
            self.player_rect.y = self.max_abajo
        elif self.player_rect.y < self.max_arriba:
            self.player_rect.y = self.max_arriba

    def movement(self, key_pressed):
        """
        Al pulsar espacio movemos el rectangulo y le aplicamos gravedad
        :param key_pressed: pygame.key.get_pressed()
        """
        if self.max_abajo >= self.player_rect.y >= self.max_arriba:
            if key_pressed[pygame.K_SPACE]:
                self.player_rect.y -= self.force
            else:
                # Le ponemos gravedad al rectangulo
                if self.player_rect.y < self.max_abajo:
                    self.player_rect.y += self.gravity
        self.__check_limits()
