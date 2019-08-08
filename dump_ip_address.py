#########################################################
#    This python script obtains the current IP address  #
#    of this machine and writes it to a file in the     #
#    shared directory that is visable from the Macs etc #
#							#
#	To make this fiule useful, it needs to be	#
#	saved to /etc.init.d/				#
#							#
#########################################################

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8',80))      #address of Google's DNS Server
string = s.getsockname()[0]
s.close()
f = open('/home/root/python-files/BB_CURRENT_IP_ADDRESS','w')
f.write(string) # write out the IP address
f.write('\n')   # write new line so the file looks clean


