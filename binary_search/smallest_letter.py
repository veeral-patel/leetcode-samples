def smallest_letter(letters, target):
    low, high = 0, len(letters)-1
    index = -1

    while low <= high:
        mid = (low+high)//2
        if letters[mid] > target:
            # can use this
            index = mid
            # search left
            high = mid-1
        else:
            # can't use this. search right
            low = mid+1

    if index == -1:
        return letters[0]
    else:
        return letters[index]
