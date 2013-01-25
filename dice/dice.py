#!/usr/bin/python

from fltk import *
import random, glob

def roll(w_id):
	random.shuffle(images)

	image1 = Fl_JPEG_Image(images[0])

	box1.image(image1.copy(box1.w(), box1.h()))
	box1.redraw()

images = []

for image in glob.glob("images/dice*.jpg"):
	images.append(image)

window = Fl_Window(100, 100, 260, 290, 'Roll Dice')
window.begin()

box1 = Fl_Box(5, 5, 250, 250)
button1 = Fl_Return_Button(5, 260, 250, 25, 'Roll Dice')

roll(window)

window.end()
button1.callback(roll)
window.show()
Fl.run()

	
