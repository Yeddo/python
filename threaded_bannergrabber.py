#!/usr/bin/env python

import threading
import Queue
import socket

Alive = []

# create a new class as a subclass of threading.Thread
class workerthread(threading.Thread):
	def __init__(self, queue):
		# calling the threading.Thread class (parent class) __init__ method
		threading.Thread.__init__(self)
		# adding the queue attribute, passed to object when created
		self.queue = queue
	
	# when worker.start() is called, run() is executed, putting the thread to work	
	def run(self):
		global Alive
		while True:
			try:
				ip = self.queue.get()
				print 'Trying IP address: ' + str(ip)
				socket.setdefaulttimeout(1)
				s = socket.socket()
				s.connect((str(ip), 22))
				banner = s.recv(1024)
				if banner != None:
					Alive.append(str(ip) + '\n')
					self.queue.task_done()	
			except:
				self.queue.task_done()
				continue
			
def main():
	global Alive		
	# creating an object of the queue class
	queue = Queue.Queue()
	
	threads = raw_input('How many threads would you like to run?\n')

	# creating threads to execute tasks
	for i in range(int(threads)):
		worker = workerthread(queue)
		worker.setDaemon(True)
		worker.start()
	
 	# splitting up the ip address, identifying ranges
 	address = raw_input('Please enter the IP address range you would like to scan.\n')
 	first =  address.split('.')[0]
 	second =  address.split('.')[1]
 	third =  address.split('.')[2]
 	fourth =  address.split('.')[3]
 	
 	if '-' in first:
 		fs = int(first.split('-')[0])
 		fe = int(first.split('-')[1]) + 1
 	else:
 		fs = int(first)
 		fe = int(first) + 1
 	if '-' in second:
 		ss = int(second.split('-')[0])
 		se = int(second.split('-')[1]) +1
 	else:
 		ss = int(second)
 		se = int(second) + 1
 	if '-' in third:
 		ts = int(third.split('-')[0])
 		te = int(third.split('-')[1]) + 1
 	else:
 		ts = int(third)
 		te = int(third) + 1
 	if '-' in fourth:
 		fos = int(fourth.split('-')[0])
 		foe = int(fourth.split('-')[1]) + 1
 	else:
 		fos = int(fourth)
 		foe = int(fourth) + 1
 	

	# making work, filling up the queue 	
	for j in range(fs, fe):
		for k in range(ss, se):
			for l in range(ts, te):
				for m in range(fos, foe):
					queue.put(str(j) + '.' + str(k) + '.' + str(l) + '.' +str(m))

	queue.join()

	print 'All tasks complete'

	f = open('targets.txt', 'w')

	for host in Alive:
		f.write(host)
	
	
	f.close()
	print 'Wrote ' + str(len(Alive)) + ' hosts to ./targets.txt'

if __name__ == '__main__':
	main()
