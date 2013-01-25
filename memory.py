#!/usr/bin/python
import random, time
from fltk import *

def go(widget):
	widget.labeltype(FL_NORMAL_LABEL)

	visible = []

	for x in range(len(button_array)):
		if button_array[x].labeltype() == FL_NORMAL_LABEL:
			visible.append(x)

		if len(visible) == 3:
			for loc in visible:	
				button_array[loc].labeltype(FL_NO_LABEL)
				button_array[loc].redraw()

	widget.labeltype(FL_NORMAL_LABEL)

numbers = [number for number in range(1, 9)] + [number for number in range(1, 9)]
window = Fl_Window(100, 100, 330, 330, "Memory")

button_array = []

window.begin()

x = 5
y = 5
w = 80
h = 80

for i in range(1, 17):
	number = random.choice(numbers)
	button_array.append(Fl_Button(x, y, w, h, str(number)))
	button_array[-1].callback(go)
	button_array[-1].labeltype(FL_NO_LABEL)
	if i == 4 or i == 8 or i == 12 or i == 16:
		x = 5
		y += 80
	else:
		x += 80
	numbers.remove(number)

selected = []

'''pack1 = Fl_Pack(5, 5, 80, 80)
pack1.begin()

for i in range(0, 4):
	pack2 = Fl_Pack(0, 0, 0, 80)
	pack2.begin()
	
	for i in range(0, 4):
		number = random.choice(numbers)
		button_array.append(Fl_Button(0, 0, 80, 0, str(number)))
		button_array[-1].callback(go)
		numbers.remove(number)
		print i

	pack2.end()
	pack2.type(FL_HORIZONTAL)
	pack2.spacing(0)

pack1.end()
pack1.type(FL_VERTICAL)
pack1.spacing(0)'''

window.end()
window.show()
Fl.run()
