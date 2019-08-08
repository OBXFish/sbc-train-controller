#             Mode 6 Relay Control Program 
#                 Ken Fischer 06/2013 
# Controls 1 Relay based on input detection according to 
# specs described in Design Doc.  Relay is turned on for 
# a an exact amont of time when detection occurs, but is
# then locked out first for a minimum time (settable).
# If the train is in the track after the guard-time, the
# relay goes back on for the specified time.  Unlike 
# Mode 5, repeating is allowed
#
#  syntax:  mode6( R1, B1, ON_TIME, GUARD_TIME)
#  Input Parameters
#	R1)	ID of relay
#	B1)	ID of the "button" to test 
#	ON_TIME) The minimum time to hold the relay on
#	GUARD_TIME)  Time to lock out button
#
############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys
																				   
# Define the main looping function for this mode:
def mode_6_loop(p1, p2, p3, p4):
	state = last_state = digitalRead(button_list[p2-1])
	digitalWrite(USR3, state)
	while (state == TRACK_OCCUPIED):	# If track is occupied, 
		on_time = c_time = d_time = time.time()
		relay_set(p1, R_ON)
		time.sleep(p3)
		relay_set(p1, R_OFF)
		off_time = time.time()
		time.sleep(p4)
		state = digitalRead(button_list[p2-1])
	else:		# If its not occupied, turn off relay
		relay_set(p1, R_OFF)
		time.sleep(.02)		# slow down the looping, but there
					# needs to be a better way 


# Start the loop:
# see if anything was passed in on the command line
parmcount = len(sys.argv)
if parmcount >= 5: # less parms indicates imperfect pass
	rel = int(sys.argv[1])
	but = int(sys.argv[2])
	on_time = int(sys.argv[3])
	guard_time = int(sys.argv[4])
	print 'RunMode6 using command line input =',rel, but, on_time, guard_time
else:
	rel = 1
	but = 1
	on_time = 5
	guard_time =  10
	print 'RunMode6 using default parameters =',rel, but, on_time, guard_time
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
while (True):
	mode_6_loop(rel, but, on_time, guard_time)
      
