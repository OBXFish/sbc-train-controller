#             
#             Operating Mode 3 Progrm:w

#                 Ken Fischer 06/2013 
# One of 4 main control programs for operating the relay
# board.  This one is one of 2 test mode programs that 
# are initiated when certain dip switch settings are 
# detected on boot-up.  The program clicks on each relay
# in sequential order for a set number of times, based
# on which relay it is, then repeats until reset.  For
# example, relay 1 is clicked once; relay 2 is clicked
# twice, relaye 3: 3 times etc.  This goes on forever.
#
#  syntax:  OpMode3()
#  Input Parameters:  None
#
#############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys

print 'OpMode3 started execution ', time.asctime() 
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
while (True):
    # read the number of relays in the device here
    config_data = [line.rstrip('\n') for line in open("/home/traincontrol/RunTimeConfigs/relay.config")]
    relay_count = int(config_data[0])
    print "Relay Count = ", relay_count
    next_relay = 0
    for index1 in range (1, relay_count+1, 1):	
	next_relay = next_relay +1
	for index2 in range (0, next_relay, 1):
	    digitalWrite(relay_list[next_relay-1], R_ON)
	    digitalWrite(USR3, 1)
            time.sleep(3)
	    digitalWrite(relay_list[next_relay-1], R_OFF)
	    digitalWrite(USR3, 0)
            time.sleep(2)
        time.sleep(1)


