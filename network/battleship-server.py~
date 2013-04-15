#!/usr/bin/env python

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', int(sys.argv[1]))
sock.bind(server_addr)

clients = {}
p1_ships = []
p2_ships = []

print 'listening on %s:%s' % server_addr

while True:
	data, client_addr = sock.recvfrom(32)
	print 'received %s from %s:%s' % (data, client_addr[0], client_addr[1])
	if data == 'connect':
					
