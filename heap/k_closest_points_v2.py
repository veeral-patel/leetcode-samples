from typing import List, Tuple
import heapq

def dist(point):
    return point[0]**2 + point[1]**2

def k_closest_points(points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    maxHeap = [] # max heap to store k closest elements
    for point in points:
        if len(maxHeap) < k:
            # heap has space => add to it
            heapq.heappush(maxHeap, (-dist(point), point))
        else:
            # no space => remove the top element (farthest one)
            # if it's farther than POINT
            if dist(point) < -maxHeap[0][0]:
                heapq.heappop(maxHeap)
                heapq.heappush(maxHeap , (-dist(point), point))

    closest = []
    for i in range(k):
        _, point = heapq.heappop(maxHeap)
        closest.append(point)

    return closest

'''
Example

points: [[1,3], [-2,2]]
k = 1

[(-8, [-2, 2])]
'''
