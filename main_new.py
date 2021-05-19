from classes.game import Game
from classes.player import Player
import pygame

if __name__ == '__main__':
    game = Game()
    player = Player()
    game.flip()
    while game.playing:
        # Controlamos si se pulsa cerrar
        game.trigger_quit_game()

        # Iniciamos el latido
        game.start_hearthbeat()

        # Obtenemos la tecla pulsada y movemos el jugador
        pressed = pygame.key.get_pressed()
        player.movement(pressed)

        # Renderizamos el jugador
        player.draw(game.screen)

        # Finalizamos el latido
        game.end_hearthbeat()
    game.quit_game()
