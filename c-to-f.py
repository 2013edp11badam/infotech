#!/usr/bin/python

from fltk import *

def convert(w_id):
	try:
		farenheit = (1.8 * float(input1.value())) + 32
		output1.value(str(farenheit))
		multibrowser1.add(str(input1.value()) + ' C = ' + str(output1.value()) + ' F')
		input1.value('')
	except ValueError:
		output1.value('error')

window = Fl_Window(100, 100, 205, 205, "C to F")
window.begin()

input1 = Fl_Input(5, 5, 95, 25)
output1 = Fl_Output(105, 5, 95, 25)
multibrowser1 = Fl_Multi_Browser(5, 65, 195, 135)
button1 = Fl_Return_Button(5, 35, 195, 25, "Convert")

window.end()
button1.callback(convert)
window.show()
Fl.run()
