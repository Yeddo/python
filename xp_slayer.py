#!/usr/bin/env python

import nmap

ip = raw_input('Please enter the IP address or range you would like to scan:\n')

# creating a portscanner object and scanning ip range for port 445
nm = nmap.PortScanner()
nm.scan(ip, '22, 445', arguments='-Pn')

# for all live hosts, checking if port 22 or 445 are open and appending to list
smb = []
ssh = []

for host in nm.all_hosts():
	if nm[host]['tcp'][445]['state'] == 'open':
		smb.append(host)

for host in nm.all_hosts():
	if nm[host]['tcp'][22]['state'] == 'open':
		ssh.append(host)

