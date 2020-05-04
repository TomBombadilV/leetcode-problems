# Min Stack
# Implementation with tuples of value and current min

from math import inf

class MinStack:
    
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        curr_min = self.getMin()
        if curr_min == None or x < curr_min:
            curr_min = x
        self.stack.append((x, curr_min))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
