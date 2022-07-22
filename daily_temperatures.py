def daily_temperatures(temperatures):
    answer = [0]*len(temperatures) # remember to initialize!
    stack = []

    for currentIndex, temp in enumerate(temperatures):
        while stack and stack[-1] < temp:
            index = stack.pop()
            answer[index] = currentIndex - index

        stack.append(currentIndex)

    return answer
