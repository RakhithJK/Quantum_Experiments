"""Function for querying doordash by lat/long."""

import json
import requests

def query_doordash_by_location():
    baseurl = "https://www.doordash.com"
    latitude = "39.596371"
    longitude = "-119.777603"

    url = "https://www.doordash.com/api/v2/restaurant/?lat={0}&lng={1}".format(latitude, longitude) 

    message_dict = {}
    message_dict["message"] = requests.get(url)
    message_dict["schema"] = "message"

    with open("search.json",'w') as f:
        f.write(json.dumps(message_dict, indent=2)) # Write message to file as this will serve as output artifact