#!/usr/bin/python
import math

def padzeros(l):
	sqrt = int(math.sqrt(len(l)))
	p = []

	for row in range(sqrt + 2):
		if row == 0 or row == sqrt + 1:
			for x in range(sqrt + 2):
				p.append(0)
		else:
			p.append(0)
			for x in l[(sqrt * row) - sqrt:sqrt * row]:
				p.append(x)
			p.append(0)

	return p

def sumaround(l, i):
	sqrt = int(math.sqrt(len(l)))
	total = 0

	neighbours = [	i - 1, 	# left
					i - sqrt + 1, # top-left
					i - sqrt,	# top-center
					i - sqrt - 1, # top-right
					i + 1, 	# right
					i + sqrt + 1, # bottom-right
					i + sqrt,	# bottom-center
					i + sqrt - 1] # bottom-left

	for neighbour in neighbours:
		total += l[neighbour]
		print l[neighbour]

	return total
