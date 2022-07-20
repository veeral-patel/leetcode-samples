def knapsack_weight_only(weights):
    if len(weights) == 0:
        return [0]
    elif len(weights) == 1:
        return [0, weights[0]]
    else:
        first = weights[0]

        answer_for_remaining = knapsack_weight_only(weights[1:])

        ans = []

        for num in answer_for_remaining:
            ans.append(num)
            ans.append(first + num)

        return list(set(ans))
