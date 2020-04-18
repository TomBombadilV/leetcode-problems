# Coin Change
# For 1 through amount, check for the min if you use each possible coin
# Time: O(amount) | Space: O(amount)

from math import inf

from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    res = [0] + [inf] * amount
    for coin in coins:
        for i in range(coin, amount + 1):
                res[i] = min(1 + res[i - coin], res[i])
    return -1 if res[amount] == inf else res[amount]

cases = [
    ([1, 2, 5], 11, 3),
    ([1, 2, 5], 10, 3),
    ([2], 3, -1),
    ([3], 5, -1),
    ([3], 9, -1)
]
for case in cases:
    coins, amount, ans = case
    print(coinChange(coins, amount))