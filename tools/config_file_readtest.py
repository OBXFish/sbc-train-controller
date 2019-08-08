##############################################################
#             
#             Test Reading of the Train Control Config File
#
#                 Ken Fischer 06/2013 
#
# Program opend the text based config file at ~/traincoltrol
# and dumps the contents to the users display
#
#  syntax:  ConfigFileReadTest()
#  input Parameters:  None
#
#############################################################

ins = open( "$HOME/traincontrol/relay.config", "r" )
array = []
for line in ins:
    array.append( line )
    print line
print array
#lines = (line.rstrip('\n') for line in open("$HOME/traincontrol/relay.config")
#print line
splines = tuple(open("$HOME/traincontrol/relay.config", 'r'))
print 'printing splines'
print splines
nlines = [line.rstrip('\n') for line in open("$HOME/traincontrol/relay.config")]
print 'nlines = '
print nlines

