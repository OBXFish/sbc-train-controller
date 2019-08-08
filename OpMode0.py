#             Operating Mode 0 Progrm:w
#                 Ken Fischer 06/2013 
#
# This is the primary control program for operating the
# relay board.  This reads the config file, and spawns
# one process per installed relay, starring the RunMode
# type specified in the config file.  Those processes
# will run until reboot
#
#  syntax:  OpMode0()
#  Input Parameters:  None
#
#############################################################

# Import libraries including PyBBIO library:
from RelayCommonLib import *
import subprocess
import time
import sys

print 'OpMode0 started execution ', time.asctime() 
#
# Initialize the I/O and other aspects of the program
#
relay_bd_init()
# read the number of relays in the device here
config_data = [line.rstrip('\n') for line in open("/home/traincontrol/RunTimeConfigs/relay.config")]
relay_count = int(config_data[0])
#
# For each line in the config file, spawn the appropriate RunMode code
#
for index in range (0, relay_count, 1):	
    pgm_string  = '/usr/bin/python /home/root/python-files/RunMode' + config_data[index+1][0] + '.py '
    parm_string = config_data[index+1][2:]
    pipe_string = ' > /home/traincontrol/logs/OpMode0_Relay_' + str(index+1) + '_Output.log'
    command_string = pgm_string + parm_string + pipe_string
    print 'spawning process: ', command_string
    subprocess.Popen( command_string, shell=True)
    time.sleep(.1)
