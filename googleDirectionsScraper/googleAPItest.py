import googlemaps
from datetime import datetime

def getPath(point1 , point2):
    gmaps = googlemaps.Client(key='AIzaSyAgMqgptHbdD-oXy0McQQk9XPW6thfo0T4')

    # Geocoding an address
    geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

    # Look up an address with reverse geocoding
    reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

    # Request directions via public transit
    now = datetime.now()
    directions_result = gmaps.directions(point1,
                                        point2,
                                        mode="walking",
                                        departure_time=now)
    print(directions_result)

p1 = 'Sydney Town Hall'
p2 = 'Parramatta, NSW'

print(getPath(p1,p2))