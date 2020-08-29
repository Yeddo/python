inputfile = open('malware', 'rb')
outputfile = open('decode', 'w+b')
byte = inputfile.read(1)
counter = 0
while byte != "":
	byte = ord(byte)
	if counter % 2 == 1:
		byte = byte ^ 0x33
	outputfile.write('%c' % byte)
	byte = inputfile.read(1)
	counter += 1
outputfile.close()