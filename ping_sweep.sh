#!/bin/bash
for i in `seq 10 18`;
do 
	ping 192.168.56.$i -c 1 -W 1 >/dev/null && echo 192.168.56.$i
done	
