#!/usr/bin/python

from fltk import *
import socket

class TicTacToe(Fl_Window):
	def __init__(self):
		Fl_Window.__init__(self, 100, 100, 310, 370, 'Tic Tac Toe')

		self.begin()
		self.button_connect = Fl_Button(5, 5, 120, 25, 'Connect...')
		self.button_connect.callback(self.connect)
		self.button_disconnect = Fl_Button(130, 5, 175, 25, 'Disconnect')
		self.button_disconnect.deactivate()

		self.array_buttons = []
		for y in xrange(3):
			for x in xrange(3):
				self.array_buttons.append(Fl_Button(x * 100 + 5, y * 100 + 35, 100, 100))
				self.array_buttons[-1].callback(self.send)
				self.array_buttons[-1].deactivate()

		self.output_status = Fl_Output(5, 340, 300, 25)
		self.output_status.value('Idle')
		self.end()

	def connect(self, w_id):
		server_info = fl_input('Enter the server IP and port (<ip>:<port>)!', '').split(':')
		try:
			self.host, self.port = server_info[0], server_info[1]
			self.connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			self.connection.connect((self.host, int(self.port)))
			self.button_disconnect.activate()
			self.output_status.value('Connected to ' + self.host + ':' + str(self.port))
			self.connection.send("2")
			#for button in self.array_buttons:
				#button.activate()
		except IndexError:
			fl_message('Invalid IP/port!')
		except AttributeError:
			fl_message('Invalid IP/port!')

	def disconnect(self, w_id):
		self.connection.close()
		self.output_status.value('Disconnected from ' + self.host + ':' + str(self.port))

	def send(self, w_id):
		self.connection.send(str(2))
		w_id.label('O')
		#for button in self.array_buttons:
		#	button.deactivate()

	def receive(self):
		(self.receive_data, self.addr) = self.connection.recvfrom(1024)
		print self.receive_data, self.addr
		#for button in self.array_buttons:
		#	button.activate()

ttt = TicTacToe()
ttt.show()
Fl.run()
