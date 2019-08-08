##############################################################
#                 Ken Fischer 06/2013 
#             BootLoader Control Program 
# This program is executed on boot up of the BB.  It
# reads the 2 position dip switch to determine which 
# one of 4 main Opertating Modes to run the controler
# and then spawns the appropriate OpMode program.
#
#  syntax:  BootLoader()
#
##############################################################


# Import libraries including PyBBIO library:
from RelayCommonLib import *
import subprocess
import time
import sys

#
# Initialize the BeagleBone Relay Board
#
relay_bd_init()
#
# Read the 2 pins on the config dip switch
#
config0 = digitalRead(config_list[0])
config1 = digitalRead(config_list[1])
#
# Mimic the dip switch state on USR LEDs 3 and 4
#
time.sleep(30)
digitalWrite(USR2, config0)
digitalWrite(USR3, config1)
#
# Run one of 4 Sub-Processes to start the controller in the specificed mode (0-3)
#
if config0 == 0 and config1 == 0:
    print "Detected Operating Mode 0 "
    subprocess.Popen('/usr/bin/python /home/root/python-files/OpMode0.py >> /home/traincontrol/logs/OpMode0_Output.log', shell=True)
elif config0 == 1 and config1 == 0:
    print "Detected Operating Mode 1 "
    subprocess.Popen('/usr/bin/python /home/root/python-files/OpMode1.py >> /home/traincontrol/logs/OpMode1_Output.log', shell=True)
elif config0 == 0 and config1 == 1:
    print "Detected Operating Mode 2 "
    subprocess.Popen('/usr/bin/python /home/root/python-files/OpMode2.py >> /home/traincontrol/logs/OpMode2_Output.log', shell=True)
elif config0 == 1 and config1 == 1:
    print "Detected Operating Mode 3 "
    subprocess.Popen('/usr/bin/python /home/root/python-files/OpMode3.py >> /home/traincontrol/logs/OpMode3_Output.log', shell=True)
