#!/usr/bin/env python

import pygame, sys, math

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image

pygame.init()
size = pygame.display.list_modes()[6]
screen = pygame.display.set_mode(size, pygame.DOUBLEBUF)
pygame.display.set_caption('My Game')
clock = pygame.time.Clock()
font = pygame.font.Font(None, 28)

rocket = pygame.image.load('rocket.png')

x, y = 100, 100
v = 0
a = 0
a_v = 0

b_x, b_y = 100, 100
b_v = 0
b_a = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.MOUSEMOTION:
			if event.buttons[0] == 1:
				x, y = event.pos[0] - 65, event.pos[1] - 50
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				a_v = 2
			elif event.key == pygame.K_RIGHT:
				a_v = -2
			elif event.key == pygame.K_UP:			
				v = 2
			elif event.key == pygame.K_SPACE:
				b_x, b_y = x, y
				b_v = 40
				b_a = a
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				a_v = 0
			elif event.key == pygame.K_UP:
				v = 0
	
	screen.fill((0, 0, 0))

	d = v * clock.tick()
	x += d * math.cos(math.radians(a + 90))
	y -= d * math.sin(math.radians(a + 90))
	a += a_v

	b_d = b_v * clock.tick()
	b_x += b_d * math.cos(math.radians(b_a + 90))
	b_y -= b_d * math.sin(math.radians(b_a + 90))

	if x > size[0] or x < 0:
		x = 0

	if y > size[1] or y < 0:
		y = 0

	rotrocket = pygame.transform.rotate(rocket, a)
	screen.blit(rotrocket, (x, y))

	pygame.display.flip()
	clock.tick(60)
