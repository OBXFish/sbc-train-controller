#             Mode 1 Relay Control Program 
#                 Ken Fischer 06/2013 
# Control 2 Relays based on input detection according to 
# specs described in Design Doc.  Relay 1 is held ON after
# detection of input.  Relay 2 is cycled on and off at a 
# rate per minute passed into the program
#
#  syntax:  mode1( R1, R2, B1, F_RATE, OFF_DELAY)
#  Input Parameters
#	R1)	ID of first relay
#	R2)	ID of second relay
#	B1)	ID of Button/Track
#	F_RATE)	Rate per minute of flashes (20, 30, 60 etc)
#	OFF_DELAY)  Tme to keep lights flashing after off
#
# Code implements a delayed-off time that is defined locally,
# but will eventually have a global setting for all relays
#
###############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys

# Define the looping function:
def mode_1_loop(p1, p2, p3, p4, p5):
    state = digitalRead(button_list[p3-1])
    digitalWrite(USR3, state)
    if state == TRACK_OCCUPIED:	# If track is occupied, then execute the Mode-1 logic.
	relay_set(p1, R_ON)
	relay_set(p2, R_ON)
	relay_2_state = R_ON
	min_time = 0
	keep_looping = True
	while (keep_looping == True):
	    time.sleep(60.0/p4)
	    relay_2_state = not relay_2_state
	    relay_set(p2, relay_2_state)
	    state = digitalRead(button_list[p3-1])
	    digitalWrite(USR3, state)	# mimic on  USR3
	    if state == TRACK_EMPTY and min_time == 0:
	        min_time = time.time() # start exit process, paying attention to timers
	    if min_time != 0:
	        max_time = time.time()
		if max_time > min_time + p5:
		    keep_looping = False
	            relay_set(p1, R_OFF)
    else:		# If its not occupied, turn off both relays
        relay_set(p1, R_OFF)
	relay_set(p2, R_OFF)
	time.sleep(.02)		# slow down the looping, but there

# Start the loop:
# see if anything was passed in on the command line
parmcount = len(sys.argv)
if parmcount >= 6: # less parms indicates imperfect pass
	rel1 = int(sys.argv[1])
	rel2 = int(sys.argv[2])
	but  = int(sys.argv[3])
	f_rate = int(sys.argv[4])
	if f_rate > 120:
		f_rate = 120	# faster is too fast
	off_del = int(sys.argv[5])
	print 'RunMode1 using command line input =',rel1, rel2, but, f_rate, off_del
else:
	rel1 = 1
	rel2 = 2
	but = 1
	f_rate = 60
	off_del = 5
	print 'RunMode1 using default parameters =',rel1, rel2, but, f_rate, off_del
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
while (True):
       	mode_1_loop(rel1, rel2, but, f_rate, off_del)
      
