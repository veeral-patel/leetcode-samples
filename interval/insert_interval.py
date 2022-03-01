def insert_interval(intervals, new_interval):
    merged = []

    i = 0

    # Add all the intervals which end before new_interval
    # begins (non-overlapping)
    while i <= len(intervals)-1 and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1

    # Merge and add our overlaping intervals
    start, end = float("inf"), float("-inf")
    while i <= len(intervals)-1 and new_interval[1] >= intervals[i][0]:
        start = min(start, intervals[i][0], new_interval[0])
        end = max(end, intervals[i][1], new_interval[1])
        i += 1

    if start != float("inf"):
        merged.append([start, end])
    else:
        merged.append(new_interval)

    # Add all the intervals which start after new_interval
    # ends (non-overlapping)
    while i <= len(intervals)-1:
        merged.append(intervals[i])
        i += 1

    return merged
