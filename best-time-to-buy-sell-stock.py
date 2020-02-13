# Best Time to Buy and Sell Stock
# Find the minimum price at that point and the maximum profit at that point
# Time: O(n) | Space: O(1)

from typing import List
import sys

def maxProfit(prices: List[int]) -> int:
    min_price, max_profit = sys.maxsize, 0
    for price in prices:
        min_price = min(min_price, price)
        curr_profit = price - min_price
        max_profit = max(max_profit, curr_profit)
    return max_profit

test_cases = [  [7, 1, 5, 3, 6, 4],
                [7, 6, 4, 3, 1],
                [1, 2]
            ]
for case in test_cases:
    print("{0} => {1}".format(case, maxProfit(case)))