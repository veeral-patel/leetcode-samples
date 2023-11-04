def find_kth_largest(nums: List[int], k: int) -> int:
   nums = [-num for num in nums] # negate all nums
   heapq.heapify(nums) # set up min heap (but max heap since we negated nums)
   for _ in range(k-1):
        heapq.heappop(nums)
   ans = heapq.heappop(nums) # get the kth element
   return -ans # negate it back before returning
