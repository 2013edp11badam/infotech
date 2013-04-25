#!/usr/bin/env python

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('0.0.0.0', int(sys.argv[1]))
sock.bind(server_addr)

clients = {}
#p1_ships = ['29', '39', '49', '59', '69'] + ['6', '7', '8', '9'] + ['51', '52', '53'] + ['76', '86', '96'] + ['82', '92']
p1_ships = ['29', '39', '49', '59', '69']
p2_ships = ['6', '7', '8', '9']

print 'listening on %s:%s' % server_addr

while True:
	data, client_addr = sock.recvfrom(32)
	print 'received %s from %s:%s' % (data, client_addr[0], client_addr[1])
	if client_addr in clients.values():
		if clients['p1'] == client_addr:
			if data in p2_ships:
				sock.sendto(str(1), client_addr)
				print 'sent 1'
			else:
				sock.sendto(str(0), client_addr)
				print 'send 0'
			sock.sendto('ot', clients['p1'])
			sock.sendto('yt', clients['p2'])
			print 'p2 turn'
		else:
			if data in p1_ships:
				sock.sendto(str(1), client_addr)
				print 'sent 1'
			else:
				sock.sendto(str(0), client_addr)
				print 'send 0'
			sock.sendto('yt', clients['p1'])
			sock.sendto('ot', clients['p2'])
			print 'p1 turn'
	else:
		if len(clients) == 0:
			clients['p1'] = client_addr
			sock.sendto('yt', client_addr)
			print clients
		elif len(clients) == 1:
			clients['p2'] = client_addr
			sock.sendto('ot', client_addr)
			print clients
