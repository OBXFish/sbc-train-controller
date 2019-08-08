#             Mode 3 Relay Control Program 
#                 Ken Fischer 06/2013 
# Controls 1 Relay based on input detection according to 
# specs described in Design Doc.  Relay turns on when  
# input is on, and off when input is off.  Detecor is 
# debounced, but no minimum or maximum time is enforced
#
#  syntax:  mode3(R1, B1)
#  Input Parameters
#	R1)	ID of relay
#	B1)	ID of Detector/Button
#
##############################################################


# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys

# Define the looping function:
def mode_3_loop(p1, p2):
    state = digitalRead(button_list[p2-1])
    digitalWrite(USR3, state)
    if state == TRACK_OCCUPIED:	 
	relay_set(p1, R_ON)
    else:		
	relay_set(p1, R_OFF)
    time.sleep(.1)	# slow down the looping
			# Is there a better way? 

# Start the loop:
# see if anything was passed in on the command line
parmcount = len(sys.argv)
if parmcount >= 3: # less parms indicates imperfect pass
	rel = int(sys.argv[1])
	but = int(sys.argv[2])
	print 'RunMode3 using command line input =', rel, but
else:
	rel = 1
	but = 1
	print 'RunMode3 using default parameters =', rel, but
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
while (True):
	mode_3_loop(rel, but)
      
