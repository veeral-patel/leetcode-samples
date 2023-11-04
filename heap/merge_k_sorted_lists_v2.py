from typing import List
import heapq

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    heap = [] # min-heap
    
    # Populate the heap: (val, row num, col num) tuples
    # For the first element of each list
    for i, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], i, 0))
        
    ans = []
    
    while heap:
        val, row_idx, col_idx = heapq.heappop(heap)
        
        # Update results
        ans.append(val)
        
        # Add next value from the list we popped (if possible)
        matching_row = lists[row_idx]
        nxt_col_idx = col_idx + 1
        if nxt_col_idx <= len(matching_row)-1:
            nxt_val = matching_row[nxt_col_idx]
            heapq.heappush(heap, (nxt_val, row_idx, nxt_col_idx))
            
            
    return ans

