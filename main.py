import pygame

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption("Juego de pesca")
    playing = True
    clock = pygame.time.Clock()

    rectangulo = {
        "X": 380,
        "Y": 370,
        "ancho": 30,
        "largo": 90,
    }
    # Cargamos el fondo de pantalla
    background = pygame.image.load("sprites/background.png")
    ux = pygame.image.load("sprites/fishing_UX2.png")
    pescado = pygame.image.load("sprites/Sardine.png")

    max_abajo = 370
    max_arriba = 37
    # Creamos lista de sprites
    all_sprites = pygame.sprite.Group()

    pygame.display.flip()
    while playing:

        for event in pygame.event.get():
            playing = not (event.type == pygame.QUIT)
            # if event.type == pygame.QUIT:
            # playing = False

        # Printamos la pantalla de negro
        # screen.fill(0)
        screen.blit(background, background.get_rect())
        ux_rect = ux.get_rect()
        ux_rect.x = 300
        ux_rect.y = 15
        screen.blit(ux, ux_rect)

        pressed = pygame.key.get_pressed()
        print(str(rectangulo["Y"]) + "-" + str(max_abajo >= rectangulo["Y"] >= max_arriba))
        if max_abajo >= rectangulo["Y"] >= max_arriba:
            if pressed[pygame.K_SPACE]:
                rectangulo["Y"] -= 5
            else:
                # Le ponemos gravedad al rectangulo
                if rectangulo["Y"] < max_abajo:
                    rectangulo["Y"] += 8

        # Controlamos que no se pase
        if rectangulo["Y"] > max_abajo:
            rectangulo["Y"] = max_abajo
        elif rectangulo["Y"] < max_arriba:
            rectangulo["Y"] = max_arriba

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
