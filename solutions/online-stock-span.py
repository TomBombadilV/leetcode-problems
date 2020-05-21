# Online Stock Span
# For each price added to stock spanner, preserve its index and remove previous 
# prices that are smaller until you encounter a price that is bigger.
# Time: O(n) | Space: O(n)

class StockSpanner:
    
    def __init__(self):
        self.stack = []
        self.count = 0

    def next(self, price: int) -> int:
        # Current index
        self.count += 1

        # Remove all prices from top of stack that are smaller than current price
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()

        # Span is distance between current price index and top of stack which is 
        # the first number bigger than current price
        span = self.count - self.stack[-1][1] if self.stack else self.count
        
        # Add current price and index to stack
        self.stack.append((price, self.count))

        return span 

# Driver Code
ss = StockSpanner()
l = [100, 80, 60, 70, 60, 75, 85]
for n in l:
    print(ss.next(n))

ss = StockSpanner()
l = [31, 41, 48, 59, 79]
for n in l:
    print(ss.next(n))

ss = StockSpanner()
l = [28, 14, 28, 35, 46, 53, 66, 80, 87, 88]
for n in l:
    print(ss.next(n))
