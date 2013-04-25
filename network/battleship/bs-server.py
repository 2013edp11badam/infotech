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

		# various colours
		self.COLOR_SHIP = FL_DARK_BLUE
		self.COLOR_SHOT_HIT = FL_RED
		self.COLOR_SHOT_MISS = FL_DARK2

		# server ships and client ships
		self.server_ships = []
		self.client_ships = []

		self.server_hit_shots = []
		self.client_hit_shots = []

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

		# bind to ip and start listening
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.server_addr = ('0.0.0.0', int(sys.argv[1]))
		self.sock.bind(self.server_addr)

		print 'listening on %s:%s' % self.server_addr

		# receive function
		self.fd = self.sock.fileno()
		Fl.add_fd(self.fd, self.receive)

	def on_click(self, w_id):
		if self.game_status == 0:
			if self.board_ships.index(w_id) not in self.server_ships:
				if len(self.server_ships) == 4:
					self.disable_board(self.board_ships)
					self.your_turn()
					self.game_status = 1
				self.server_ships.append(self.board_ships.index(w_id))
				w_id.color(self.COLOR_SHIP)

			print 'SERVER SHIPS:', self.server_ships

		# TODO: REDO THIS PART BELOW
		elif self.game_status == 1:
			if self.board_shots.index(w_id) in self.client_ships:
				if len(self.server_hit_shots) == 4:
					fl_message('You have sunken all of your opponents battleships! Congraulations, you win!')
				else:
					self.server_hit_shots.append(self.board_shots.index(w_id))
				w_id.color(self.COLOR_SHOT_HIT)
				self.disable_board(self.board_shots)
			else:
				w_id.color(self.COLOR_SHOT_MISS)
				self.their_turn()
			self.sock.sendto('222', self.receive_addr)

	def receive(self, fd):
		data, self.receive_addr = self.sock.recvfrom(32)
		print 'received %s from client (%s:%s)' % (data, self.receive_addr[0], self.receive_addr[1])
		
		if self.game_status == 0:
			if int(data) not in self.client_ships:
				if len(self.client_ships) < 5:
					self.client_ships.append(int(data))
					print 'CLIENT SHIPS:', self.client_ships

		elif self.game_status == 1:
			if int(data) < 100 and int(data) in self.server_ships:
				self.sock.sendto('1', self.receive_addr)
				print 'SENT 1 B/C DATA IN LIST'
			elif int(data) < 100 and int(data) not in self.server_ships:
				self.sock.sendto('0', self.receive_addr)
				print 'SENT 0 B/C DATA NOT IN LIST'

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

battleship_server = Window(100, 100, "Battleship Server")
battleship_server.show()
Fl.run()
battleship_server.sock.close()