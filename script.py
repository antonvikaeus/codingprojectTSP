#!/usr/bin/env python

#Below I create an array with Swedens 10 largest cities and the
#distancce between each pair of cities.

#each city has a specific index value, e.g. Stockholm has index 0, Norrköping index 9
45
#List of distances in kilometers
# Sthlm, Goth, Malm, Uppsa, Vasteras, Orebro, Linkoping, Helsingborg, Jonkoping, Norrkoping
d = [470.78,614.07,72.01,107.48,198.51,200.00,557.13,324.55,161.79, \
    ,,,,,,,,,,,,,,,,,,]
#List over coordinates of all cities, for making visualiztion
coordinates = [(59.32758544549431,18.0999755859375),(57.715885127745054,11.9915771484375),(55.584554519645074,13.018798828125),(59.867572594860526,17.656402587890625),(59.59762076586839,16.5618896484375), \
    (59.30095391119714,15.22430419921875),(58.393076007580135,15.66650390625),(55.9922367329393,12.799072265625),(57.73934950049299,14.21630859375),(58.578277001241794,16.21307373046875)]
list_cities_dist = [(0,1,d[0]), (0,2,d[1]), (0,3,d[2]), (0,4,d[3]), (0,5,d[4]), (0,6,d[5]), (0,7,d[6]), (0,8,d[7]), (0,9,d[8]), \
                    (1,2,d[]), (1,3,d), (1,4,d), (1,5,d), (1,6,d), (1,7,d), (1,8,d18), (1,9,d19), \
                    (2,3,d), (2,4,d), (2,5,d), (2,6,d), (2,7,d), (2,8,d), (2,9,d), \
                    (3,4,d), (3,5,d), (3,6,d), (3,7,d), (3,8,d), (3,9,d), \
                    (4,5,d), (4,6,d), (4,7,d), (4,8,d), (4,9,d), \
                    (5,6,d), (5,7,d), (5,8,d), (5,9,d), \
                    (6,7,d), (6,8,d), (6,9,d), \
                    (7,8,d), (7,9,d), \
                    (8,9,d) ]

print(list_cities_dist)


#below I pick out the distance between city 0 and 2
try_ind = list_cities_dist[1][2]
print(try_ind)