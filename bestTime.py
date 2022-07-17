def bestTime(prices):
    # Best time to buy/sell stock
    # Ideas
    # DP
    # Double for loop
    # Min price/max profit
    minPrice = float("inf")
    maxProfit = 0
    for price in prices:
        maxProfit = max(maxProfit, price-minPrice)
        minPrice = min(minPrice, price)
    return maxProfit
