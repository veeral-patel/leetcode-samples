from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True

        memoized = [False]*len(nums)

        for i in reversed(range(len(nums))):
            # at the end already
            if i == len(nums)-1:
                memoized[i] = True

            # can get to end in one jump
            for jumpCount in range(1, nums[i]+1):
                if i + jumpCount == len(nums)-1:
                    memoized[i] = True

            # can get to the end in multiple jumps
            for jumpCount in range(1, nums[i]+1):
                jumpIndex = i + jumpCount
                if jumpIndex <= len(nums)-1 and memoized[jumpIndex]:
                    memoized[i] = True

        print(memoized)

        return memoized[0]

s = Solution()
assert s.canJump([2,3,1,1,4]) == True
assert s.canJump([1,8]) == True
assert s.canJump([]) == True
assert s.canJump([1,2,3]) == True
assert s.canJump([3,2,1,0,4]) == False
print("tests passed")
