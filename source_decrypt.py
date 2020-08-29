#!/usr/bin/python3

import os
import binascii
import random

def divide_chunks(l, n):
    # looping till length l
    for i in range(0, len(l), n):
        yield l[i:i + n]

def extract_key(data):
    decoded_str = b'The following encoded individuals are to be given a $27.3k bonus'
    encoded_str = data[0:64]
    key = []
    for i in range(0, len(decoded_str)):
        key.append(decoded_str[i] ^ encoded_str[i])

    print(f'KEY : {key}')
    return key

def decrypt_otp(key, data):
    d = data
    otp = key
    print(f'OTP: {otp}\n')
    out = []
    for i in range(0, len(d)):
        out.append(d[i] ^ otp[i % len(otp)])
    return bytes(out)

# Read the lines from the file
data = b''
with open("./document.encrypted", "rb") as file:
    data = file.read()

print(f'OUT: {type(data)}\n{data}\n')

data = data.decode()
hex_lines = data.split('\n')

chunks = []
encrypt = b''
for hex_line in hex_lines:
    chunks.append(binascii.unhexlify(hex_line))
    encrypt += binascii.unhexlify(hex_line)

print(f'DIVIDE_CHUNKS: {type(chunks)}\n{chunks}\n')

print(f'ENCRYPT: {type(encrypt)}\n{encrypt}\n')

key = extract_key(encrypt)

doc = decrypt_otp(key, encrypt)

print(f'DOC: {type(doc)}\n{doc}')


