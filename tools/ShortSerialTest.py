#! /usr/bin/env python    #RM- added this, got the impression it is a good idea for finding things o execute
#################################################################
# This is a shortened re-code of Rob;'s Propeller script that   #
# exercises the LED Matrix                                      #
#################################################################


# Include external function calls
import threading
import time
import sys
import serial  # RM- I uncommented this

# init UART1 on the BeagleBone default br=19200, max 115200 bps, 8N1, no parity    RM- added this init stuff
# UART1, MODE=O
RX_MUX = 'uart1_rxd'
TX_MUX = 'uart1_txd'
MUX_MODE = 0
RECEIVE_ENABLE = 32
TRANSMIT_ENABLE = 0
ser = serial.Serial('/dev/ttyO1', 19200, timeout=1)   # RM- needed this whole init routine, especially ser definition
open('/sys/kernel/debug/omap_mux/' + RX_MUX, 'wb').write("%X" % (RECEIVE_ENABLE + MUX_MODE))
open('/sys/kernel/debug/omap_mux/' + TX_MUX, 'wb').write("%X" % (TRANSMIT_ENABLE + MUX_MODE))

#----------------------------------------------------------#
# define constants and variables used to control the LED   #
# ---------------------------------------------------------#
_UpdateScreen          =   chr(0x00)
_SetPointerX           =   chr(0x03)
_SetPointerY           =   chr(0x04)
_SetForegroundColor    =   chr(0x11)
_SetBackgroundColor    =   chr(0x12)
_DisplayChar0508       =   chr(0x13)
_DrawDot               =   chr(0x1D)
_SetLineEndX           =   chr(0x1E)
_SetLineEndY           =   chr(0x1F)
_DrawLine              =   chr(0x20)
_SetRadius             =   chr(0x21)
_DrawCircle            =   chr(0x22)
_Copy2bxGDRAM          =   chr(0x0A)
_DisplaybxGDRAM        =   chr(0x0B)
_fillGDRAM             =   chr(0x0C)  # Fill the GDRAM with Data(User Defined)
_DisplayCustomerBMP1   =   chr(0x1B)
_ASCII_A		= chr(0x41)
_ASCII_B		= chr(0x42)
_ASCII_C		= chr(0x43)
_ASCII_D		= chr(0x44)
_ASCII_E		= chr(0x45)
_ASCII_F		= chr(0x46)
_ASCII_SPACE		= chr(0x20)
_HEX_0			= chr(0x00)
_PMTX = "PMTX"

Index      = chr(0x00)
IndexX     = chr(0x00)
IndexY     = chr(0x00)

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
Update_String = _PMTX + _UpdateScreen + _HEX_0 + _HEX_0 + _HEX_0 + _HEX_0   # RM- you where short 1 _HEX_0


		#######################################
		# simple routine to refresh LED unit  #
		# value of wait-time is passed in     #
		#######################################

def Update_LED(wait_time):
	ser.write(Update_String)
	time.sleep(wait_time)
	return

		#######################################
		# simple routine to clear  LED unit   #
		#######################################
def clear_matrix():
	out_string = _PMTX + _fillGDRAM + _HEX_0 + _HEX_0 + _HEX_0 + _HEX_0
	ser.write(out_string)
	Update_LED(0)
	return


	       #######################################
	       # main section of program starts here #
	       #######################################

# see if anything was passed in on the command line
parmcount = len(sys.argv)
if parmcount > 1: # 1 indicates nothing passed in on command line
	command = int(sys.argv[1])
	print 'using command line input =', command
else:
	command = 1
	print 'using default command =', command

# Clear the displpay to start things off  RM-added this to start off with a clear display
time.sleep(2)  # give matrix time to set up
clear_matrix()

for LETTER in Alphabet:
	out_string = _PMTX + _DisplayChar0508 + _HEX_0 + _HEX_0 + _HEX_0 + LETTER
	ser.write(out_string)
	Update_LED(.2)
	time.sleep(0.5)  # give matrix time to set up

# Clear the displpay to start next set of things
clear_matrix()


#----------------------------------------------------------------------#
# Draw a series Dots to fill the display. left to right, top to bottom #
#----------------------------------------------------------------------#
for IndexY in range (0, 8):	#RM- can't see the color change onthe display if same as above, changed to Red
	for IndexX in range (0, 8):
		xout_string = _PMTX + _SetPointerX + _HEX_0 + _HEX_0 + _HEX_0 + chr(IndexX)
		ser.write(xout_string)
		yout_string = _PMTX + _SetPointerY + _HEX_0 + _HEX_0 + _HEX_0 + chr(IndexY)
		ser.write(yout_string)
		purple_dot_string = _PMTX + _DrawDot + _HEX_0 + chr(0xFF) + _HEX_0 + chr(0xFF)
		ser.write(purple_dot_string)
		Update_LED(.1)
	time.sleep(.1)

#RM- can't see the color change on the display if same as above, changed to Yellow
#----------------------------------------------------------------------#
# Draw a series Dots to fill the dislay. right to left, bottom to top
#----------------------------------------------------------------------#
print "REVERSING NOW"
time.sleep(2)
for IndexY in range (7, -1, -1):
	for IndexX in range (7, -1, -1):
		xout_string = _PMTX + _SetPointerX + _HEX_0 + _HEX_0 + _HEX_0 + chr(IndexX)
		ser.write(xout_string)
		yout_string = _PMTX + _SetPointerY + _HEX_0 + _HEX_0 + _HEX_0 + chr(IndexY)
		ser.write(yout_string)
		yellow_dot_string = _PMTX + _DrawDot + _HEX_0 + _HEX_0 + chr(0xFF) + chr(0xFF)
		ser.write(yellow_dot_string)
#		Update_LED(.1)
	Update_LED(0)
	time.sleep(.2)

#----------------------------------------------------------------------#
# Draw some random dots, but display only at the end.  See how fast    #
# the LEDs can be written to before refresh.                           #
#----------------------------------------------------------------------#
for IndexY in range (0, 8, 2):	
	for IndexX in range (0, 8, 2):
		xout_string = _PMTX + _SetPointerX + _HEX_0 + _HEX_0 + _HEX_0 + chr(IndexX)
		ser.write(xout_string)
		yout_string = _PMTX + _SetPointerY + _HEX_0 + _HEX_0 + _HEX_0 + chr(IndexY)
		ser.write(yout_string)
		purple_dot_string = _PMTX + _DrawDot + _HEX_0 + chr(0xFF) + _HEX_0 + chr(0xFF)
		ser.write(purple_dot_string)
Update_LED(0)
time.sleep(30)

# Clear the displpay to clean up after the program is over
clear_matrix()

