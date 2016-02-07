import json
import urllib

# Get the url from user input
counts = 0
url = raw_input("What's the url")
print "Opening ", url.strip()
# read data from the url
open_url = urllib.urlopen(url.strip())
data = open_url.read()

# Print the number of characters
print "Number of characters: ",len(data)
# Parse json
json_dict = json.loads(data)

# print the comments
comment_list = json_dict["comments"]
for comment in comment_list:
    counts += comment["count"]

#Finally, print the total number of counts
print "The total count is ",counts