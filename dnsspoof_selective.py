#!/usr/bin/env python

import nfqueue
from scapy.all import *
import os

os.system('iptables -A INPUT -p udp --sport 53 -j NFQUEUE')

def callback(payload):
	data = payload.get_data()
	pkt = IP(data)
	if pkt[DNS].qr == 1:
		print pkt[DNSRR].rrname
	# recalculating checksums and whatnot...
	pkt[IP].len = len(str(pkt))
	pkt[TCP].len = len(str(pkt[TCP]))
	del pkt[IP].chksum
	payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(pkt), len(pkt))
	return 0
	
# forward packet untouched

def main():
	q = nfqueue.queue()
	q.open()
	q.bind(socket.AF_INET)
	q.set_callback(callback)
	q.create_queue(0)
	try:
		 q.try_run() # Main loop
	except KeyboardInterrupt:
		 q.unbind(socket.AF_INET)
		 q.close()
		 os.system('iptables -F')
		 os.system('iptables -X')

main()
