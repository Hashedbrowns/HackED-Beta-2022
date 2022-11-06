import json
from RoutePoint import RoutePoint
from Route import Route
import jsonpickle
import ProjectCustomExceptions
import os
 


def readData(filename):
    '''
    Opens a data file for reading.
    '''
    print("File location using os.getcwd():", os.getcwd())
    with open(os.getcwd() + '/googleDirectionsScraper/' + filename, "r") as read_file:
        data = json.load(read_file)

    return data

def getRoutePairs():
    '''
    Gets the route pair information from Craig's output file.
    return:
        routes - list(list(RoutePoints)): a list of 2-list set of RoutePoints
    '''
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
    '''
    Gets the Route information from the existing output file. This function
    exists in case we need to rerun the script and we want to avoid duplicate
    calls to the Google API. 
    '''
    routesAppended = []

    # read the data from the appended file for comparing against the 
    #  data = readData('edges-appended.json')
    with open(os.getcwd() + '/googleDirectionsScraper/' + 'edges-appended.json', 'r') as fi:
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

