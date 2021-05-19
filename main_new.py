from classes.game import Game
from classes.player import Player
from classes.sardina import Sardina
from classes.scoreUX import ScoreUX
import pygame

if __name__ == '__main__':
    game = Game()
    player = Player()
    sardina = Sardina()
    score = ScoreUX()
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

        # Controlamos si el jugador esta sobre la recompensa
        sardina.colision(player.player_rect)
        sardina.check_win()
        sardina.blit(game.screen)

        # Printamos la puntuacion
        score.draw(game.screen, sardina.puntuacion)

        # Finalizamos el latido
        game.end_hearthbeat()
    game.quit_game()
