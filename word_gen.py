#!/usr/bin/env python

import sys, os

def main():
	if len(sys.argv) != 3:
		print "usage " + sys.argv[0] + " <inputfile> <outputfile>"

	in_file = open(sys.argv[1], "r")
	out_file = open(sys.argv[2], "w")
	out_set = set()

	for word in in_file:
		upper_case(word, out_set)
		out_set = lower_case(out_set)
		out_set = cap_case(out_set)
		out_set = alter_case(out_set)
		out_set = dollar_at(out_set)
		out_set = leet(out_set)

	for word in out_set:
		out_file.write(word)
	
	in_file.close()
	out_file.close()

def upper_case(word, out_set):
	out_set.add(word.upper())

def lower_case(out_set):
	new_list = list(out_set)
	for word in new_list:
		out_set.add(word.lower())
	return out_set

def alter_case(out_set):
	new_list = list(out_set)
	for word in new_list:
		new_word = ''
		for letter in word:
			if letter.islower() == True:
				new_word += letter.upper()
			elif letter.isupper() == True:
				new_word += letter.lower()
			else:
				new_word += letter
		out_set.add(new_word)
	return out_set
	
def cap_case(out_set):
	new_list = list(out_set)
	for word in new_list:
		new_word = ''
		new_word += word[0].upper()
		new_word += word[1:].lower()
		out_set.add(new_word)
	return out_set

def dollar_at(out_set):
	new_list = list(out_set)
	for word in new_list:
		new_word = ''
		for letter in word:
			if letter.lower() == 'a':
				new_word += '@'
			elif letter.lower() == 's':
				new_word += '$'
			elif letter.lower() == 'o':
				new_word += '0'
			else:
				new_word += letter
		out_set.add(new_word)
	return out_set

def leet(out_set):
	new_list = list(out_set)
	for word in new_list:
		new_word = ''
		for letter in word:
			if letter.lower() == 'a':
				new_word += '4'
			elif letter.lower() == 'g':
				new_word += '6'
			elif letter.lower() == 'l':
				new_word += '1'
			elif letter.lower() == 's':
				new_word += '5'
			elif letter.lower() == 't':
				new_word += '7'
			elif letter.lower() == 'o':
				new_word += '0'
			else:
				new_word += letter
		out_set.add(new_word)
	return out_set
			

if __name__ == '__main__':
	main()



















