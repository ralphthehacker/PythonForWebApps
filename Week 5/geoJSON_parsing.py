import json
import urllib

# Base url for the Google Maps API
service_url = 'http://python-data.dr-chuck.net/geojson?'
while True:
    # Get the url from user input
    counts = 0
    address = raw_input("What's the location")

    # Querying the Google Maps API with a user inputted location
    url = service_url + urllib.urlencode({'sensor':'false', 'address': address})

    # read data from the url
    open_url = urllib.urlopen(url.strip())
    data = open_url.read()
    print("Received number of characters: ", len(data))

    # Load the JSON
    location_json = json.loads(data)
    print "The placeID is ",location_json["results"][0]["place_id"]
