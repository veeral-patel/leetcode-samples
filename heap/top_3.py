from typing import List
import heapq

"""
Given a list of numbers, return top 3 smallest numbers
"""

def heap_top_3(arr: List[int]) -> List[int]:
    heap = []
    
    for i, num in enumerate(arr):
        heapq.heappush(heap, num)
        
    ans = []
    for _ in range(3):
        ans.append(heapq.heappop(heap))
        
    return ans
