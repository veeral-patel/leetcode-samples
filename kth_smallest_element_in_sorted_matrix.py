import heapq

def kth_smallest_element_in_a_sorted_matrix(matrix, k):
    if not matrix or k <= 0:
        return 0

    heap = []

    numRows = len(matrix)
    numCols = len(matrix[0])

    for i, row in enumerate(matrix):
        heapq.heappush(heap, (row[0], i, 0))

    for _ in range(k-1):
        num, rowIndex, colIndex = heapq.heappop(heap)
        if colIndex+1 <= numCols-1:
            num2 = matrix[rowIndex][colIndex+1]
            heapq.heappush(heap, (num2, rowIndex, colIndex+1))

    top = heap[0][0]

    return top

matrix = [
  [ 1,  5,  9],
  [10, 11, 13],
  [12, 13, 15]
]
k = 8

