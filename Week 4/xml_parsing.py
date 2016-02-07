import urllib
import xml.etree.ElementTree as ET
#Objective: Add up all the numbers in the count tags
text =raw_input("Enter the url")
#"http://python-data.dr-chuck.net/comments_42.xml"
# First, read the url
url = urllib.urlopen(text.encode('UTF-8'))

#now, read the XML data
data = url.read()

# And form a XML tree with it
xml_tree = ET.fromstring(data)

# Then, look for the count tags
counts = xml_tree.findall(".//count")
sum = 0

#Finally, add up all the count values
for count in counts:
    sum += int(count.text)


print sum