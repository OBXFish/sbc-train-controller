import sys
import time
import random
import termios
import atexit
from select import select

#kbhit credits go to http://code.activestate.com/recipes/572182-how-to-implement-kbhit-on-linux/

print "Knight Rider style LEDs on the BeagleBone"
print "Press 'q' to exit"

leds = [
'/sys/class/leds/beaglebone::usr0/brightness',
'/sys/class/leds/beaglebone::usr1/brightness',
'/sys/class/leds/beaglebone::usr2/brightness',
'/sys/class/leds/beaglebone::usr3/brightness',
]

def ledon(n):
        value = open(leds[n],'w')
        value.write(str(1))
        value.close()

def ledoff(n):
        value = open(leds[n],'w')
        value.write(str(0))
        value.close()

def toggle(x):
	ledon(x)
        time.sleep(.1)
        ledoff(x)

for i, val in enumerate(leds):
	ledoff(i)

# save the terminal settings
fd = sys.stdin.fileno()
new_term = termios.tcgetattr(fd)
old_term = termios.tcgetattr(fd)

# new terminal setting unbuffered
new_term[3] = (new_term[3] & ~termios.ICANON & ~termios.ECHO)

# switch to normal terminal
def set_normal_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, old_term)

# switch to unbuffered terminal
def set_curses_term():
    termios.tcsetattr(fd, termios.TCSAFLUSH, new_term)

def getch():
    return sys.stdin.read(1)

def kbhit():
    dr,dw,de = select([sys.stdin], [], [], 0)
    return dr <> []

if __name__ == '__main__':
    atexit.register(set_normal_term)
    set_curses_term()

    while 1:
        if kbhit():
            ch = getch()
	    if ch == 'q':
            	break
	for x in range(0, 4, 1):
		toggle(x)

	for x in range(2, 0, -1):
		toggle(x)
    print 'Exiting...'

