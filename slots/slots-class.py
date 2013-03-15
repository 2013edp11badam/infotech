#!/usr/bin/python
import random, time, glob
from fltk import *

class Slots():
	def __init__(self):
		# import self.images from 'self.images' folder
		self.images = []

		for image in glob.glob("images/*.png"):
			self.images.append(Fl_PNG_Image(image))

		self.credits = 5

		# create window and widgets
		self.window = Fl_Window(100, 100, 620, 245, 'Slot Machine')
		self.window.begin()

		self.slot1 = Fl_Box(5, 5, 200, 200)
		self.slot1.box(FL_UP_BOX)
		self.slot2 = Fl_Box(210, 5, 200, 200)
		self.slot2.box(FL_UP_BOX)
		self.slot3 = Fl_Box(415, 5, 200, 200)
		self.slot3.box(FL_UP_BOX)
		self.button_credits = Fl_Button(575, 210, 40, 30, 'Add')
		self.button_pull = Fl_Button(210, 210, 200, 30, 'Pull')
		self.credits_output = Fl_Output(505, 210, 65, 30, 'Credits:')
		self.credits_output.value(str(self.credits))

		self.window.end()

		self.set_slots()

		self.button_credits.callback(self.change_credits, 5)
		self.button_pull.callback(self.pull_slots)

		self.window.show()
		Fl_run()

	def change_credits(self, w_id, num):
		self.credits += num
		self.credits_output.value(str(self.credits))

	def set_slots(self):
		# used to set slots when program runs (no animation)
		random.shuffle(self.images)

		self.slot1.hide()
		self.slot2.hide()
		self.slot3.hide()
	
		self.slot1.image(self.images[0].copy(self.slot1.w() - 20, self.slot1.h() - 20))
		self.slot2.image(self.images[1].copy(self.slot2.w() - 20, self.slot2.h() - 20))
		self.slot3.image(self.images[2].copy(self.slot3.w() - 20, self.slot3.h() - 20))

		self.slot1.show()
		self.slot2.show()
		self.slot3.show()

	def pull_slots(self, w_id):
		# used to pull slots after clicking on button (animation)

		self.button_pull.deactivate()
		self.credits_output.deactivate()
		self.button_credits.deactivate()

		if credits > 0:
			self.change_credits('', -1)
			self.credits_output.value(str(self.credits))

			for x in range(60):
				if x <= 20:
					self.slot1_value = random.randint(0, len(self.images) - 1)
					self.slot1.image(self.images[self.slot1_value].copy(self.slot1.w() - 20, self.slot1.h() - 20))
					self.slot1.redraw()
				if x <= 40:
					self.slot2_value = random.randint(0, len(self.images) - 1)
					self.slot2.image(self.images[self.slot2_value].copy(self.slot2.w() - 20, self.slot2.h() - 20))
					self.slot2.redraw()
				if x <= 60:
					self.slot3_value = random.randint(0, len(self.images) - 1)
					self.slot3.image(self.images[self.slot3_value].copy(self.slot3.w() - 20, self.slot3.h() - 20))
					self.slot3.redraw()
				time.sleep(0.05)
				Fl.check()

			if self.slot1_value == self.slot2_value == self.slot3_value:
				self.change_credits('', 20)
				fl_message('Triple play! Have a generous serving of credits (20).')
			elif self.slot1_value == self.slot2_value or self.slot2_value == self.slot3_value or self.slot3_value == self.slot1_value:
				self.change_credits('', 5)
				fl_message('Double! Have a bunch of credits (5).')

			self.button_pull.activate()
			self.credits_output.activate()
			self.button_credits.activate()

		else:
			fl_message('You have an insufficent amount of credits.')

slots_window = Slots()
