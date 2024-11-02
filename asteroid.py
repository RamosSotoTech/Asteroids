import pygame
import circleshape
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius=radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(random_angle)
        velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1 * 1.2
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2 * 1.2
