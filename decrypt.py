#!/usr/bin/env python3

pw = input('Please enter the password:\n')

key = ''

for letter in pw:
	    key += format(ord(letter), '08b')

while True:
	encrypt_data = input('Please enter the binary you would like to decrypt:\n')

	ks = ''
	while len(ks) < len(encrypt_data):
		ks += key
	ks = ks[0:len(encrypt_data)]

	decrypt_data = format(int(encrypt_data, 2) ^ int(ks, 2), 'b')

	while len(decrypt_data) != len(encrypt_data):
		decrypt_data = '0' + decrypt_data

	x = 0
	y = 8

	decrypt_text  = ''

	while y <= len(decrypt_data):
		decrypt_text += chr(int(decrypt_data[x:y], 2))
		x += 8
		y += 8

	print('Here is you encrypted/decrypted text:\n')
	print(decrypt_text + '\n')

