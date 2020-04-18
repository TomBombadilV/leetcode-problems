# Min stack re-implementation practice for 30 days of coding

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        m = self.getMin() if self.stack and self.getMin() < x else x
        self.stack.append((x, m))

    def pop(self) -> int:
        return self.stack.pop()[0] if self.stack else None

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

# Driver code
m = MinStack()
m.push(-2)
m.push(0)
m.push(-3)
m.getMin()
m.pop()
m.top()
m.getMin()
