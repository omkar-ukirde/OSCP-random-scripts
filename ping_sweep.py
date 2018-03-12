from commands import getoutput
from multiprocessing import Process
def pingdef(ping):
	address = "192.168.0." + str(ping)
	line = getoutput("ping -n -c 1 -w 1 %s 2>/dev/null" % address)
	if ('100% packet loss') not in line:
		print address
		
for ping in range(1,254):
	pingone = Process(target=pingdef,args=(ping,))
	pingone.start()   
	 
