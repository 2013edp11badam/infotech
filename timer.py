#!/usr/bin/python
from fltk import *

def start(w_id):
	button_stop.activate()
	button_start.deactivate()
	Fl.add_timeout(1.0, count)

def stop(w_id):
	button_start.activate()
	button_stop.deactivate()
	Fl.remove_timeout(count)

def reset(w_id):
	output1.value(str(0))

def count():
	output1.value(str(int(output1.value()) + 1))
	dial1.value(dial1.value() + 6.0)
	Fl.repeat_timeout(0.05, count)

window = Fl_Window(100, 100, 215, 275)
window.begin()

button_start = Fl_Button(5, 35, 100, 25, 'Start')
button_stop = Fl_Button(110, 35, 100, 25, 'Stop')
button_reset = Fl_Button(140, 5, 70, 25, 'Reset')
output1 = Fl_Output(5, 5, 130, 25)
output1.value('0')
dial1 = Fl_Dial(5, 65, 205, 205)
dial1.type(FL_LINE_DIAL)
dial1.angle1(180)
dial1.angle2(181)

window.end()

button_start.callback(start)
button_stop.callback(stop)
button_reset.callback(reset)

window.show()
Fl.run()
