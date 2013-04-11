#!/usr/bin/env python

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', int(sys.argv[1]))
sock.bind(server_addr)

clients = {}
ships = [1, 11, 2, 22, 3, 33, 4, 44, 5, 55, 6, 66, 7, 77, 8, 88, 9, 99]

print 'listening on %s:%s' % server_addr

while True:
	data, client_addr = sock.recvfrom(32)
	print 'received %s from %s:%s' % (data, client_addr[0], client_addr[1])
	if data == 'connect':
		if len(clients) == 0:
			clients['p1'] = client_addr
			sock.sendto('yap1', client_addr)
		elif len(clients) == 1:
			clients['p2'] = client_addr
			sock.sendto('yap2', client_addr)
	else:
		if int(data) in ships:
			sock.sendto('1', client_addr)
			print 'sent 1'
		else:
			sock.sendto('0', client_addr)
			print 'sent 0'
