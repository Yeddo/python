#!/usr/bin/env python

import nfqueue
from scapy.all import *
import os
import zlib, StringIO, gzip

#os.system('iptables -A INPUT -p tcp --sport 80 -j NFQUEUE')
os.system('iptables -A OUTPUT -p tcp --dport 80 -j NFQUEUE')
#os.system('iptables -t nat -A PREROUTING -p tcp --dport 80 -j NFQUEUE')

def callback(payload):
	print 'at least got this far'
	data = payload.get_data()
	pkt = IP(data)
	if not pkt.haslayer(Raw):
		payload.set_verdict(nfqueue.NF_ACCEPT)
	else:
		print 'got a packet'
		if 'Accept-Encoding' in pkt[Raw].load:
			print 'has encoding'
			pkt[Raw].load =  pkt[Raw].load.replace('Accept-Encoding', 'Accept-Rubbish!!!')
			print pkt[Raw].show()
			# recalculating checksums and whatnot...
			del pkt[IP].chksum
			pkt[IP].len = len(str(pkt))
			pkt[TCP].len = len(str(pkt[TCP]))
			payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(pkt), len(pkt))
		'''
		if 'gzip\r\n\r\n' in pkt[Raw].load:
			pkt[IP].len = len(str(pkt))
			pkt[TCP].len = len(str(pkt[TCP]))
				
			try:
				# setting up slice points
				# escape char doesn't count in index number
				# gzip len not neccessary, only need index numbers
				load = pkt[Raw].load
				gzip_len_start_index = load.find('gzip\r\n\r\n') + len('gzip\r\n\r\n')
				gzip_len = load[gzip_len_start_index:gzip_len_start_index + 7]
				gzip_start_index = gzip_len_start_index + 7 + len('\r\n')
				gzip_end_index = load.find('\r\n0\r\n\r\n')
				gzip_data = load[gzip_start_index:gzip_end_index]
				print gzip_len
				
				# decompressing gzip data, need to switch over to gzip lib to keep uniform...
				html = zlib.decompress(gzip_data, 16+zlib.MAX_WBITS)
				
				# modifying html, think I should insert addtional script
				# instead of replacing original one
				script_index = html.find('<script>')
				mod_html = html[:script_index] + '<script>alert("Hey there")</script>\n' + html[script_index:]
				
				# re-gzipping html
				out = StringIO.StringIO()
				with gzip.GzipFile(fileobj=out, mode='w') as f:
					f.write(mod_html)
				mod_gzip = out.getvalue()
				
				# modified gzip load size
				dec_mod_gzip_len = len(mod_gzip)
				hex_mod_gzip_len = hex(dec_mod_gzip_len).strip('0x')
				mod_gzip_len = ((7 - len(hex_mod_gzip_len)) * '0') + hex_mod_gzip_len
				
				# assembling modified load
				mod_load = load[:gzip_len_start_index] + mod_gzip_len + '\r\n' + mod_gzip + '\r\n0\r\n\r\n'

				# creating pkt to insert changed load
				# this breaks it, even if pkt isn't used and pkt is sent instead?!?!?!?!?!
				pkt[Raw].load = mod_load

			# recalculating checksums and whatnot...
			del pkt[IP].chksum
			pkt[IP].len = len(str(pkt))
			pkt[TCP].len = len(str(pkt[TCP]))
			payload.set_verdict_modified(nfqueue.NF_ACCEPT, str(pkt), len(pkt))
			except Exception, e:
				print 'Exception!!!!!!!!!!'
				print e
		else:
			payload.set_verdict(nfqueue.NF_ACCEPT)
			'''
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

main()
'''
'''
