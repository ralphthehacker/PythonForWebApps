from BeautifulSoup import *
import urllib
import ssl


url = raw_input("Plz enter the url")
count = int(raw_input("Plz enter the count"))
position = int(raw_input("Plz enter the position"))
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)

count_index = 0
return_user = None
while count_index in range(count) :
    #Using the .read() function makes urlib read all the data from the url at once
    html = urllib.urlopen(url,context= scontext).read()

    #The html is passed as a constructor to BeautifulSoup
    cute_soup = BeautifulSoup(html)

    # Looking for all the span tags
    tags = cute_soup('a')
    # print"*****TAG*******"
    # print tags
    # print "**************"

    #Getting the current tag and counting values
    for i,tag in enumerate(tags):
        #Looking for the tag in the user prompted position
        if i == position-1:
            url = tag.get('href', None)
            print "Current index at iteration", count_index, ":", url
            return_user = tag.contents[0]
            break
    # Incrementing the counter
    count_index+=1

print "The user is ", return_user
