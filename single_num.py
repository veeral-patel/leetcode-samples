def singleNumber(nums):
    # Ideas
    # Bit manipulation- just XOR all nums together
    # Sorting
    # Frequency map
    # In place trick- could work, but complicated
    res = 0
    for num in nums:
        res = res ^ num
    return res
