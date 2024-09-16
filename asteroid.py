from circleshape import CircleShape
from constants import *
import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 0)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            left_vector = self.velocity.rotate(random_angle)
            right_vector = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            left_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            right_asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            left_asteroid.velocity = left_vector * 1.2
            right_asteroid.velocity = right_vector * 1.2


