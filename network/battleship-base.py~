#!/usr/bin/env python

from fltk import *
import string

class Battleship(Fl_Window):
	def __init__(self, x, y, w, h, label):
		Fl_Window.__init__(self, x, y, w, h, label)

		# define colors
		self.COLOR_NONE = FL_GRAY
		self.COLOR_SHIP = fl_rgb_color(150, 150, 150)
		self.COLOR_HIT = fl_rgb_color(200, 20, 20)
		self.COLOR_MISS = fl_rgb_color(230, 230, 230)

		self.begin()
		self.buttons = []
		for y in range(10):
			for x in range(10):
					self.buttons.append(Fl_Button(x * (w / 10), y * (h / 10), w / 10, h / 10))
					self.buttons[-1].callback(self.button_pressed)
					self.buttons[-1].box(FL_THIN_UP_BOX)
					self.buttons[-1].labelsize(h / 42)
		self.end()

	def button_pressed(self, w_id):
			w_id.label('HIT')
			w_id.labelcolor(self.COLOR_HIT)

	def modify_board(self, arg):
		for button in board:
			if arg == 1:
				button.activate()
			else:
				button.deactivate()

bs = Battleship(100, 100, 600, 600, 'Battleship')
bs.show()
Fl.run()
