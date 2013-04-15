#!/usr/bin/env python

from fltk import *
import string, socket

class MyBoard(Fl_Window):
	def __init__(self, x, y, w, h, label):
		Fl_Window.__init__(self, x, y, w, h, label)

		# define colors
		self.COLOR_NONE = fl_rgb_color(180, 180, 180)
		self.COLOR_SHIP = fl_rgb_color(130, 130, 130)
		self.COLOR_HIT = fl_rgb_color(200, 20, 20)
		self.COLOR_MISS = fl_rgb_color(50, 50, 50)

		# define game things
		self.status = 1
		self.ships = 0

		# create board
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

		# receive function
		self.fd = self.sock.fileno()
		Fl.add_fd(self.fd, self.receive)

	def send(self, w_id):
		self.sock.sendto(self.board.index(w_id), self.server_addr)

	def receive(self, fd):
		(data, addr) = self.sock.recvfrom(32)
		pass


mb = MyBoard(50, 100, 350, 350, 'My Board')
mb.show()

Fl.run()
