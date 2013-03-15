#/usr/bin/env python
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', 1234)
sock.connect(server_addr)

try:
	while True:
		msg = raw_input()
		sock.sendall(msg)
except KeyboardInterrupt:
	sock.close()
