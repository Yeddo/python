#!/usr/bin/env python3


pw = input('Please enter the password:\n')

key = ''

for letter in pw:
	key += format(ord(letter), '08b')

while True:
	text = input('Please enter the text you would like to encrypt/decrypt:\n')
	
	bin_text = ''
	for letter in text:
		bin_text += format(ord(letter), '08b')
	
	ks = ''
	while len(ks) < len(bin_text):
		ks += key
	ks = ks[0:len(bin_text)]

	encrypt_data = format(int(ks, 2) ^ int(bin_text, 2), 'b')
	while len(encrypt_data) != len(ks):
		encrypt_data = '0' + encrypt_data
	print('Here is your encrypted binary:\n')
	print(encrypt_data + '\n')
