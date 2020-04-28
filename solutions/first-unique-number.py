# First Unique Number
# Use an ordered dictionary to keep track of unique insertions
# Time: O(1) | Space: O(n)

from collections import OrderedDict
from typing import List

class FirstUnique:
    def __init__(self, nums: List[int]):
        self.unique = OrderedDict()
        self.q = set()
        for n in nums:
            self.add(n)

    def showFirstUnique(self) -> int: 
        # If there is a number in the unique set
        if len(self.unique) > 0:
            # Return it
            return next(iter(self.unique.items()))[0]
        return -1

    def add(self, value: int) -> None:
        # If number already exists in queue
        if value in self.q:
            # Delete it from unique set
            if value in self.unique:
                del self.unique[value]
        # If new, add to queue and unique set
        else:
            self.q.add(value)
            self.unique[value] = True

if __name__ == "__main__":
    fu = FirstUnique([7, 7, 7])
    print(fu.showFirstUnique())
    fu.add(5)
    print(fu.showFirstUnique())
    fu.add(2)
    print(fu.showFirstUnique())
    fu.add(5)
    print(fu.showFirstUnique())
