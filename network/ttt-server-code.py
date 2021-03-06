#/usr/bin/env python
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', int(sys.argv[1]))

clients = {}

print 'listening on %s:%s' % server_addr

while True:
	try:
		data, client_addr = sock.recvfrom(1)
		print 'received %d from %s:%s' % (int(data), client_addr)
		if data == '0':
			if len(clients) == 0:
				clients['p1'] = client_addr
				print '%s:%s is player 1' % client_addr
			elif len(clients) == 1:
				clients['p2'] = client_addr
				print '%s:%s is player 2' % client_addr
