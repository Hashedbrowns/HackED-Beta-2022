
import readData
from Route import Route
from getPath import getPath
from datetime import datetime
import jsonpickle
import ProjectCustomExceptions

def main():
    '''
    This will take a pre-existing list of direction pairs and then make calls to Google Directions
    to get the route data and distance and then jsonpickle the list of objects and write it out to a
    json file.
    '''
    routes = readData.getRoutePairs()
    originalAppendedRoutes= []

    try: 
        originalAppendedRoutes = readData.getRoutePairsAppended()
    except FileNotFoundError:
        # create the file
        print('No existing file was found for the points. ')
    except ProjectCustomExceptions.FileEmptyError:
        print('The edge file is empty.')


    appendedRoutes = []
    counter = 0

    CALL_LIMIT = 275

    calls = {}
    start = datetime.now()

    # ensure that we make no more than 1000 calls to the API. 
    danger_counter = 0
    while routes and danger_counter < 2500:
        now = datetime.now()
        cur_time = (now-start).seconds // 60
        if cur_time not in calls:
            calls[cur_time] = 0
        # check if the route is already in appended routes
        # counter in place during testing to make sure we don't 
        if calls[cur_time] < CALL_LIMIT:
            route = routes.pop()
            counter += 1
            danger_counter += 1

            p1, p2 = route
            new_route = Route(p1, p2)
            if new_route not in originalAppendedRoutes:
                if counter % 10 == 0 and counter > 0:
                    print(f'Calculated distances for {counter} routes.')
                path = getPath(p1, p2)
                route = Route(p1, p2, path[0]['legs'][0]['distance'], path[0]['overview_polyline']['points'])
                appendedRoutes.append(route)
                calls[cur_time] += 1
            else:
                appendedRoutes.append(new_route)


    with open('edges-appended.json', 'w+') as wf:
        write_contents = jsonpickle.encode(appendedRoutes)
        wf.write(write_contents)

if __name__== "__main__":
    main()