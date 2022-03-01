import heapq
from typing import List, Tuple

def k_closest_points(points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    heap = []
    for point in points:
        heapq.heappush(heap, (point[0]**2 + point[1] ** 2, point))

    closest = []
    for i in range(k):
        entry = heapq.heappop(heap)
        point = entry[1]
        closest.append(point)

    return closest
