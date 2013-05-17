#!/usr/bin/env python

import pygame, sys

pygame.init()

screen = pygame.display.set_mode((640, 480), pygame.DOUBLEBUF)
pygame.display.set_caption('Background Test')
clock = pygame.time.Clock()

image_bg = pygame.image.load('bg.png')

screen.blit(image_bg, (0, 0))

x = 100

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x -= 10
			elif event.key == pygame.K_RIGHT:
				x += 10

	screen.blit(image_bg, (0, 0))
	
	font = pygame.font.Font(None, 28)
	text = font.render("-" * 20, 1, (0, 0, 0))
	screen.blit(text, (x, 100))

	pygame.display.flip()
	clock.tick(60)

sys.exit()
