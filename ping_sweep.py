import subprocess
import os

FNULL = open(os.devnull, 'w')
for ping in range(1,25):
	address = "192.168.0." + str(ping)
	res = subprocess.call(['ping', '-c', '1','-w','1', address] ,stdout=FNULL, stderr=FNULL)
	if res == 0:
      		print address
   
