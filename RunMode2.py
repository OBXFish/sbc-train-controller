#             Mode 2 Relay Control Program 
#                 Ken Fischer 06/2013 
# Controls 1 Relay based on input detection according to 
# specs described in Design Doc.  Relay is flashed at a 
# rate per minute that is passed into the program on the
# command line, as long as its less than 120 times per 
# minute.  The relay is flashed until the input transitions
# low, and an additional OFF_DELAY seconds have passed
#
#  syntax:  mode2( R1, B1, F_RATE, OFF_DELAY)
#  Input Parameters
#	R1)	ID of relay
#	B1)	ID Of Track/Button input
#	F_RATE)	Rate per minute of flashes (20, 30, 60 etc)
#	OFF_DELAY)  Time in seconds to wait till turn-off
#
##############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys
																				   
# Define the looping function:
def mode_2_loop(p1, p2, p3, p4):
    state = digitalRead(button_list[p2-1])
    digitalWrite(USR3, state)
    if state == TRACK_OCCUPIED:	 
	relay_set(p1, R_ON)
	relay_state = R_ON
	min_time = 0
	keep_looping = True
	while (keep_looping == True):
	    relay_state = not relay_state
	    time.sleep(60.0/p3)
	    relay_set(p1, relay_state)
	    state = digitalRead(button_list[p2-1])
	    digitalWrite(USR3, state)	# mimic on  USR3
	    if state == TRACK_EMPTY and min_time == 0:
		min_time = time.time()	# start exit process, paying attention to timers
	    if min_time != 0:
	        max_time = time.time()
		if max_time > min_time + p4:
		    keep_looping = False
    else:
	relay_set(p1, R_OFF)
	time.sleep(.02)		# slow down the looping


# Start the loop:
# see if anything was passed in on the command line
parmcount = len(sys.argv)
if parmcount >= 5: # less parms indicates imperfect pass
	rel = int(sys.argv[1])
	but = int(sys.argv[2])
	f_rate = int(sys.argv[3])
	if f_rate > 120:
		f_rate = 90	# faster is too fast
	off_del = int(sys.argv[4])
	print 'RunMode2 using command line input =',rel, but, f_rate, off_del
else:
	rel = 1
	but = 1
	f_rate = 60
	off_del = 5
	print 'RunMode2 using default parameters =',rel, but, f_rate, off_del
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
while (True):
	mode_2_loop(rel, but, f_rate, off_del)
      
