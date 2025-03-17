from sys import exit
import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    ASTEROID_MIN_RADIUS,
    ASTEROID_KINDS,
    ASTEROID_SPAWN_RATE,
    ASTEROID_MAX_RADIUS
)
from shot import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    # Clock for FPS-locked updates
    clock = pygame.time.Clock()
    dt: int = 0

    # Groups for entity organization
    updateables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    Player.containers = (updateables, drawables)
    Asteroid.containers = (asteroids, updateables, drawables)
    AsteroidField.containers = (updateables)
    Shot.containers = (bullets, updateables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Main Game Loop
    while True:
        # Update entities
        pygame.event.pump()
        updateables.update(dt)

        # Detect collisions
        for asteroid in asteroids:
            for bullet in bullets:
                if not asteroid.collides(bullet):
                    continue
                asteroid.split()
                bullet.kill()

            if not asteroid.collides(player):
                continue
            print("Game over!")
            exit(0)

        # Draw
        screen.fill((0, 0, 0))
        for drawable in drawables:
            drawable.draw(screen)

        # Update display
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
