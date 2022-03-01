from typing import List

class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        if not arr1 or not arr2 or not arr3:
            return []

        p1, p2, p3 = 0, 0, 0
        intersection = []

        while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
            num1, num2, num3 = arr1[p1], arr2[p2], arr3[p3]

            # print(num1, num2, num3)

            # if all the numbers are the same, save to our list
            # and advance all pointers
            if num1 == num2 and num2 == num3:
                intersection.append(num1)
                p1, p2, p3 = p1+1, p2+1, p3+1
            else:
                # otherwise, advance the two smaller pointers
                # as we'll never see those numbers again
                if arr1[p1] < arr2[p2]:
                    p1 += 1
                elif arr2[p2] < arr3[p3]:
                    p2 += 1
                else:
                    p3 += 1

        return intersection
