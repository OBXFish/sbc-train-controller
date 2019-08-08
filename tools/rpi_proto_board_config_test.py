#             ProtoBoardTest Program 
#                 Ken Fischer 06/2013 
#
# modified from BeagleBone Python to Raspbery Pi for Testing
#
# This program reads the 2 dip switches on the Proto Board
# and mimics the state on the 2 LEDs that are on the board.
#
##############################################################


# Import libraries including PyBBIO library:
from RelayCommonLib import *
import subprocess
import time
import sys

# initialize the GPIO Libraries
relay_bd_init()
#
# Loop forever, Reading the 2 pins on the config dip switch
# and writing the state to the 2 LEDs
#
while(True):
  config0 = digitalRead(config_list[0])
  config1 = digitalRead(config_list[1])
  digitalWrite(LED_1, config0)
  digitalWrite(LED_2, config1)
  if config0 == 0 and config1 == 0:
    print "Detected Operating Mode 0 "
  elif config0 == 1 and config1 == 0:
    print "Detected Operating Mode 1 "
  elif config0 == 0 and config1 == 1:
    print "Detected Operating Mode 2 "
  elif config0 == 1 and config1 == 1:
    print "Detected Operating Mode 3 "
  time.sleep(2)
