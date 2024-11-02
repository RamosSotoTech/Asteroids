# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys

import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

drawable = pygame.sprite.Group()
updatable = pygame.sprite.Group()
asteroids = pygame.sprite.Group()
shots = pygame.sprite.Group()


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    Player.containers = drawable, updatable
    Asteroid.containers = drawable, updatable, asteroids
    AsteroidField.containers = updatable
    Shot.containers = drawable, updatable, shots

    asteroid_field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for sprite in updatable:
            sprite.update(dt)

        for sprite in asteroids:
            if sprite.collides_with(player):
                print("Game Over!")
                sys.exit()
            for shot in shots:
                if sprite.collides_with(shot):
                    sprite.split()
                    shot.kill()
                    break

        screen.fill("black")

        for sprite in drawable:
            sprite.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000.0


if __name__ == "__main__":
    main()
