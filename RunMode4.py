#             Mode 4 Relay Control Program 
#                 Ken Fischer 06/2013 
# Controls 1 Relay based on input detection according to 
# specs described in Design Doc.  Relay is turned on for 
# a minimum amount of time as soon as the input is on.
# This minimum time includes the Off-Delay paremter
# which is passed in as well as the minimum time.
# so, the relay will be on for the loger of the
# minimum time, or the time the input is held on
# plus the Off-Delay timer.
#
#  syntax:  mode4( R1, B1, MIN_TIME, OFF_DELAY)
#  Input Parameters
#	R1)	ID of relay
#	B1)	ID of the "button" to test on the input side
#	MIN_TIME) The minimum time to hold the relay on
#	OFF_DELAY)  Time in seconds to wait till turn-off
#
#############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys

# Define the looping function:
def mode_4_loop(p1, p2, p3, p4):
	state = last_state = digitalRead(button_list[p2-1])
	digitalWrite(USR3, state)
	if state == TRACK_OCCUPIED:	# If track is occupied, 
		relay_set(p1, R_ON)
		s_time = t_time = time.time()
		keep_looping = True
		while (keep_looping == True):
			time.sleep(0.02) # kill very little time
			state = digitalRead(button_list[p2-1]) # check input
			c_time = time.time()
			if state == TRACK_EMPTY:
				if last_state == TRACK_OCCUPIED:
					t_time = time.time() # time first change was detected
					last_state = not TRACK_OCCUPIED
					time.sleep(p4)
				if c_time > s_time + p3:
					keep_looping = False
		e_time = time.time()
		#print "time since start", e_time - s_time
		#print "time track occupied", t_time - s_time
		#print "time since track empty", e_time - t_time
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
	min_time = int(sys.argv[3])
	off_del = int(sys.argv[4])
	if min_time < off_del:
		min_time = off_del
	print 'RunMode4 using command line input =',rel, but, min_time, off_del
else:
	rel = 1
	but = 1
	min_time = 1
	off_del =  5
	print 'RunMode4 using command line input =',rel, but, min_time, off_del
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
while (True):
	mode_4_loop(rel, but, min_time, off_del)
      
