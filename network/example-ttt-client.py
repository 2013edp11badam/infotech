import socket, sys
from fltk import *

class myWin(Fl_Window):
	def __init__(self, x, y, w, h, label):
		Fl_Window.__init__(self, x, y, w, h, label)
		self.buttons = []
		self.turn = True
		self.begin()
		for n in xrange(0, 3):
			for i in xrange(0, 3):
				self.buttons.append(Fl_Button(i * (w / 3), n * (h / 3), w / 3, h / 3))
				self.buttons[-1].callback(self.buttonPressed)
				self.buttons[-1].labelsize(150)
		self.end()
		self.host = sys.argv[1]
		self.port = int(sys.argv[2])
		self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.bufsize = 32
		self.fd = self.s.fileno()
		Fl.add_fd(self.fd, self.receiveData)

	def buttonPressed(self, w):
		if self.turn:
			self.s.sendto(str(self.buttons.index(w)), (self.host, self.port))
			w.label('O')
			w.deactivate()
			w.redraw()
			self.turn = False

	def receiveData(self, fd):
		(self.data, self.addr) = self.s.recvfrom(self.bufsize)
		w = self.buttons[int(self.data)]
		w.label('X')
		w.deactivate()
		w.redraw()
		self.turn = True

a = myWin(0, 0, 600, 600, 'TTT Client')
a.show()
Fl.run()
