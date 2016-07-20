# Parsing HTML with BeautifulSoup
import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')

html = urllib.urlopen(url).read() # read all html
soup = BeautifulSoup(html)

# Retrieve a list of the anchor tags
# Each tag is like a dictionary in HTML attributes

tags = soup('a') # find all <a> tags

for tag in tags:
    print tag.get('href', None) # print links
