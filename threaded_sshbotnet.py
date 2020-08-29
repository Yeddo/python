#!/usr/bin/env python

import threading
import Queue
import pxssh

# create a new class as a subclass of threading.Thread
class workerthread(threading.Thread):
	def __init__(self, bot_q, command_q):
		# calling the threading.Thread class (parent class) __init__ method
		threading.Thread.__init__(self)
		# adding the queue attribute, passed to object when created
		self.bot_q = bot_q
		self.command_q = command_q
	
	# when worker.start() is called, run() is executed, putting the thread to work	
	def run(self):
		task = self.bot_q.get()
		
		ip = task.split(':')[0]
		username = task.split(':')[1]
		password = task.split(':')[2]

		try:
			child = pxssh.pxssh()
			print 'IP address: ' + ip + '\n' + str(child.before)
			child.login(ip, username, password)
			self.bot_q.task_done()
			print '[+] ' + username + '@' + ip + ' online.'
			try:
				while True:
					command = self.command_q.get()
					child.sendline(command)
					if 'sudo' in command:
						try:
							print 'in sudo'
							ret = child.expect(['assword:', '#'])
							if ret == 0:
								child.sendline(password)
								print 'password sent'
							elif ret == 1:
								print 'password not required'
						except Exception, e:
							print 'sudo error ' + ip
							print e
					child.prompt()		
					print '[*] Output for IP Address: ' + str(ip)
					print child.before

			except:
				print'[-] Error processing command for IP Address: ' + str(ip)
			finally: 
				self.command_q.task_done()
			
		except Exception, e:
			print '[-] Error logging in to IP Address: ' + str(ip)
			print e
			self.bot_q.task_done()
			



def main():
	# creating an object of the queue class
	bot_q = Queue.Queue()
	command_q = Queue.Queue()

	botlist = open('files/rangehost.txt').readlines()

	# creating threads to execute tasks
	for i in range(len(botlist)):
		worker = workerthread(bot_q, command_q)
		worker.setDaemon(True)
		worker.start()
					
	for bot in botlist:
		bot_q.put(bot)
	bot_q.join()
	while True:
		command = raw_input('Input command\n')
		for bot in range(len(botlist)):
			command_q.put(command)


	print 'All tasks complete'

if __name__ == '__main__':
	main()
