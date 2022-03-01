from collections import deque

def subsets(letters):
    # Handle edge case
    if not letters:
        return []

    # To store our list of subsets
    answer = []

    # We will be processing this queue
    queue = deque()

    # Populate our queue
    queue.append([])

    # While there are more elements in the queue
    while queue:
        # Get the next element (next subset)
        nxt = queue.popleft()

        # Add it to the list of subsets
        answer.append(nxt)

        if nxt == []:
            for letter in letters:
                queue.append([letter])
        else:
            last_char = nxt[-1]
            for letter in letters:
                if letter > last_char:
                    queue.append(nxt + [letter])

    return answer

subsets(['a', 'b'])

'''
Example
letters = [a,b]
queue = [[a,b]]
nxt = [b]
answer = [[], [a], [b], [a, b]]
'''
