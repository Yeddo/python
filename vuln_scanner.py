import socket
import os
import sys

def retBanner(ip, port):
 	try:
		socket.setdefaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return
		
def checkVulns(banner):
	f = open("vuln_banners.txt",'r')
	for line in f.readlines():
		if line.strip('\n') in banner:
			print "[+] Server is vulnerable: " +banner.strip('\n')

def main():
	if len(sys.argv) == 2:
		filename = sys.argv[1]
		if not os.path.isfile(filename):
			print '[-] ' + filename + ' access denied.'
			exit(0)
		if not os.access(filename, os.R_OK):
			print '[-] ' + filename + ' access denied.'
			exit(0)
	else:
		print '[-] Usage: ' + str(sys.argv[0])
		exit(0)
						
	portList = [22,139,445]
	for x in range(1,16):
		ip = '10.0.0.' +str(x)
		for port in portList:
			banner = retBanner(ip,port)
			if banner:
				checkVulns(banner)
	
if __name__ == '__main__':
		main()
		
		
		
		
		
		
