#!/usr/bin/env python

class Chair():
	def __init__(self, location):
		self.location = location

	def getLocation(self):
		return self.location

	def setLocation(self, new_location):
		self.location = new_location

chair1 = Chair((0, 1))
chair2 = Chair((0, 4))

for x in range(10):
	for y in range(10):
		if chair1.getLocation() == (y, x):
			print 'X',
		else:
			print 'O',
	print ''
