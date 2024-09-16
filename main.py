# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from player import Player, Shot
from constants import *
from asteroidfield import AsteroidField
from asteroid import Asteroid

def main():
	print("Starting asteroids!")
	print("Screen width:", SCREEN_WIDTH)
	print("Screen height:", SCREEN_HEIGHT)
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	clock = pygame.time.Clock()
	dt = 0
	x = SCREEN_WIDTH / 2
	y = SCREEN_HEIGHT / 2
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	shots = pygame.sprite.Group()
	Player.containers = (updatable, drawable)
	Asteroid.containers = (updatable, drawable, asteroids)
	Shot.containers = (updatable, drawable, shots)
	AsteroidField.containers = (updatable)
	player = Player(x, y)
	asteroidfield = AsteroidField()

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0, 0, 0))
		dt = clock.tick(60) / 1000
		for sprite in updatable:
			sprite.update(dt)
		for rock in asteroids:
			if rock.collision(player):
				print("Game Over!")
				sys.exit()
			for shot in shots:
				if shot.collision(rock):
					shot.kill()
					rock.split()
		for sprite in drawable:
			sprite.draw(screen)
		pygame.display.flip()

if __name__ == "__main__":
    main()
