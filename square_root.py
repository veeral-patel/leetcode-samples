import math

def square_root(n):
    arr = list(range(n+1))

    answer = -1

    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        squared = math.floor(pow(arr[mid], 2))
        if squared == n:
            # we found the answer exactly. exit with the
            # answer
            answer = arr[mid]
            return answer

        elif squared < n:
            # this is a candidate for the answer
            answer = arr[mid]

            # however let's search right to find a higher
            # number which squared is less than n
            left = mid+1

        else:
            # too large: search left
            right = mid-1

    return answer

'''
Example

square_root(5)

arr = [1,2,3,4,5]
left = 0
right = 4
mid = 2
arr[mid] = 3

squared = math.floor(pow(3,2)) = 9
'''
