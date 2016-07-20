import urllib
import xml.etree.ElementTree as ET

loc = raw_input('Enter location: ')
print 'Retrieving', loc

fhand = urllib.urlopen(loc).read() # read XML from this loc
print 'Retrieved', len(fhand), 'characters' # print numbers of characters

tree = ET.fromstring(fhand) # create XML scheme (tree)
counts = tree.findall('comments/comment') # take all 'comment' from 'comments'

count = 0
s = 0
for comm in counts:
    count += 1
    s += int(comm.find('count').text) # sum

print 'Count:', count
print 'Sum:', s
