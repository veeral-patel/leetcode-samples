def min_max_weight(weights, d):
    # https://algo.monster/problems/capacity_to_ship_packages
    low = max(weights)
    high = sum(weights)

    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if feasible(weights, d, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    if ans == -1:
        raise Exception("didn't find any suitable capacity")

    return ans

def feasible(weights, days, capacity):
    days_required = 1

    capacity_left = capacity

    for i, weight in enumerate(weights):
        if weight <= capacity_left:
            capacity_left = capacity_left - weight
        else:
            capacity_left = capacity
            capacity_left = capacity_left - weight
            days_required += 1

    return days_required <= days
