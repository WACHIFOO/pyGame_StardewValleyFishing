import pygame


class ScoreUX:
    def __init__(self):
        self.x = 427
        self.y = 470
        self.ancho = 10
        self.largo = 0
        self.amarillo = 0
        self.rojo = 255

    def draw(self, screen, puntuacion):
        puntuacion_orig = puntuacion
        if puntuacion < 0:
            puntuacion = 0
        else:
            puntuacion = puntuacion * 4.35
        pygame.draw.rect(
            screen,
            self.color(puntuacion_orig),
            pygame.Rect(
                self.x,
                self.y - puntuacion,
                self.ancho,
                puntuacion,
            )
        )

    def color(self, puntuacion):
        """
        Segun la puntuacion cambiamos de naranja a verde
        0 = 255, 0, 0
        50% = 255, 255, 0
        100% = 0, 255, 0

        Wtf loco ni zorra como he sacado esto.
        """
        if puntuacion < 50:
            self.amarillo = self.amarillo - 10
        else:
            self.amarillo = self.amarillo + 10

        if self.amarillo > 255:
            self.rojo = self.rojo - 10
        else:
            self.rojo = self.rojo + 10

        if self.rojo > 255:
            self.rojo = 255
        elif self.rojo < 0:
            self.rojo = 0

        if self.amarillo > 255:
            self.amarillo = 255
        elif self.amarillo < 0:
            self.amarillo = 0

        return self.rojo, self.amarillo, 30
