#/usr/bin/env python
import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_addr = ('127.0.0.1', int(sys.argv[1]))
sock.bind(server_addr)
sock.listen(1)

print >> sys.stdout, 'listening on %s:%s' % server_addr

while True:
	conn, client_addr = sock.accept()
	while True:
		try:
			print >> sys.stdout, 'received %d from %s:%s' % (int(conn.recv(1)), client_addr[0], client_addr[1])
		except ValueError:
			pass	
