import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS
)
from player import Player


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt: int = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Main Game Loop
    while True:
        pygame.event.pump()
        screen.fill((0, 0, 0))

        player.update(dt)
        player.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
