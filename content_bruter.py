#!/usr/bin/env python

import urllib2
import threading
import Queue
import urllib

threads = 20
target_url = "http://192.168.1.116"
wordlist_file = "/home/jonathan/wordlists/all.txt"
resume = None
user_agent = "User-Agent=Mozilla/5.0 (X11; Linux x86_64; rv:31.0) Gecko/20100101 Firefox/31.0 Iceweasel/31.4.0"

def build_wordlist(wordlist_file):
	f = open(wordlist_file, "r")
	raw_words = f.readlines()
	f.close()

	found_resume = False
	words = Queue.Queue()
	for word in raw_words:
		word = word.rstrip()
		if resume != None:
			if found_resume:
				words.put(word)
			else:
				if word == resume:
					found_resume = True
					print "Resuming wordlist from %s." % resume
		else:
			words.put(word)
	return words

def dir_bruter(word_queue, extensions=None):
	while not word_queue.empty():
		attempt = word_queue.get()
		attempt_list = []
		# check to see if there is a file extension, if
		# not we are bruting a directory
		if "." not in attempt:
			attempt_list.append("/%s/" % attempt)
		else:
			attempt_list.append("/%s" % attempt)
		# if we want to brute force extensions
		if extensions:
			for extension in extensions:
				attempt_list.append("/%s%s" % (attempt, extension))
		for brute in attempt_list:
			# urllib.quote encodes special characters such as a space
			url = "%s%s" % (target_url, urllib.quote(brute))
			try:	
				headers = {}
				headers['User-Agent'] = user_agent
				req = urllib2.Request(url, headers=headers)
				resp = urllib2.urlopen(req)
				if len(resp.read()):
					print "[%d] --> %s" % (resp.code, url)
			except urllib2.URLError, e:
				if hasattr(e, 'code') and e.code != 404:
					print "[!!!] %d --> %s" % (e.code, url)
				pass
word_queue = build_wordlist(wordlist_file)
extensions = [".php", ".bak", ".orig", ".inc"]

for i in range(threads):
	t = threading.Thread(target=dir_bruter, args=(word_queue, extensions))
	t.start()













