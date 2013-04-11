#!/usr/bin/env python

from fltk import *
import string, socket

class Battleship(Fl_Window):
	def __init__(self, x, y, w, h, label):
		Fl_Window.__init__(self, x, y, w, h, label)

		# define colors
		self.COLOR_NONE = fl_rgb_color(180, 180, 180)
		self.COLOR_SHIP = fl_rgb_color(130, 130, 130)
		self.COLOR_HIT = fl_rgb_color(200, 20, 20)
		self.COLOR_MISS = fl_rgb_color(50, 50, 50)

		self.begin()
		self.board = []
		for y in range(10):
			for x in range(10):
					self.board.append(Fl_Button(x * (w / 10), y * (h / 10), w / 10, h / 10))
					self.board[-1].callback(self.send)
					self.board[-1].color(self.COLOR_NONE)
					self.board[-1].box(FL_THIN_UP_BOX)
					self.board[-1].labelsize(h / 42)
		self.end()

		# connect to server
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_addr = ('127.0.0.1', int(sys.argv[1]))

		self.sock.sendto('connect', self.server_addr)

		# receive
		self.fd = self.sock.fileno()
		Fl.add_fd(self.fd, self.receive)

	def send(self, w_id):
		self.last_sent = self.board.index(w_id)
		self.sock.sendto(str(self.last_sent), self.server_addr)
		print 'sent ' + str(self.board.index(w_id)) + ' to ' + self.server_addr[0] + ':'

	def receive(self, fd):
		(data, addr) = self.sock.recvfrom(32)
		if data == '1':
			self.board[self.last_sent].label('HIT')
			self.board[self.last_sent].labelcolor(FL_WHITE)
			self.board[self.last_sent].color(self.COLOR_HIT)
			self.board[self.last_sent].deactivate()
		elif data == '0':
			self.board[self.last_sent].label('MISS')
			self.board[self.last_sent].labelcolor(self.COLOR_MISS)
			self.board[self.last_sent].deactivate()
		else:
			print data

	#def modify_board(self, arg):
	#	for button in board:
	#		if arg == 1:
	#			button.activate()
	#		else:
	#			button.deactivate()

bs = Battleship(100, 100, 600, 600, 'Battleship')
bs.show()
Fl.run()
