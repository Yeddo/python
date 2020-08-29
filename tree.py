#!/usr/bin/env python

import os


startDir = os.getcwd()

for root, dirs, files in os.walk(startDir):
	fileDepth = (len(root.split('/')) - len(startDir.split('/'))) * '---'
	dirDepth = (len(root.split('/')) - len(startDir.split('/')) - 1) * '---'

	if root != '.' and root != startDir:
		print dirDepth + root.split('/')[len(root.split('/')) - 1].upper() + '/'
	for file in files:
		print fileDepth + file.lower()
	
