# Min Stack
# First implementation

from math import inf

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.stack_min = inf

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.stack_min = min(self.stack_min, x)

    def pop(self) -> None:
        n = self.stack.pop()
        if self.stack_min == n:
            if self.stack:
                self.stack_min = min(self.stack)
            else:
                self.stack_min = None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())