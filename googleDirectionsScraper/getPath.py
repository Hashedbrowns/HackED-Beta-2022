import googlemaps
from RoutePoint import RoutePoint
from datetime import datetime
import ProjectCustomExceptions
import os
from dotenv import load_dotenv

load_dotenv()

# Actual API key not stored with application. See Ryan for key if needed for local dev.
GOOGLE_DIRECTIONS_API_KEY = os.getenv('GOOGLE_DIRECTIONS_API_KEY')

def getPath(point1: RoutePoint , point2: RoutePoint):
    '''
    Takes a pair of RoutePoints and gets the Google Directions API response for them.
    If the response is empty, it will raise an error.
    '''
    gmaps = googlemaps.Client(key=GOOGLE_DIRECTIONS_API_KEY)

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(point1.getCoordinates(),
                                        point2.getCoordinates(),
                                        mode="walking",
                                        departure_time=now)
    if len(directions_result) == 0:
        raise ProjectCustomExceptions.EmptyAPIResponse
    return directions_result
