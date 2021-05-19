import pygame

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Juego de pesca")
    playing = True
    clock = pygame.time.Clock()

    rectangulo = {
        "X": 200,
        "Y": 408,
        "ancho": 30,
        "largo": 90,
    }

    pygame.display.flip()
    while playing:
        screen.fill(0)

        for event in pygame.event.get():
            playing = not (event.type == pygame.QUIT)
            # if event.type == pygame.QUIT:
            # playing = False

        pressed = pygame.key.get_pressed()

        print(str(rectangulo["Y"]) + "-" + str(408 >= rectangulo["Y"] >= 100))
        if 408 >= rectangulo["Y"] >= 100:
            if pressed[pygame.K_SPACE]:
                rectangulo["Y"] -= 5
            else:
                # Le ponemos gravedad al rectangulo
                if rectangulo["Y"] < 408:
                    rectangulo["Y"] += 8

        # Controlamos que no se pase
        if rectangulo["Y"] > 408:
            rectangulo["Y"] = 408
        elif rectangulo["Y"] < 100:
            rectangulo["Y"] = 100

        # Limpiamos la pantalla pintandola de negro. Esto habría que cambiarlo segun el fondo
        # Printamos el rectangulo
        pygame.draw.rect(
            screen,
            (255, 128, 255),
            pygame.Rect(
                rectangulo["X"],
                rectangulo["Y"],
                rectangulo["ancho"],
                rectangulo["largo"]
            )
        )

        ######################################
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# http://programarcadegames.com/python_examples/show_file.php?file=game_class_example.py
