def twoSum(nums, target):
    nums.sort()

    start = 0
    end = len(nums)-1

    while start < end:
        num1, num2 = nums[start], nums[end]
        total = num1 + num2
        if total == target:
            return [num1, num2]
        elif total > target:
            end -= 1
        else:
            start += 1

    return [-1, -1]
