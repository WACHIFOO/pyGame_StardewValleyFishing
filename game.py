import pygame


class Game:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.playing = True
        self.screen = pygame.display.set_mode((500, 500))

    def flip(self):
        """
        No se que es pero hay que hacer flip xD
        """
        pygame.display.flip()

    def __tick(self):
        """
        Configuramos los fps del juego a 60
        """
        self.clock.tick(60)

    def start_hearthbeat(self):
        """
        Al empezar el bucle limpiamos la pantalla y demás
        """
        self.screen.fill(0)

    def end_hearthbeat(self):
        """
        Despues de cada vuelta al bucle "Latido" hacemos flip y tick
        """
        self.flip()
        self.__tick()

    def trigger_quit_game(self):
        """
        Miramos si se ha pulsado salir del juego
        """
        for event in pygame.event.get():
            self.playing = not (event.type == pygame.QUIT)

    def quit_game(self):
        """
        Quitamos el juego
        """
        pygame.quit()
