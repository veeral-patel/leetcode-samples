from typing import List

def merge_k_sorted_lists(lists: List[List[int]]) -> List[int]:
    # https://algo.monster/problems/merge_k_sorted_lists
    # Store (value, index of list in list of lists, index of value in that list)
    # in heap.
    heap = []

    for listIndex, lst in enumerate(lists):
        heapq.heappush(heap, (lst[0], listIndex, 0))

    ans = []

    while heap:
        val, listIndex, index = heapq.heappop(heap)

        ans.append(val)

        lst = lists[listIndex]

        if index < len(lst)-1:
            heapq.heappush(heap, (lst[index+1], listIndex, index+1))

    return ans

