import sys
import pexpect
import os

# setting current users home dir to 'home' because for some reason '~' doesn't work... wtf
home = os.getenv('HOME')

def writeHash():
	hFile = open(home + '/hashes.txt', 'w')
	print 'Please paste the hashes you would like to decrypt, then press <ctrl> + d:'
	# Write one line at a time so newlines are recognized, not just a block of crap
	for line in sys.stdin.readlines():
		hFile.write(line)
	hFile.write('\n')
	hFile.close()

def john():
	pot = open(home + '/.john/john.pot', 'w')
	pot.close()
	log = open(home + '/.john/john.log', 'w')
	log.close()
	dictionary = raw_input('\nWhat dictionary would you like to use?\n')
	child = pexpect.spawn('john --wordlist=' + dictionary + ' ' + home + '/hashes.txt')
	child.expect('guesses:')
	# 'passwords' is everything between spawning 'john' and the string match 'guesses:' 
	# formatted as a string then split into a list on every instance of '\n'
	passwords = child.before.split('\n')
	print '\n------------------------------------------'
	print '|    Cracked the following passwords:    |'
	print '------------------------------------------'
	# Used slicing to start at the 4th item in passwords because the first 3 items
	# are a bunch of crap I don't care about
	for line in passwords[3::]:
		print line
	
def main():
	writeHash()
	john()

main()


	
