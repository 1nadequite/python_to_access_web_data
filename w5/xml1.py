import urllib
import xml.etree.ElementTree as ET

loc = raw_input('Enter location: ')
print 'Retrieving', loc

fhand = urllib.urlopen(loc).read() # read XML from this loc
print 'Retrieved', len(fhand), 'characters' # print numbers of characters

tree = ET.fromstring(fhand) # create XML scheme (tree)
counts = tree.findall('.//count') # take all 'comment' from 'comments'
print 'Count:', len(counts)

s = 0
for comm in counts:
    s += int(comm.text) # sum
print 'Sum:', s
