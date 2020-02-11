# Best Time to Buy and Sell Stock
# Keep calculating the maximum increase, save the max
# Time: O(n) | Space: O(1)

from typing import List

def maxProfit(prices: List[int]) -> int:
    total_profit = 0
    max_profit = 0
    for i in range(1, len(prices)):
        diff = prices[i] - prices[i-1]
        if total_profit + diff <= 0:
            total_profit = 0
        else:
            total_profit += diff
        max_profit = max(max_profit, total_profit)
    return max_profit

test_cases = [  [7, 1, 5, 3, 6, 4],
                [7, 6, 4, 3, 1],
                [1, 2]
            ]
for case in test_cases:
    print("{0} => {1}".format(case, maxProfit(case)))