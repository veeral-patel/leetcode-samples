def move_zeroes(nums):
    if not nums:
        return

    slow = 0
    fast = 0

    # While we haven't reached end of the array
    while fast <= len(nums)-1:
        # If we reach a non-zero number
        if nums[fast] != 0:
            # Then swap
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

        # Always advance second pointer
        fast += 1
