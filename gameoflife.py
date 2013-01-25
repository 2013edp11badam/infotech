#!/usr/bin/python
import time
from fltk import *

def update_buttons():
	if button_play_pause.label() == 'Start':
		button_play_pause.label('Stop')
		button_play_pause.callback(stop)
		button_clear.deactivate()
		menu_speed.deactivate()
	else:
		button_play_pause.label('Start')
		button_play_pause.callback(start)
		button_clear.activate()
		menu_speed.activate()

def change_state(w_id):
	if w_id.color() == FL_BLACK:
		w_id.color(FL_WHITE)
	else:
		w_id.color(FL_BLACK)

def change_speed(w_id, new_speed):
	global speed
	speed = 1/new_speed

def clear(w_id):
	for button in gol:
		button.color(FL_WHITE)
		button.redraw()

def start(w_id):
	global go
	go = True
	update_buttons()
	run()

def stop(w_id):
	global go
	go = False
	update_buttons()

def run():
	while go:
		tick()
		Fl.check()
		#time.sleep(speed)

def tick():
	live, dead = [], []

	for button in gol:
		index = gol.index(button)
		neighbours = [	index - 1, 	# left
						index - 65, # top-left
						index - 64,	# top-center
						index - 63, # top-right
						index + 1, 	# right
						index + 65, # bottom-right
						index + 64,	# bottom-center
						index + 63] # bottom-left

		neighbour_count = 0

		for neighbour in neighbours:
			try:
				if gol[neighbour].color() == FL_BLACK:
					neighbour_count += 1
			except IndexError:
				pass

		if neighbour_count < 2:
			dead.append(gol.index(button))
		elif neighbour_count == 3:
			live.append(gol.index(button))
		elif neighbour_count > 3:
			dead.append(gol.index(button))

		neighbour_count = 0

	for button in live:
		gol[button].color(FL_BLACK)
		gol[button].redraw()
	for button in dead:
		if gol[button].color() == FL_BLACK:
			gol[button].color(FL_WHITE)
			gol[button].redraw()

	Fl.check()

window = Fl_Window(650, 680, 'Conway\'s Game of Life')
window.begin()

button_play_pause = Fl_Return_Button(5, 5, 160, 25, 'Start')
button_clear = Fl_Button(170, 5, 80, 25, 'Clear')

menu_speed = Fl_Menu_Button(615, 5, 30, 25)
menu_speed.add('15', 0, change_speed, 15)
menu_speed.add('30', 0, change_speed, 30)
menu_speed.add('45', 0, change_speed, 45)
menu_speed.add('60', 0, change_speed, 60)

global speed
speed = 1/30

x, y = 5, 35
w, h = 64, 64

gol = []

for a in range(w):
	for b in range(h):
		gol.append(Fl_Button(x, y, 10, 10))
		gol[-1].box(FL_FLAT_BOX)
		gol[-1].color(FL_WHITE)
		gol[-1].callback(change_state)
		x += 10
	x = 5
	y += 10

window.end()

button_play_pause.callback(start)
button_clear.callback(clear)

window.show()
Fl.run()
