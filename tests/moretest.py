#!/usr/bin/env python
from fltk import *

class MyBox(Fl_Box):
	def __init__(self, x, y, w, h):
		Fl_Box.__init__(self, x, y, w, h)
		self.box(FL_FLAT_BOX)

	def handle(self, event):
		if event == FL_ENTER:
			self.color(FL_BLUE)
			self.redraw()
			return 1
		else:
			return 0

class MyWindow(Fl_Window):
	def __init__(self, w, h, label=None):
		Fl_Window.__init__(self, w, h, label)
		self.begin()
		self.butarray=[]
		for y in range(0, 100):
			for x in range(0, 100):
				self.butarray.append(MyBox(x * 6, y * 6, 6, 6))
		self.end()

app = MyWindow(600, 600, "Paint")
app.show()
Fl.run()
