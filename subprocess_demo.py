#!/usr/bin/env python

import subprocess

# not usable in program?
print subprocess.call(['ls'])

# string
lines = subprocess.check_output(['ls'])

# make it a list
line_list = lines.split('\n')

print 'subprocess.check_output *******************'
for line in line_list:
	print line

output = subprocess.Popen('ls', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True)

print 'Popen output ******************'
print output.stdout.read()


