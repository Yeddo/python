#!/usr/bin/env python

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((sys.argv[1], 10000))

buff = "A"*500

sock.send(buff)

print sock.recv(1024)

sock.close()
