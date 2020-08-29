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

for x in range(0, 256):
	print 'IP address: %s' %'169.254.7.' + str(x)
	print retBanner('169.254.7.' + str(x), 22)

#print 'The banner is: '
#print retBanner('192.168.43.3', 22)
