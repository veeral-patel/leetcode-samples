from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda interval: interval[0])

    merged = []

    for interval in intervals:
        if merged:
            last = merged[-1]
            if do_overlap(last, interval):
                merged[-1] = do_merge(last, interval)
            else:
                merged.append(interval)
        else:
            merged.append(interval)

    return merged

def do_overlap(intvl1, intvl2):
    return intvl2[0] <= intvl1[1]

def do_merge(intvl1, intvl2):
    return [min(intvl1[0], intvl2[0]), max(intvl1[1], intvl2[1])]
