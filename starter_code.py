#!/usr/bin/python3
import argparse
import socket
import re
import base64
import binascii
​
str_break = '-------------------------------------------------------------------'
str_conversion = '->'
​
def decode_data(type_data, data):
    '''Decode data to string'''
    output = ''
​
    if 'raw' in type_data:
        pass
    elif 'b64' in type_data:
        print("DECODE: B64")
        output = base64.b64decode(data).decode("utf-8")
    elif 'hex' in type_data:
        print("DECODE: HEX")
        output = bytes.fromhex(data).decode("utf-8")
    elif 'oct' in type_data:
        print("DECODE: OCT")
        output = binascii.unhexlify(hex(int(data, base=8))[2:]).decode("utf-8")
    elif 'dec' in type_data:
        print("DECODE: DEC")
        output = binascii.unhexlify(hex(int(data, base=10))[2:]).decode("utf-8")
    elif 'bin' in type_data:
        print("DECODE: BIN")
        output = binascii.unhexlify(hex(int(data, base=2))[2:]).decode("utf-8")
    else:
        print(f'ERROR: Unknown decode type {type_data}')
​
    if 'binary' == type(output) :
        output = binascii.a2b_uu(output)
​
    return(output)
​
def encode_data(type_data, data):
    '''Decode data to string'''
    output = ''
​
    if 'raw' in type_data:
        output=data
    elif 'b64' in type_data:
        print("ENCODE: B64")
        output = base64.b64encode(data.encode("utf-8")).decode("utf-8")
    elif 'hex' in type_data:
        print("ENCODE: HEX")
        output = binascii.hexlify(data.encode())
    elif 'oct' in type_data:
        print("ENCODE: OCT")
        output = int(binascii.hexlify(data.encode()), base=16)
        output = oct(output)[2:]
    elif 'dec' in type_data:
        print("ENCODE: DEC")
        output = str(int(binascii.hexlify(data.encode()), base=16))
    elif 'bin' in type_data:
        print("ENCODE: BIN")
        output = int(binascii.hexlify(data.encode()), base=16)
        output = bin(output)[2:].decode("utf-8")
    else:
        print(f'ERROR: Unknown encode type {type_data}')
​
    return(output)
​
# 'argparse' is a very useful library for building python tools that are easy
# to use from the command line.  It greatly simplifies the input validation
# and "usage" prompts which really help when trying to debug your own code.
parser = argparse.ArgumentParser(description="Solver for 'All Your Base' challenge")
parser.add_argument("ip", help="IP (or hostname) of remote instance")
parser.add_argument("port", type=int, help="port for remote instance")
args = parser.parse_args();
​
# This tells the computer that we want a new TCP "socket"
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
​
# This says we want to connect to the given IP and port
sock.connect((args.ip, args.port))
​
# This gives us a file-like view for receiving data from the connection which
# makes handling messages from the server easier since it handles the
# buffering of lines for you.  Note that this only helps us on receiving data
# from the server and we still need to send data over the underlying socket
# (i.e. `sock.send(...)` at the end of the loop below).
f = sock.makefile()
​
while True:
    line = f.readline().strip()
    # This iterates over data from the server a line at a time.  This can
    # cause some unexpected behavior like not seeing "prompts" until after
    # you've sent a reply for it (for example, you won't see "answer:" for
    # this problem). However, you can still "sock.send" below to transmit data
    # and the server will handle it correctly.
​
    if len(line) == 0 :
        continue
​
    elif str_break in line :
        print(f'Server: {line}')
        line = f.readline().strip()
​
        if str_conversion in line:
            type_input, type_output = tuple(line.split('->'))
            print(f'Server: {line}')
            data = f.readline().strip()
            print(f'Server: {data}')
​
            output = decode_data(type_input, data)
            print(f'DECODE: {output}')
            output = encode_data(type_output,output)
​
            print(f'ENCODE: {output}')
            # Send a response back to the server
            sock.send((output + "\n").encode()) # The "\n" is important for the server's
                                                # interpretation of your answer, so make
                                                # sure there is only one sent for each
                                                # answer.
    else :
        print(f'Server: {line}')
​
​
    # Handle the information from the server to extact the problem and build
    # the answer string.
    #pass # Fill this in with your logic
    # A good starting point for approaching the problem:
    #   1) Identify and capture the text of each question (the "----" lines
    #          should be useful for this).
    #   2) Extract the three primary parts of each question:
    #      a) The source encoding
    #      b) The destination encoding
    #      c) The source data
    #   3) Convert the source data to some "standard" encoding (like 'raw')
    #   4) Convert the "standardized" data to the destination encoding