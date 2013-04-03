#/usr/bin/env python
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('127.0.0.1', int(sys.argv[1]))
sock.bind(server_addr)

print 'listening on %s:%s' % server_addr

while True:
	try:
		data, client_addr = sock.recvfrom(1)
		print 'received %d from %s:%s' % (int(data), client_addr[0], client_addr[1])
	except ValueError:
		pass
