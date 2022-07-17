def square_root(n):
    low = 0
    high = n

    ans = -1

    while low <= high:
        mid = (low+high) // 2

        squared = mid**2

        if squared == n:
            return mid
        elif squared < n:
            ans = mid
            low = mid+1
        elif squared > n:
            high = mid-1

    return ans
