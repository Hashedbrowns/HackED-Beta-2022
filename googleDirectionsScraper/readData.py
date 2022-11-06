import json
from RoutePoint import RoutePoint
from Route import Route
import jsonpickle
import ProjectCustomExceptions

def readData(filename):
    with open(filename, "r") as read_file:
        data = json.load(read_file)

    return data

def getRoutePairs():
    routes = []

    data = readData("edges.json")

    for pair in data:
        route = []
        for point in pair:
            id, name, loc = point.values()
            lat, long = loc
            route.append(RoutePoint(name, id, lat, long))
        routes.append(route)
    return routes

def getRoutePairsAppended():
    routesAppended = []

    # read the data from the appended file for comparing against the 
    #  data = readData('edges-appended.json')
    with open('edges-appended.json', 'r') as fi:
        file_contents = fi.read()
        if len(file_contents) == 0:
            raise ProjectCustomExceptions.FileEmptyError
        decoded_data = jsonpickle.decode(file_contents)

    # read all existing data
    for route in decoded_data:
        # pt1, pt2, distance, polyline = route #.value()
        routesAppended.append(route)
    return routesAppended


    # return the data

