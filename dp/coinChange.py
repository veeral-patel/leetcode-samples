from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1
        elif min(coins) > amount:
            return 0
        else:
            count = 0
            largest = max(coins)
            rest = [coin for coin in coins if coin != largest]
            largestUsed = amount // largest
            amountLeft = amount % largest
            count += largestUsed
            if amountLeft == 0:
                return count
            else:
                moreCoinsNeeded = self.coinChange(rest, amountLeft)
                if moreCoinsNeeded == -1:
                    return -1
                else:
                    count += moreCoinsNeeded
                    return count
