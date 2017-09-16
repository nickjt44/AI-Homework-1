############################################ README for CSC 520 Assignment 1 ############################################

I have written two code files: haversine.py and search.py. My code is written using Python 3, to be specific, Python 3.6.

#########################################################################################################################

haversine.py is used to calculate the distance from one city to another based on their latitude and longitude.

I used the formula for this calculation from the website http://www.movable-type.co.uk/scripts/latlong.html

The haversine() function takes two lat/long pairs and calculates the distance between the cities in kilometers. I noticed that
a couple of the cities provided had incorrect distances, which caused the calculated as the crow flies distance to be larger in
these cases, so I have multiplied the result by 0.95 just to make sure that the heuristic is admissable.

The makeHeuristic() function used the haversine function for each pair of cities, calculates the distances, and stores them in files.
Specifically, each city has a dedicated file, in a subdirectory called "cities/". In the file for a city, the distances from each city 
are in the format:

-city name- -distance-

This format allows the heuristic distances to be recovered easily and efficiently for in-program calculations.


#########################################################################################################################

The search.py file contains three algorithms: BFS, DFS, and A*. It also contains classes for the data structures used in the algorithms,
a function to initialize the graph (initGraph()), and a loop (searchloop()) that loops over all cities for exercises 3(b) and (c).

The algorithms are commented to explain their functionality.

#########################################################################################################################

In order to use the code, simply create a new instance of an object with the cities you wish to find a path between 
(eg. dfs = DFS("zerind","neamt"). 
The cities must be in lower case.
Then perform the search, eg. dfs.search(). The search will return the shortest path, and the number of nodes expanded.



