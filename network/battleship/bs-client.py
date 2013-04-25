#!/usr/bin/env python

from fltk import *
import sys, socket

class Window(Fl_Window):
	def __init__(self, x, y, label):
		Fl_Window.__init__(self, x, y, 310, 640, label)

		self.begin()

		# game status
		# 0 - picking ships
		# 1 - playing
		self.game_status = 0

		self.client_ships = []

		# various colours
		self.COLOR_SHIP = FL_DARK_BLUE
		self.COLOR_SHOT_HIT = FL_RED
		self.COLOR_SHOT_MISS = FL_DARK2

		# game widgets
		self.box_status = Fl_Box(35, 308, 240, 25)
		self.box_status.label("Pick the location of your ships!")

		# generate board for my shots
		self.board_shots = []
		for y in range(10):
			for x in range(10):
					self.board_shots.append(Fl_Button(5 + (x * 30), 5 + (y * 30), 30, 30))
					self.board_shots[-1].callback(self.on_click)
					self.board_shots[-1].box(FL_THIN_UP_BOX)
		self.disable_board(self.board_shots)

		# generate board for my ships
		self.board_ships = []
		for y in range(10):
			for x in range(10):
					self.board_ships.append(Fl_Button(5 + (x * 30), 335 + (y * 30), 30, 30))
					self.board_ships[-1].callback(self.on_click)
					self.board_ships[-1].box(FL_THIN_UP_BOX)

		self.end()

		# connect to server
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_addr = (sys.argv[1], int(sys.argv[2]))

		# receive function
		self.fd = self.sock.fileno()
		Fl.add_fd(self.fd, self.receive)

	def on_click(self, w_id):
		if self.game_status == 0:
			if self.board_ships.index(w_id) not in self.client_ships:
				if len(self.client_ships) == 4:
					self.disable_board(self.board_ships)
					self.game_status = 1
					self.their_turn()
				self.client_ships.append(self.board_ships.index(w_id))
				self.sock.sendto(str(self.board_ships.index(w_id)), self.server_addr)
				self.last_sent = self.board_ships.index(w_id)
				w_id.color(self.COLOR_SHIP)

		elif self.game_status == 1:
			self.sock.sendto(str(self.board_shots.index(w_id)), self.server_addr)
			self.sock.sendto('222', self.receive_addr)
			self.last_sent = self.board_shots.index(w_id)
			self.disable_board(self.board_shots)
			self.their_turn()

	def receive(self, fd):
		data, self.receive_addr = self.sock.recvfrom(32)
		print 'received %s from server (%s:%s)' % (data, self.receive_addr[0], self.receive_addr[1])
		
		if int(data) == 1:
			self.board_shots[self.last_sent].color(self.COLOR_SHOT_HIT)
			self.board_shots[self.last_sent].redraw()
		elif int(data) == 0:
			self.board_shots[self.last_sent].color(self.COLOR_SHOT_MISS)
			self.board_shots[self.last_sent].redraw()

		if int(data) == 222:
			self.your_turn()
		
	def enable_board(self, board):
		for button in board:
			button.activate()

	def disable_board(self, board):
		for button in board:
			button.deactivate()

	def your_turn(self):
		self.enable_board(self.board_shots)
		self.box_status.box(FL_THIN_UP_BOX)
		self.box_status.label("Your turn!")
		self.box_status.labelcolor(FL_DARK_GREEN)

	def their_turn(self):
		self.disable_board(self.board_shots)
		self.box_status.box(FL_THIN_DOWN_BOX)
		self.box_status.label("Their turn!")
		self.box_status.labelcolor(FL_DARK_RED)

battleship_client = Window(100, 100, "Battleship Client")
battleship_client.show()
Fl.run()
battleship_client.sock.close()