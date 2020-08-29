#!/usr/bin/env python

import json

n = ['22.63.0.0/18', '23.63.5.0/24', '23.63.10.0/26', '23.63.100.0/22', '23.63.192.0/18']
net0 = ''.join(format(int(x), '08b') for x in n[0].split('/')[0].split('.'))[0:int(n[0].split('/')[1])]
net1 = ''.join(format(int(x), '08b') for x in n[1].split('/')[0].split('.'))[0:int(n[1].split('/')[1])]
net2 = ''.join(format(int(x), '08b') for x in n[2].split('/')[0].split('.'))[0:int(n[2].split('/')[1])]
net3 = ''.join(format(int(x), '08b') for x in n[3].split('/')[0].split('.'))[0:int(n[3].split('/')[1])]
net4 = ''.join(format(int(x), '08b') for x in n[4].split('/')[0].split('.'))[0:int(n[4].split('/')[1])]

net0_count = 0
net1_count = 0
net2_count = 0
net3_count = 0
net4_count = 0

# opens file as a list
ip_list = json.loads(open('ipaddr2.json').read())

for ip in ip_list:
	bin_ip = ''.join(format(int(x), '08b') for x in ip.split('.'))
	if bin_ip[0:len(net0)] == net0:
		net0_count += 1
	elif bin_ip[0:len(net1)] == net1:
		net1_count +=1
	elif bin_ip[0:len(net2)] == net2:
		net2_count +=1
	elif bin_ip[0:len(net3)] == net3:
		net3_count +=1
	elif bin_ip[0:len(net4)] == net4:
		net4_count +=1

print('Net 0: ' + str(net0_count))
print('Net 1: ' + str(net1_count))
print('Net 2: ' + str(net2_count))
print('Net 3: ' + str(net3_count))
print('Net 4: ' + str(net4_count))
