import googlemaps
from RoutePoint import RoutePoint
from datetime import datetime

class EmptyAPIResponse(Exception):
    pass

def getPath(point1: RoutePoint , point2: RoutePoint):
    gmaps = googlemaps.Client(key='AIzaSyAgMqgptHbdD-oXy0McQQk9XPW6thfo0T4')

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(point1.getCoordinates(),
                                        point2.getCoordinates(),
                                        mode="walking",
                                        departure_time=now)
    if len(directions_result) == 0:
        raise EmptyAPIResponse
    return directions_result
