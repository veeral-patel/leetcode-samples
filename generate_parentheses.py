from collections import deque

def generate_parentheses(n):
    queue = deque()
    answer = []

    queue.append("")

    while queue:
        nxt = queue.popleft()
        open_count, closed_count = get_counts(nxt)
        if open_count == n and closed_count == n:
            answer.append(nxt)
        elif open_count == n: # need to close
            queue.append(nxt+")")
        else:
            queue.append(nxt+"(")
            if closed_count < open_count:
                queue.append(nxt+")")

    return answer

def get_counts(s):
    openCount = len([c for c in s if c == '('])
    closedCount = len([c for c in s if c == ')'])
    return openCount, closedCount
