import OS
import time

a=1
while a<255:
	b=str(a)
	print"==========================================================="
	print "performing nmap of 192.168.1."+b
	os.system("nmap -T5 -n -sV -O 192.168.1."+b)
	a=a+1
	time.sleep(10)
	