#!/usr/bin/env python

import pygame, sys, math, itertools

class Spaceship():
	id_iter = itertools.count(1)
	def __init__(self, screen, image, pos=[0, 0]):
		self.id = self.id_iter.next()
		self.screen = screen
		self.image = image
		self.pos = pos
		self.vel = 0
		self.angle = 0
		self.angle_velocity = 0

	def rotate(self, angle):
		orig_rect = self.image.get_rect()
		rot_image = pygame.transform.rotate(self.image, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		self.image = rot_image

pygame.init()
screen = pygame.display.set_mode(pygame.display.list_modes()[6], pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rocket = pygame.image.load('rocket.png')

spaceships = [Spaceship(screen, rocket, (i, 100)) for i in [100, 200]]

while True:
	for event in pygame.event.get():
		if event.type != pygame.QUIT:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					for spaceship in spaceships:
						spaceship.rotate(20)
				elif event.key == pygame.K_RIGHT:
					for spaceship in spaceships:
						spaceship.rotate(-20)
				elif event.key == pygame.K_UP:
					pass
				elif event.key == pygame.K_DOWN:
					pass
			elif event.type == pygame.KEYUP:
				pass			
		else:
			sys.exit()

		screen.fill((0, 0, 0))

		for spaceship in spaceships:
			screen.blit(spaceship.image, spaceship.pos)
	
		pygame.display.flip()
		clock.tick(60)
