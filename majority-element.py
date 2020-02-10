# Majority Element
# Count up the elements until you've reached one that exists more than n//1 times
# Time: O(n) | Space: O(n)

from typing import List
from collections import defaultdict

def majorityElement(nums: List[int]) -> int:
    l = len(nums) // 2
    d = defaultdict(int)
    for n in nums:
        d[n] += 1
        if d[n] > l:
            return n

print(majorityElement([2, 2, 1, 1, 1, 2, 2]))