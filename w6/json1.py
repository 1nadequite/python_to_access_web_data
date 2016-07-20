import urllib
import json

url = raw_input('Enter location: ')
print 'Retrieving', url

data = urllib.urlopen(url).read() # read from this url
print 'Retrieved', len(data), 'characters' # print numbers of char

info = json.loads(data) # load json
print 'Count:', len(info['comments'])

s = 0
for item in info['comments']:
    s += int(item['count'])
print 'Sum:', s
