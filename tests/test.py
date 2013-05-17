#!/usr/bin/python
from fltk import *

def add_number(w_id, number):
	output1.value(output1.value() + str(number))

window = Fl_Window(320, 320, 'FLTK Test #2')
window.begin()

buttons = []
x, y = 40, 40

for button in range(1, 10):
	buttons.append(Fl_Button(x, y, 40, 40, str(button)))
	buttons[-1].callback(add_number, button)
	if button == 3 or button == 6:
		y += 40
		x = 40
	else:
		x += 40

output1 = Fl_Output(160, 160, 120, 40)

window.end()
window.show()
Fl.run()
