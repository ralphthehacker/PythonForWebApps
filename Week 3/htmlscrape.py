from BeautifulSoup import *
import urllib


url = raw_input("Plz enter the url")
#Using the .read() function makes urlib read all the data from the url at once
html = urllib.urlopen(url).read()

#The html is passed as a constructor to BeautifulSoup
cute_soup = BeautifulSoup(html)

# Looking for all the span tags
tags = cute_soup('span')

number_count = []

#Getting the current tag and counting values
for tag in tags:
    number_count.append(int(tag.contents[0].encode('utf-8')))

print sum(number_count)