"""Function for querying doordash by lat/long."""


def query_doordash_by_location(baseurl, latitude, longitude):
    """Search for restaurants around a location.
    
    Args:
        baseurl (str): the base url for doordash API.
        latitude (str): latitude to query.
        longitude (str): longitude to query.
        
    Returns:
        dict: a dictionary containing found restaurants.
    """
    url = urlparse.urljoin(baseurl, 'api/v2/restaurant/?lat={0}&lng={1}'.format(latitude, longitude))
    response = requests.get(url)

    return response.json()





