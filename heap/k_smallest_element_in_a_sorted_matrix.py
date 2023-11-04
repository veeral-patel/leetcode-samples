from typing import List
import heapq

def kth_smallest(matrix: List[List[int]], k: int) -> int:
    heap = []
    
    # Insert (value, row #, col #) tuples into the heap
    for i, row in enumerate(matrix):
        heapq.heappush(heap, (row[0], i, 0))
                       
                       
    rank = 1
                       
    while heap:
        # Fetch next smallest item into the heap
        nxtVal, nxtRowIdx, nxtColIdx = heapq.heappop(heap)
        if rank == k:
            return nxtVal
                       
        # Insert next element in that row into the heap if possible
        matching_row = matrix[nxtRowIdx]
        if nxtColIdx + 1 <= len(matching_row)-1:
            nxtHighestColIdx = nxtColIdx + 1
            heapq.heappush(heap, (matching_row[nxtColIdx + 1], nxtRowIdx, nxtColIdx + 1))
                       
        rank += 1
