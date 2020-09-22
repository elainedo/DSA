"""

There is a car pooling system that picks up and drops off passengers but
every vehicle in this system can only drive in one direction. Each vehicle 
has a capacity (empty seats) of passengers.

Given a list of trips where trip[i] = [num_passenger, start, end], return if 
you can pick up and drop off passengers at locations specified. 

"""

def carPooling(trips, capacity):
    stops = [0 for i in range(1001)]
    for i in range(len(trips)):
        stops[trips[i][1]] += trips[i][0]
        stops[trips[i][2]] -= trips[i][0]
    for i in range(len(stops)):
        if capacity >= 0:
            capacity -= stops[i]
        else:
            break
    return capacity >= 0

trips = [[2,1,5],[3,3,7]]
capacity = 4
print(carPooling(trips, capacity))

trips = [[2,1,5],[3,3,7]]
capacity = 5
print(carPooling(trips, capacity))