# Best Time to Buy and Sell Stock
# Whenever the prices increases from one day to the next, add to profit.
# Time: O(n) | Space: O(1)

def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    for i in range(1, len(prices)):
        # If price is higher than yesterday, add increase to profit
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]
    return profit
