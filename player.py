import circleshape
import pygame
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN
from shot import Shot


class Player(circleshape.CircleShape):
    def __init__(self, x, y, radius=PLAYER_RADIUS):
        super().__init__(x, y, radius=radius)
        self.rotation = 0
        self.timer = 0
        self.health = 3

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), width=2)

    def rotate(self, dt):
        self.rotation += dt * PLAYER_TURN_SPEED

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.timer -= dt

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer > 0:
            return None
        self.timer = PLAYER_SHOOT_COOLDOWN
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        return shot

    def hit(self):
        self.health -= 1
        if self.health == 0:
            self.kill()
        return self.health