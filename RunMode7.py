#             Mode 7 Relay Control Program 
#                 Ken Fischer 06/2013 
# Controls 1 Relay based on input detection according to 
# specs described in Design Doc.  Relay is "flashed" 3 times 
# at a duty cycle passed into the program on the command line.
# If the parameters are not in range, a deafult is used.  The
# tripe "flashed" is exected "N" times, wher N is passed in,
# but must be between 1 and 5,  A Guard Timer is then executed
# to prevent the ringing from happening too frequently.
#
#  syntax:  mode2( R1, B1, T1, T2, T3, LC)
#  Input Parameters
#	R1)	ID of relay
#	B1)	ID Of Track/Button input
#       T1)     Pulse On time in miliseconds
#	T2)	Pulse Off time in miliseconds
#	T3)	Pause between cycles in seconds
#       LC)	Loop Count
#       GT)	Guard Time in seconds
##############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys



# Define the triple ring function:
def mode_7_triple_ring(pa1, pa2, pa3):
	ring_count = 3
	while (ring_count > 0): 
		relay_set(pa1, R_ON)
	    	time.sleep(pa2)
	    	relay_set(pa1, R_OFF)
	    	time.sleep(pa3)
	    	ring_count = ring_count - 1


# Define the looping function:
def mode_7_loop(p1, p2, p3, p4, p5, p6, p7):
    state = last_state = digitalRead(button_list[p2-1])
    if state == TRACK_OCCUPIED:	 
    	occupied_time = time.time()
	loop_ctr = p6
	while (loop_ctr > 0):
		mode_7_triple_ring(p1, p3, p4)
	    	time.sleep(p5)
	    	loop_ctr = loop_ctr - 1
    	ring_off_time = time.time()
	time.sleep(p7)  # sleep for at least guard time
	keep_looping = True
	while (keep_looping == True):
		time.sleep(0.02) # kill very little time
		state = digitalRead(button_list[p2-1]) # check input
		if state == TRACK_EMPTY:
			detect_time = time.time() # change detected
			keep_looping = False
	stopped_looping_time = time.time()
	print "time since start ", stopped_looping_time - occupied_time
	print "time relay on ", ring_off_time - occupied_time
	print "time relay held off ", stopped_looping_time - ring_off_time
    else:		# If its not occupied, turn off relay
    	relay_set(p1, R_OFF)
	time.sleep(.02)		# slow down the looping, but there
					# needs to be a better way 

# Start the loop:
# see if anything was passed in on the command line
parmcount = len(sys.argv)
if parmcount > 7: # less parms indicates imperfect pass
	rel = int(sys.argv[1])
	but = int(sys.argv[2])
	on_pulse = float(sys.argv[3])/1000.0
	off_pulse = float(sys.argv[4])/1000.0
	pause_time = int(sys.argv[5])
	ring_count = int(sys.argv[6])
	guard_time = int(sys.argv[7])
	print 'RunMode7 using command line input =', rel, but, on_pulse, off_pulse, pause_time, ring_count, guard_time
else:
	rel = 1
	but = 2
	on_pulse = 25/1000.0
	off_pulse = 200/1000.0
	pause_time = 1
	ring_count = 3
	guard_time = 15
	print 'RunMode7 using default parms =', rel, but, on_pulse, off_pulse, pause_time, ring_count, guard_time


#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
while (True):
	mode_7_loop(rel, but, on_pulse, off_pulse, pause_time, ring_count, guard_time)
      
