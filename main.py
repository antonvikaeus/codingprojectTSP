#!/usr/bin/env python2

#Wanted to visualize this with the help of the coordinates of the city.
#coordinates = {'Sthlm':{59.32758544549431,18.0999755859375} , 'Gbg': {57.715885127745054,11.9915771484375}, ''(55.584554519645074,13.018798828125),(59.867572594860526,17.656402587890625),(59.59762076586839,16.5618896484375), \   # (59.30095391119714,15.22430419921875),(58.393076007580135,15.66650390625),(55.9922367329393,12.799072265625),(57.73934950049299,14.21630859375),(58.578277001241794,16.21307373046875)

routes = []


def find_paths(node, cities, path, distance):
    # Add waypoint
    path.append(node)

    # Calculate path length from current to last node
    if len(path) > 1:
        distance += cities[path[-2]][node]

    # add path from last to first city and return.
    if (len(cities) == len(path)) and (cities[path[-1]].has_key(path[0])):
        global routes
        path.append(path[0])
        distance += cities[path[-2]][path[0]]
        print(path, distance)
        routes.append([distance, path])
        return

    # create paths for all possible cities not yet used
    for city in cities:
        if (city not in path) and (cities[city].has_key(node)):
            find_paths(city, dict(cities), list(path), distance)


if __name__ == '__main__':
    cities = {
        'Sthlm': {'Gbg': 470.78, 'Malmo': 614.07, 'Uppsala': 72.01, 'Vasteras': 107.48, 'Orebro': 198.51,'Linko': 200,'Helsing': 557.13,'Jonko': 324.55,'Norrko': 161.79},
        'Gbg': {'Sthlm': 470.78, 'Malmo': 272.66, 'Uppsala': 453.54, 'Vasteras': 376.92, 'Orebro': 282.27, 'Linko': 274.52, 'Helsing': 215.66, 'Jonko': 145.83,'Norrko': 312.34},
        'Malmo': {'Sthlm': 614.07, 'Gbg': 272.66, 'Uppsala': 679.74, 'Vasteras': 597.09, 'Orebro': 502.43, 'Linko': 417.72, 'Helsing': 264.96, 'Jonko': 291.68,'Norrko': 455.53},
        'Uppsala': {'Sthlm': 72.01, 'Gbg': 453.54, 'Malmo': 679.74, 'Vasteras': 77.00, 'Orebro': 171.76, 'Linko': 265.17, 'Helsing': 622.30, 'Jonko': 389.72,'Norrko': 226.96},
        'Vasteras': {'Sthlm': 107.48, 'Gbg': 376.92, 'Malmo': 597.09, 'Uppsala': 77.00, 'Orebro': 95.65, 'Linko': 191.29, 'Helsing': 540.59, 'Jonko': 308.01,'Norrko': 153.07},
        'Orebro': {'Sthlm': 198.51, 'Gbg': 282.27, 'Malmo': 502.43, 'Uppsala': 171.76, 'Vasteras': 95.65, 'Linko': 140.12, 'Helsing': 445.86, 'Jonko': 213.29,'Norrko': 116.41},
        'Linko': {'Sthlm': 200, 'Gbg': 274.52, 'Malmo': 417.72, 'Uppsala': 265.17, 'Vasteras': 191.29, 'Orebro': 140.12, 'Helsing': 361.34, 'Jonko': 128.77,'Norrko': 42.04},
        'Helsing': {'Sthlm': 557.13, 'Gbg': 215.66, 'Malmo':  264.96, 'Uppsala': 622.30, 'Vasteras': 540.59, 'Orebro': 445.86, 'Linko': 361.34, 'Jonko': 234.61,'Norrko': 398.46},
        'Jonko':  {'Sthlm': 324.55, 'Gbg': 145.83, 'Malmo':  291.68, 'Uppsala': 389.72, 'Vasteras': 308.01, 'Orebro': 213.29, 'Linko': 128.77, 'Helsing': 234.61,'Norrko': 166.51},
        'Norrko': {'Sthlm': 161.79, 'Gbg': 312.34, 'Malmo':  455.53, 'Uppsala': 226.96, 'Vasteras': 153.07, 'Orebro': 116.41, 'Linko': 42.04, 'Helsing': 398.46,'Jonko': 166.51},

    }
    find_paths('Uppsala', cities, [], 0)
    print("\n")
    routes.sort()
    print("If we start in: Uppsala")
    if len(routes) != 0:
        print ("The shortest route is: %s" % routes[0])