#!/usr/python
##################################################################
############ To make a beep after every 2 seconds. ###############
########## Frequency set to 1000 #################################
############ sudo apt install sox ################################
import os
import time
while True:
    os.system('play --no-show-progress --null --channels 1 synth %s sine %f' % ( 0.25, 1000))
    ############################################################################(beep period, frequency)
    time.sleep(10)

