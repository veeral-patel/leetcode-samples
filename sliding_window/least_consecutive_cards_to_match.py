"""
A bunch of cards is laid out in front of you in a line, where the value of each card ranges from 0 to 10^6. A pair of cards are matching if they have the same number value.

Given a list of integer cards, your goal is to match a pair of cards, but you can only pick up cards in a consecutive manner. What's the minimum number of cards that you need to pick up to make a pair? If there is no matching pairs, return -1.

For example, given cards = [3, 4, 2, 3, 4, 7], then picking up [3, 4, 2, 3] makes a pair of 3s and picking up [4, 2, 3, 4] matches two 4s. We need 4 consecutive cards to match a pair of 3s and 4 consecutive cards to match 4s, so you need to pick up at least 4 cards to make a match.
"""

from typing import List
from collections import Counter

def least_consecutive_cards_to_match(cards: List[int]) -> int:
    left, right = 0, 1
    ans = float("inf")
    
    while right <= len(cards):
        window = cards[left:right]
        if has_pair(window):
            ans = min(ans, len(window))
            left += 1
        else:
            right += 1
   
    return ans if ans != float("inf") else -1

def has_pair(arr: List[int]) -> bool:
    counter = Counter(arr)
    for k, v in counter.items():
        if v == 2: # found a pair
            return True
    return False
