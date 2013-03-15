#!/usr/bin/env python

import socket, sys

try:
	ip, port = sys.argv[1].split(':')[0], int(sys.argv[1].split(':')[1])

	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.connect((ip, port))
	print 'connected to', ip
	connection.close()
except IndexError:
	print 'invalid ip/port'
except KeyboardInterrupt:
	connection.close()
	print "\nclosed connection"
