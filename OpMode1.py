#             
#             Operating Mode 1 Progrm:w

#                 Ken Fischer 06/2013 
# One of 4 main control programs for operating the relay
# board.  This one is one of 2 test mode programs that 
# are initiated when certain dip switch settings are 
# detected on boot-up.  The program turns each relay on
# in sequential order for 10 seconds. This goes on forever.
#
#  syntax:  OpMode1()
#  Input Parameters:  None
#
#############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys

#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
print 'OpMode1 started execution ', time.asctime() 
while (True):
    # read the number of relays in the device here
    config_data = [line.rstrip('\n') for line in open("/home/traincontrol/RunTimeConfigs/relay.config")]
    relay_count = int(config_data[0])
    for index1 in range (0, relay_count, 1):	
	digitalWrite(relay_list[index1], R_ON)
	digitalWrite(USR3, 1)
        time.sleep(5)
	digitalWrite(relay_list[index1], R_OFF)
	digitalWrite(USR3, 0)
        time.sleep(1)
# NEED TO CLOSE UP FILES ON EXIT?  OPEN CONFIG IN COMMON?


