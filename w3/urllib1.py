import urllib
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt') #take and opened this url

for line in fhand:
    print line.strip()
