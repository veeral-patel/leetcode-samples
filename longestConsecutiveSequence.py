def longestConsecutiveSequence(nums):
    if not nums:
        return []

    nums.sort()

    longestSequence = 1
    curSequence = 1

    for i in range(len(nums)-1):
        if nums[i]+1 == nums[i+1]:
            curSequence += 1
            longestSequence = max(curSequence, longestSequence)
        else:
            curSequence = 1

    return longestSequence

def n2(nums):
    if not nums:
        return 0

    numsSet = set(nums)

    longestSequence = []

    for num in nums:
        last = num
        curSequence = [last]
        while last+1 in numsSet:
            curSequence.append(last+1)
            last = last+1
        if len(curSequence) > len(longestSequence):
            longestSequence = curSequence

    return longestSequence
