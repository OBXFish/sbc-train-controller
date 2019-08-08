#             Operating Mode 2 Progrm:w
#                 Ken Fischer 06/2013 
#
# One of 4 main control programs for operating the relay
# board.  This one is one of 2 "normal" operating modes.
# This mode spawns one process per installed relay, and
# a relay is on when its input is on, and off when its not.
# The main purpose of this mode is to verify that the 
# the controller is working, and to allow each accessory
# to be tested by pressing its button, or putting a car
# on the appropriate track
#
#  syntax:  OpMode2()
#  Input Parameters:  None
#
#############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import subprocess
import time
import sys

print 'OpMode2 started execution ', time.asctime() 
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
# read the number of relays in the device here
config_data = [line.rstrip('\n') for line in open("/home/traincontrol/RunTimeConfigs/relay.config")]
relay_count = int(config_data[0])
print "Relay Count ", relay_count
#
# For each line in the config file, spawn a copy of RunMode3
#
for index in range (0, relay_count, 1):	
    pgm_string  = '/usr/bin/python /home/root/python-files/RunMode3.py '
    parm_string = config_data[index+1][2] + ' ' + config_data[index+1][4]
    pipe_string = ' >> /home/traincontrol/logs/OpMode2_Relay_' + str(index+1) + '_Output.log'
    command_string = pgm_string + parm_string + pipe_string
    print 'spawning process: ', command_string
    subprocess.Popen(command_string, shell=True)
    time.sleep(.1)
