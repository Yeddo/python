#!/usr/bin/env python

from scapy.all import *

net = raw_input("Please input the network you would like to scan (scans a class 'C' network):\n")
targets = []
for num in range(1,256):
	targets.append(net.split('.')[0] + '.' + net.split('.')[1] + '.' + net.split('.')[2] + '.' + str(num))
for target in targets:
	resp = srp1(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(hwsrc="00:25:d3:99:e3:40", psrc="10.203.30.112", hwdst="ff:ff:ff:ff:ff:ff", pdst=target, op=1), verbose=0, timeout=0.2)
	print ('|' + 100*' ' + '|\r').strip('\n')
	print (' ' + int(int(target.split('.')[3])/len(targets))*'*' + '\r').strip('\n').strip('\n')
#	if resp:
#		print "IP address: " + target
