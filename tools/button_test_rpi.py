# button__test.py - Ken Fischer 05/2013 (modified from Alexander Hiam - 2/2012)
# USR3 LED mirrors GPIO2_7 until CTRL-C is pressed.
# GPIO1_7 is written to as the opposite of USR3
#
# This example is in the public domain

# Import Python GPIO library for Raspberry Pi:
import RPi.GPIO as GPIO
import time

# Define Constants:
led_1_pin = 22
led_2_pin = 27
led_3_pin = 16
led_4_pin = 20
led_5_pin = 13
led_6_pin = 19
led_7_pin = 21
led_8_pin = 12
button_pin = 17
button_state = 0

# Create a setup function:
def setup():
  # Set the GPIO Mode:
  GPIO.setmode(GPIO.BCM)
  # Set the GPIO pins:
  GPIO.setup(led_1_pin, GPIO.OUT)
  GPIO.setup(led_2_pin, GPIO.OUT)
  GPIO.setup(led_3_pin, GPIO.OUT)
  GPIO.setup(led_4_pin, GPIO.OUT)
  GPIO.setup(led_5_pin, GPIO.OUT)
  GPIO.setup(led_6_pin, GPIO.OUT)
  GPIO.setup(led_7_pin, GPIO.OUT)
  GPIO.setup(led_8_pin, GPIO.OUT)
  GPIO.setup(button_pin, GPIO.IN)
  # Initialize LED State:
  GPIO.output(led_1_pin, GPIO.LOW)
  GPIO.output(led_3_pin, GPIO.LOW)
  GPIO.output(led_5_pin, GPIO.LOW)
  GPIO.output(led_7_pin, GPIO.LOW)
  GPIO.output(led_2_pin, GPIO.HIGH)
  GPIO.output(led_4_pin, GPIO.HIGH)
  GPIO.output(led_6_pin, GPIO.HIGH)
  GPIO.output(led_8_pin, GPIO.HIGH)
  print("Here we go... Press CTRL-C to exit")



# Create a main function:
setup()
try:
  while 1:
    if GPIO.input(button_pin):
       button_state = 0
       GPIO.output(led_1_pin, GPIO.LOW)
       GPIO.output(led_3_pin, GPIO.LOW)
       GPIO.output(led_5_pin, GPIO.LOW)
       GPIO.output(led_7_pin, GPIO.LOW)
       GPIO.output(led_2_pin, GPIO.HIGH)
       GPIO.output(led_4_pin, GPIO.HIGH)
       GPIO.output(led_6_pin, GPIO.HIGH)
       GPIO.output(led_8_pin, GPIO.HIGH)
    else:
       button_state = 1
       GPIO.output(led_1_pin, GPIO.HIGH)
       GPIO.output(led_3_pin, GPIO.HIGH)
       GPIO.output(led_5_pin, GPIO.HIGH)
       GPIO.output(led_7_pin, GPIO.HIGH)
       GPIO.output(led_2_pin, GPIO.LOW)
       GPIO.output(led_4_pin, GPIO.LOW)
       GPIO.output(led_6_pin, GPIO.LOW)
       GPIO.output(led_8_pin, GPIO.LOW)
    time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
  GPIO.cleanup() # cleanup all GPIO



