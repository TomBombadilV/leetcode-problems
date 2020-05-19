# Online Stock Span

class StockSpanner:
    
    def __init__(self):
        self.stack = []
        self.count = 0

    def next(self, price: int) -> int:
        self.count += 1
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        span = self.count - self.stack[-1][1] if self.stack else self.count
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
