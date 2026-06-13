import pygame


def main():
    pygame.init()

    screen = pygame.display.set_mode((1200, 1000))
    pygame.display.set_caption("Dijkstra's Game")

    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill("white")

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()