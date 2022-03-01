output = [[[".","Q",".","."],[".",".",".","Q"],["Q",".",".","."],[".",".","Q","."]],[[".",".","Q","."],["Q",".",".","."],[".",".",".","Q"],[".","Q",".","."]]]

results = []
for board in output:
    strings = []
    for row in board:
        strings.append("".join(row))
    results.append(strings)

print(results)
