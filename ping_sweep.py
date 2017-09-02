#!/usr/bin/python3
import subprocess
for i in range(1,254):
    ip = '192.168.56.' + str(i)
    response = subprocess.call(['ping', '-c' ,'1','-W' ,'1',ip ],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    if (response == 0):
        print (ip)


