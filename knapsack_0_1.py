import math

def knapsack(weights, values, max_weight):
    if not weights or not values:
        return 0
    elif max_weight <= 0:
        return 0

    without_first = knapsack(weights[1:], values[1:], max_weight)

    if max_weight >= weights[0]:
        with_first = values[0] + knapsack(weights[1:], values[1:], max_weight-weights[0])
    else:
        with_first = -math.inf

    return max(without_first, with_first)
