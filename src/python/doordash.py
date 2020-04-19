"""Function for querying doordash by lat/long."""

import json
import requests


def query_doordash_by_location(baseurl=None, latitude=None, longitude=None):
    """Hackathon exercise """

    baseurl = "https://www.doordash.com"
    latitude = "39.596371"
    longitude = "-119.777603"

    url = "https://www.doordash.com/api/v2/restaurant/?lat={0}&lng={1}".format(latitude, longitude) 
    response = requests.get(url)

    return response.json()





