#!/usr/bin/env python

import threading
import Queue
from scapy.all import *

# create a new class as a subclass of threading.Thread
class workerthread(threading.Thread):
	def __init__(self, queue, address):
		# calling the threading.Thread class (parent class) __init__ method
		threading.Thread.__init__(self)
		# adding the queue attribute, passed to object when created
		self.queue = queue
		# adding the address attribute
		self.address = address
	
	# when worker.start() is called, run() is executed, putting the thread to work	
	def run(self):
		while True:
			port = self.queue.get()
			resp = sr1(IP(dst=self.address)/TCP(sport=60000, dport=port, flags=2), timeout=1, verbose=0)
			if resp:
				if resp[TCP].flags == 18:
					print "[+] Port " + str(port) + " open."
				self.queue.task_done()
			else:
				self.queue.task_done()
			
def main():
	queue = Queue.Queue()
	
	threads = raw_input('How many threads would you like to run?\n')
 	address = raw_input('Please enter the IP address you would like to scan.\n')
	
	# creating threads to execute tasks
	for i in range(int(threads)):
		worker = workerthread(queue, address)
		worker.setDaemon(True)
		worker.start()
	
	# making work, filling up the queue 	

	for i in range(1,1001):
		queue.put(i)
	
	queue.join()

	print 'All tasks complete'

if __name__ == '__main__':
	main()
