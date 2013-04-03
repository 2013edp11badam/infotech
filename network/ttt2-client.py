#!/usr/bin/env python

from fltk import *

class TicTacToe(Fl_Window):
	def __init__(self):
		Fl_Window.__init__(self, 100, 100, 310, 310, 'Tic Tac Toe')

		self.begin()
		self.dict_buttons = {}
		for y in xrange(3):
			for x in xrange(3):
				self.dict_buttons{num: (Fl_Button(x * 100 + 5, y * 100 + 5, 100, 100, str(x, y)))}
		self.end()

ttt = TicTacToe()a
Fl.run()
