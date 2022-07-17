def squares(nums):
    if not nums:
        return []

    start, end = 0, len(nums)-1

    lst = []

    while start <= end:
        num1 = nums[start]
        num2 = nums[end]

        if abs(num1) >= abs(num2):
            lst.insert(0, num1**2)
            start += 1
        else:
            lst.insert(0, num2**2)
            end -= 1

    return lst


