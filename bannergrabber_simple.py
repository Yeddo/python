#!/usr/bin/env python

import socket

def retBanner(ip,port):
	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return

def main():
	### print and return results for use by parent
	banner = retBanner('192.168.56.101', 22)
	print banner
	


if __name__ == '__main__':
	main()
