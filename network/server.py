#!/usr/bin/env python

import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((socket.gethostname(), 12345))
connection.listen(5)

print 'server running'

while True:
	try:
		client, addr = connection.accept()
		print 'connection from ' + addr[0])
		client.close()
	except KeyboardInterrupt:
		client.close()
		print 'connect closed unexpectedly'
