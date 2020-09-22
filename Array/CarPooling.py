"""
You are driving a vehicle that has capacity empty seats initially available for passengers.  
The vehicle only drives east (ie. it cannot turn around and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] contains 
information about the i-th trip: the number of passengers that must be picked up, and the 
locations to pick them up and drop them off.  The locations are given as the number of 
kilometers due east from your vehicle's initial location.

Return true if and only if it is possible to pick up and drop off all passengers for all 
the given trips. 

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
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