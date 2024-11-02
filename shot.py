import pygame
import circleshape
from constants import SHOT_RADIUS


class Shot(circleshape.CircleShape):
    def __init__(self, x, y, radius = SHOT_RADIUS):
        super().__init__(x, y, radius=radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "gray", self.position, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt
