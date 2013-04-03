#/usr/bin/env python
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', int(sys.argv[1]))

try:
	while True:
		msg = raw_input('> ')
		sock.sendto(msg, server_addr)
except KeyboardInterrupt:
	sock.close()
