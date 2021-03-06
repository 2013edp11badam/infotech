#!/usr/bin/env python

import itertools, pygame, math, sys

class Entity(object):
	id_iter = itertools.count(1)
	def __init__(self, image, pos=[0, 0]):
		self.entities = []

		self.id = self.id_iter.next()
		self.image = image
		self.pos = pos
		self.vel = 0
		self.angle = 0
		self.angle_vel = 0

		self.entities.append(self)

		print self.entities

	def rotate(self, angle):
		orig_rect = self.image.get_rect()
		rot_image = pygame.transform.rotate(self.image, angle)
		rot_rect = orig_rect.copy()
		rot_rect.center = rot_image.get_rect().center
		rot_image = rot_image.subsurface(rot_rect).copy()
		self.image = rot_image

		#rotated = pygame.transform.rotate(self.image, angle)
		#new_rect = self.image.get_rect().copy()
		#new_rect.center = self.pos
		#self.image = rotated

	def getImage(self): return self.image
	def getPos(self): return self.pos
	def getVel(self): return self.vel
	def getAngle(self): return self.angle
	def getAngleVel(self): return self.angle_vel

	def setImage(self, image): self.image = image
	def setPos(self, pos): self.pos = pos
	def setVel(self, vel): self.vel = vel
	def setAngle(self, angle): self.angle = angle
	def setAngleVel(self, angle_vel): self.angle_vel = angle_vel

class Spaceship(Entity):
	def __init__(self, image, pos=[0, 0]):
		Entity.__init__(self, image, pos)

	def shootBullet(self): pass

pygame.init()
screen = pygame.display.set_mode(pygame.display.list_modes()[10], pygame.DOUBLEBUF)
clock = pygame.time.Clock()

rocket = pygame.image.load('rocket.png')

spaceships = [Spaceship(rocket, [i, i]) for i in [100, 200, 300, 400]]

while True:
	for event in pygame.event.get():
		if event.type != pygame.QUIT:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					for spaceship in spaceships:
						spaceship.setAngleVel(2)
				elif event.key == pygame.K_RIGHT:
					for spaceship in spaceships:
						spaceship.setAngleVel(-2)
				elif event.key == pygame.K_UP:
					for spaceship in spaceships:
						spaceship.setVel(5)
				elif event.key == pygame.K_DOWN:
					for spaceship in spaceships:
						spaceship.setVel(-5)
			elif event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					for spaceship in spaceships:
						spaceship.setAngleVel(0)
				elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					for spaceship in spaceships:
						spaceship.setVel(0)			
		else:
			sys.exit()

	screen.fill((0, 0, 0))

	for spaceship in spaceships:	
		d = spaceship.getVel() * clock.tick()

		current_pos = spaceship.getPos()
		new_xpos = current_pos[0] + d * math.cos(math.radians(spaceship.getAngle() + 90))
		new_ypos = current_pos[1] - d * math.sin(math.radians(spaceship.getAngle() + 90))
		new_pos = (new_xpos, new_ypos)
		spaceship.setPos(new_pos)	

		spaceship.setAngle(spaceship.getAngle() + spaceship.getAngleVel())		
		spaceship.rotate(spaceship.getAngleVel())

		screen.blit(spaceship.getImage(), spaceship.getPos())
	
	pygame.display.flip()
	clock.tick(60)
