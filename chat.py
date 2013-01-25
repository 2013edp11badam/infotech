#!/usr/bin/python

from fltk import *

def send(w_id):
	global nickname
	split_input = input1.value().split(' ')

	if input1.value() == '':
		pass
	elif split_input[0] == '/nick':
		nickname = input1.value().split(' ')[1]
		chat.value(chat.value() + str('Your nickname has been changed to ' + nickname + '\n'))
	elif split_input[0] == '/clear':
		chat.value('')
	else:
		chat.value(chat.value() + str(nickname + ': ' + input1.value() + '\n'))

	input1.value('')

nickname = 'unnamed'

window = Fl_Window(100, 100, 610, 440, "Chat")
window.begin()

chat = Fl_Multiline_Output(5, 5, 600, 400)
input1 = Fl_Input(5, 410, 525, 25)
button1 = Fl_Return_Button(535, 410, 70, 25, 'Send') 

window.end()
button1.callback(send)
window.show()
Fl.run()
