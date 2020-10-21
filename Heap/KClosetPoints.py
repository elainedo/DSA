'''
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
'''

import heapq

def kClosest(points, K):
    pq = [] #priority queue
    
    for point in points:
        heapq.heappush(pq, (-(point[0]*point[0]+point[1]*point[1]), point))
        if len(pq) > K:
            heapq.heappop(pq)
        
    return [y for (x, y) in pq]

print(kClosest([[1,3],[-2,2]], 1))