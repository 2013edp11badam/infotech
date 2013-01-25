#!/usr/bin/python

from fltk import *
import random, glob

def shuffle(w_id):
	random.shuffle(images)

	image1 = Fl_JPEG_Image(images[0])
	image2 = Fl_JPEG_Image(images[1])
	image3 = Fl_JPEG_Image(images[2])
	image4 = Fl_JPEG_Image(images[3])

	box1.image(image1.copy(box1.w(), box1.h()))
	box2.image(image2.copy(box2.w(), box2.h()))
	box3.image(image3.copy(box3.w(), box3.h()))
	box4.image(image4.copy(box4.w(), box4.h()))

	box1.redraw()
	box2.redraw()
	box3.redraw()
	box4.redraw()

	print 'Images shuffled, showing ' + images[0] + ', ' + images[1] + ', ' + images[2] + ', ' + images[3] + "\n"

images = []

for image in glob.glob("images/*.jpg"):
	images.append(image)
	print 'Added ' + image

window = Fl_Window(100, 100, 290, 295, "Shuffle!")
window.begin()

box1 = Fl_Box(5, 5, 140, 140)
box2 = Fl_Box(145, 5, 140, 140)
box3 = Fl_Box(5, 150, 140, 140)
box4 = Fl_Box(145, 150, 140, 140)

button1 = Fl_Return_Button(5, 135, 280, 25, "Shuffle")

shuffle(window)

window.end()
button1.callback(shuffle)
window.show()
Fl.run()
