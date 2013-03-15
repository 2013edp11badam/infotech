#!/usr/bin/python

import socket
from fltk import *

class Chat(Fl_Window):
	def __init__(self):
		# open chat window and init buttons, chatbox, etc.
		Fl_Window.__init__(self, 100, 100, 610, 440, "Chat")

		self.begin()
		self.output_chat = Fl_Multiline_Output(5, 5, 600, 400)
		self.input_message = Fl_Input(5, 410, 525, 25)
		self.button_send = Fl_Return_Button(535, 410, 70, 25, 'Send')
		self.button_send.callback(self.send)
		self.end()
	
	def send(self):
		# send message to server
		if self.input_message.value() != '':
			self.output_chat.value(self.output_chat.value() + str('unnamed' + ': ' + self.input_message.value() + '\n'))
			self.input_message.value('')	

	def receive(self):
		# receive message and post message to chat
		pass

class Connect(Fl_Window):
	def __init__(self):
		# open connection window and init buttons, textbox, etc.
		Fl_Window.__init__(self, 100, 100, 270, 65, "Connect to Server")

		self.begin()
		self.input_server = Fl_Input(5, 5, 200, 25)
		self.input_port = Fl_Input(215, 5, 50, 25, ':')
		self.button_connect = Fl_Return_Button(5, 35, 260, 25, 'Connect')
		#self.output_status = Fl_Output()
		self.end()

	def connect(self, server, port):
		# connect to server
		pass

#chatwindow = Chat()
#chatwindow.show()
connectwindow = Connect()
connectwindow.show()

Fl.run()

"""def send(w_id):
	global nickname
	split_input = input1.value().split(' ')

	if split_input[0] == '/nick':
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
Fl.run()"""
