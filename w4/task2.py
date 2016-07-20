# Following Links in Python

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter URL: ')
c = int(raw_input('Enter count: '))
p = int(raw_input('Enter position: '))

print url
while c > 0:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    url = tags[p - 1].get('href', None)
    print url

    c -=  1

