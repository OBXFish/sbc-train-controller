############################################################
#
#             SpawnProcessTest Program
#
#                 Ken Fischer 06/2013 
#
# This test program spanws 6 process, one of each mode type with 
# hard coded values.  This tool is really not useful except for debugging
#
#  syntax:  SpawnProcessTest()
#  Input Parameters:  None
#
#############################################################

# Import libraries including PyBBIO library:
import time
import subprocess

subprocess.Popen('python Mode_1_Relay_Test.py 1 2 1 60 10 > /home/traincontrol/logs/Mode_1_Output.log', shell=True)
time.sleep(.1)
subprocess.Popen('python Mode_2_Relay_Test.py 8 1 120 6 > /home/traincontrol/logs/Mode_2_Output.log', shell=True)
time.sleep(.1)
subprocess.Popen('python Mode_3_Relay_Test.py 3 1 > /home/traincontrol/logs/Mode_3_Output.log', shell=True)
time.sleep(.1)
subprocess.Popen('python Mode_4_Relay_Test.py 4 1 15 10 > /home/traincontrol/logs/Mode_4_Output.log', shell=True)
time.sleep(.1)
subprocess.Popen('python Mode_5_Relay_Test.py 5 1 10 5 > /home/traincontrol/logs/Mode_5_Output.log', shell=True)
time.sleep(.1)
subprocess.Popen('python Mode_6_Relay_Test.py 6 1 10 5 > /home/traincontrol/logs/Mode_6_Output.log', shell=True)
time.sleep(.1)


