#             Relay Common Library 
#             Ken Fischer 09/2013 
# This file contains common constants and routines used
# by all the Python modules for the train controller.
#
# Funcitons defined here
#     train_cti_init()  initializes inputs and outputs
#     relay_set()	sets a defined relay to a given state
#
################################################################

#
#	import BBIO Libraries
#
from bbio import *
import signal

#
# Define the GPIO PINs for relays and detectors
#
CONFIG1 = GPIO1_30
CONFIG2 = GPIO1_4
LED_1 = GPIO1_15
LED_2 = GPIO0_27
BUTTON1 = GPIO2_12
BUTTON2 = GPIO2_10
BUTTON3 = GPIO2_8
BUTTON4 = GPIO2_6
REL_1 = GPIO1_6
REL_2 = GPIO1_2
REL_3 = GPIO1_14
REL_4 = GPIO2_1
config_list = [CONFIG1, CONFIG2]
led_list = [LED_1, LED_2]
relay_list = [REL_1, REL_2, REL_3, REL_4]
button_list = [BUTTON1, BUTTON2, BUTTON3, BUTTON4]

#
# define important constants
#
R_ON	= 0
R_OFF	= 1
TRACK_OCCUPIED 	= 0	#logic seems reversed: pin pulled low when occupied
TRACK_EMPTY	= 1	#logic seems reversed: pin pulled high when empty

#
# Define Exit handling routine
#
def relay_term_handler(p1,p2):
	for x in relay_list:	# turn off all relays
		digitalWrite(x, R_OFF)
		time.sleep(.02)
	bbio_cleanup()
	print 'System Shutting down, cleanup complete'
	exit()

#
# Function to Initialize GPIO pins:
#
def relay_bd_init():
	#  Set up Exception Handler Traps
	signal.signal(signal.SIGTERM, relay_term_handler)
	signal.signal(signal.SIGINT, relay_term_handler)
	#  Initialize BBIO Libraries
	bbio_init()
	for x in config_list:	# set config pins to input
		pinMode(x, INPUT)
		time.sleep(.05)
	for x in button_list:	# set all buttons to input
		pinMode(x, INPUT)
		time.sleep(.05)
	for x in led_list:	# set all leds to output
		pinMode(x, OUTPUT)
		time.sleep(.05)
	for x in led_list:	# turn off all leds
		digitalWrite(x, R_OFF)
		time.sleep(.05)   
	for x in relay_list:	# set all relays to output
		pinMode(x, OUTPUT)
		time.sleep(.05)
	for x in relay_list:	# turn off all relays
		digitalWrite(x, R_OFF)
		time.sleep(.05)
									   
#
# Define Relay Setting Routine
#
def relay_set(r_number, rstate):
	digitalWrite(relay_list[r_number-1], rstate)

