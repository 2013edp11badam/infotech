#!/usr/bin/python
import os
from fltk import *

def play(w_id):
	for x in range(1, playlist.size()):
		if playlist.selected(x):
			song = playlist.text(x)
			os.system('ogg123 ' + folder + '/' + song + ' &')
	button_stop.activate()
	button_play.deactivate()

def stop(w_id):
	os.system('pkill ogg123')
	button_play.activate()
	button_stop.deactivate()
	

def choose_dir(w_id):
	global folder
	folder = fl_dir_chooser('Choose directory...', '/home/senior/music/', 0)
	try:
		for file in os.listdir(folder):
			playlist.add(file)
		button_play.activate()
	except TypeError:
		pass

window = Fl_Window(480, 365)
window.begin()

button_play = Fl_Button(5, 5, 80, 25, 'Play')
button_play.deactivate()
button_stop = Fl_Button(90, 5, 80, 25, 'Stop')
button_stop.deactivate()
button_dir = Fl_Button(175, 5, 300, 25, 'Choose directory')
slider = Fl_Slider(5, 35, 470, 25)
slider.slider_size(0.02)
slider.type(FL_HORIZONTAL)
playlist = Fl_Multi_Browser(5, 65, 470, 300)

window.end()

button_play.callback(play)
button_stop.callback(stop)
button_dir.callback(choose_dir)

window.show()
Fl.run()

