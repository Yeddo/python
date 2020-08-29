#!/usr/bin/env python

import SocketServer

# create a class that is a subclass of BaseRequestHandler
# 
class EchoHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'Got connection from: ', self.client_address
		data = 'dummy'

		# self.request is client socket, uses .send() and 
		# .recv() methods
		self.request.send("Youre mom")
		while len(data):
			data = self.request.recv(1024)
			print 'Client sent: ' + data
			self.request.send(data)

		print 'Client left'

serverAddr = ('0.0.0.0', 9000)

# first element is a tuple containing ip addr and port
# second element is class of handler to handle connections
server = SocketServer.TCPServer(serverAddr, EchoHandler)
server.serve_forever()
