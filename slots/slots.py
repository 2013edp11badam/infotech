#!/usr/bin/python
import random, time, glob
from fltk import *

def change_credits(w_id, num):
	global credits
	credits += num
	credits_output.value(str(credits))

def set_slots():
	# used to set slots when program runs (no animation)
	random.shuffle(images)

	slot1.hide()
	slot2.hide()
	slot3.hide()
	
	slot1.image(images[0].copy(slot1.w() - 20, slot1.h() - 20))
	slot2.image(images[1].copy(slot2.w() - 20, slot2.h() - 20))
	slot3.image(images[2].copy(slot3.w() - 20, slot3.h() - 20))

	slot1.show()
	slot2.show()
	slot3.show()

def pull_slots(w_id):
	# used to pull slots after clicking on button (animation)

	button_pull.deactivate()
	credits_output.deactivate()
	button_credits.deactivate()
	zz

	if credits > 0:
		change_credits('', -1)
		credits_output.value(str(credits))

		for x in range(60):
			if x <= 20:
				slot1_value = random.randint(0, len(images) - 1)
				slot1.image(images[slot1_value].copy(slot1.w() - 20, slot1.h() - 20))
				slot1.redraw()
			if x <= 40:
				slot2_value = random.randint(0, len(images) - 1)
				slot2.image(images[slot2_value].copy(slot2.w() - 20, slot2.h() - 20))
				slot2.redraw()
			if x <= 60:
				slot3_value = random.randint(0, len(images) - 1)
				slot3.image(images[slot3_value].copy(slot3.w() - 20, slot3.h() - 20))
				slot3.redraw()
			time.sleep(0.1)
			Fl.check()

		if slot1_value == slot2_value == slot3_value:
			change_credits('', 20)
			fl_message('Triple play! Have a generous serving of credits (20).')
		elif slot1_value == slot2_value or slot2_value == slot3_value or slot3_value == slot1_value:
			change_credits('', 5)
			fl_message('Double! Have a bunch of credits (5).')

		button_pull.activate()
		credits_output.activate()
		button_credits.activate()

	else:
		fl_message('You have an insufficent amount of credits.')

# import images from 'images' folder
images = []

for image in glob.glob("images/*.png"):
	images.append(Fl_PNG_Image(image))

# set credits
global credits
credits = 5

# create window and widgets
window = Fl_Window(100, 100, 620, 245, 'Slot Machine')
window.begin()

slot1 = Fl_Box(5, 5, 200, 200)
slot1.box(FL_UP_BOX)
slot2 = Fl_Box(210, 5, 200, 200)
slot2.box(FL_UP_BOX)
slot3 = Fl_Box(415, 5, 200, 200)
slot3.box(FL_UP_BOX)
button_credits = Fl_Button(575, 210, 40, 30, 'Add')
button_pull = Fl_Button(210, 210, 200, 30, 'Pull')
credits_output = Fl_Output(505, 210, 65, 30, 'Credits:')
credits_output.value(str(credits))

window.end()

set_slots()

button_credits.callback(change_credits, 5)
button_pull.callback(pull_slots)

window.show()
Fl_run()
