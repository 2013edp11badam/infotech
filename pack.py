#!/usr/bin/python
from fltk import *

def changemylabel(widget):
	if Fl.event_button() == FL_RIGHT_MOUSE:
		widget.color(FL_GREEN)
	if Fl.event_button() == FL_LEFT_MOUSE:
		#widget.color(FL BLUE)
		widget.deactivate()
		widget.label("Hello")
	
	if (widget.labeltype() == FL_NO_LABEL):
		widget.labeltype(FL_NORMAL_LABEL)
	else:
		widget.labeltype(FL_NO_LABEL)

window = Fl_Window(600, 50, 340, 440, "my gui")

pic = Fl_JPEG_Image("guyf.jpg")
butarray=[]

window.begin()

mainpack=Fl_Pack(20,20,300,400)
mainpack.begin()

for i in range(0,3):
	pack = Fl_Pack(0,0,0,100)
	pack.begin()

	for x in range(0,3):
		butarray.append(Fl_Button(0,0,80,0,"****"))
		butarray[-1].color(FL_RED)
		butarray[-1].callback(changemylabel)

	pack.end()
	pack.type(FL_HORIZONTAL)
	pack.spacing(20)

mainpack.end()
mainpack.type(FL_VERTICAL)
mainpack.spacing(20)

window.end()
Fl.scheme("gtk+")
window.show()
Fl.run()
