"""Function for querying doordash by lat/long."""

import json
import requests
import urlparse


def query_doordash_by_location(baseurl=None, latitude=None, longitude=None):
    """Search for restaurants around a location.
    
    Args:
        baseurl (str): the base url for doordash API.
        latitude (str): latitude to query.
        longitude (str): longitude to query.
        
    Returns:
        dict: a dictionary containing found restaurants.
    """

    baseurl = "https://www.doordash.com"
    latitude = "39.596371"
    longitude = "-119.777603"

    url = urlparse.urljoin(baseurl, 'api/v2/restaurant/?lat={0}&lng={1}'.format(latitude, longitude))
    response = requests.get(url)

    return response.json()





