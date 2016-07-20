# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers in the file.
# We provide two files for this assignment. One is a sample file where we give you the sum
# for your testing and the other is the actual data you need to process for the assignment.
# You do not need to save these files to your folder since your program will read the data
# directly from the URL. Note: Each student will have a distinct data url for tetrieve all of the anchor tags
# your own data url for analysis.

import urllib
from bs4 import BeautifulSoup

url = raw_input('Enter - ')
html = urllib.urlopen(url).read()

soup = BeautifulSoup(html)

count = 0
s = 0
tags = soup('span')
for tag in tags:
    count += 1
    s += int(tag.contents[0])
print 'Count', count
print 'Sum', s
