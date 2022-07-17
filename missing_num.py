def missingNumber(nums):
    # Ideas
    # Sort: O(n log n) T, O(1) S
    # Hashset: O(n) T, O(n) S
    # Bit manipulation- XOR with 0,1,2,...n. O(n) T, O(n) S
    pass
    missing = 0
    for num in nums:
        missing = num ^ missing
    for a in range(0, len(nums)+1):
        missing = a ^ missing
    return missing
