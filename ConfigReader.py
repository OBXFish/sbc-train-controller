#             ConfigReader Control Program 
#                 Ken Fischer 06/2013 
#
# When executed, this program reads the Config dip switches,
# mimics them on the User LEDs, and writes the current setting to
# stdout.  It loops indefintely, reading the settings and writing
# output.  
#
#  syntax:  ConfigReader()
#
##############################################################


# Import libraries including PyBBIO library:
from RelayCommonLib import *
import time
import sys

relay_bd_init()
last_state = this_state = 5
# Loop Forever, reading the pins, and mimicing them on the LEDs
while (True):
    #
    # Read the 2 pins on the config dip switch
    #
    config0 = digitalRead(config_list[0])
    config1 = digitalRead(config_list[1])
    #
    # Mimic the dip switch state on USR LEDs 3 and 4
    #
    digitalWrite(USR2, config0)
    digitalWrite(USR3, config1)
    if config0 == 0 and config1 == 0:
        this_state = 0
	if this_state != last_state:
	    last_state = this_state
	    print "Detected Operating Mode: ", this_state
    elif config0 == 1 and config1 == 0:
        this_state = 1
	if this_state != last_state:
	    last_state = this_state
	    print "Detected Operating Mode: ", this_state
    elif config0 == 0 and config1 == 1:
        this_state = 2
	if this_state != last_state:
	    last_state = this_state
	    print "Detected Operating Mode: ", this_state
    elif config0 == 1 and config1 == 1:
        this_state = 3
	if this_state != last_state:
	    last_state = this_state
	    print "Detected Operating Mode: ", this_state
    time.sleep(1) 
