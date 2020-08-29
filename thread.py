#!/usr/bin/env python

import thread
import time
import random

Lock = thread.allocate()
Count = 1
X = random.Random()


def workerthread(id):
	global Count
	global X
	while True:
		try:
			if Lock.locked():
				print 'Thread ID %d just got lock blocked' %id
				time.sleep(1)
			else:
				Lock.acquire()
				print 'Thread ID %d acquired the lock' %id
				Count += 1
				print "Thread ID %d updated counter value to %d" %(id, Count)
				nap = X.randint(1,5)
				print 'Thread ID %d taking a nap with the lock for %d seconds' %(id, nap)
				time.sleep(nap)
				Lock.release()
				print 'Thread ID %d released the lock' %id
				time.sleep(X.randint(1,5))
		except Exception, e:
			print e
			continue
		
# start 5 threads		
for i in range(5):
	thread.start_new_thread(workerthread, (i,))
	
# allows program to continue running while workerthreads 
while True:
	pass
