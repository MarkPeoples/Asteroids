from circleshape import CircleShape
from constants import *
import pygame

class Player(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shot_timer = 0
		
	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)

	def rotate(self, dt):
		self.rotation += PLAYER_TURN_SPEED * dt

	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def update(self, dt):
		self.shot_timer += dt
		keys = pygame.key.get_pressed()

		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_SPACE]:
			self.shoot()

	def triangle(self):
			forward = pygame.Vector2(0, 1).rotate(self.rotation)
			right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
			a = self.position + forward * self.radius
			b = self.position - forward * self.radius - right
			c = self.position - forward * self.radius + right
			return [a, b, c]
	
	def shoot(self):
		if self.shot_timer >= PLAYER_SHOT_COOLDOWN:
			shot = Shot(self.position.x, self.position.y)
			velocity = pygame.Vector2(0, 1)
			velocity = velocity.rotate(self.rotation)
			velocity *= PLAYER_SHOOT_SPEED
			shot.velocity = velocity
			self.shot_timer = 0
		

class Shot(CircleShape):
	def __init__(self, x, y):
		super().__init__(x, y, SHOT_RADIUS)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", self.position, self.radius, 2)

	def update(self, dt):
		self.position += self.velocity * dt