# Majority Element
# Method 1: 
# Count up the elements until you've reached one that exists more than n//1 times
# Time: O(n) | Space: O(n)
# Method 2:
# Use Boyer & Moore majority vote algorithm
# Time: O(n) | Space: O(1)

from typing import List
from collections import defaultdict

def majorityElement(nums: List[int]) -> int:
    """
    Method 1
    """
    # Minimum count of a majority element is n // 2 + 1
    floor = len(nums) // 2
    # Iterate through list, keeping all counts in a dictionary. Once minimum
    # majority count is hit, return
    count = defaultdict(int)
    for n in nums:
        count[n] += 1
        if count[n] > floor:
            return n

def majorityElement(nums: List[int]) -> int:
    """
    Method 2
    """
    # Keep track of current majority and its count
    maj, count = None, 0
    for n in nums:
        # If count is 0, reset majority to current number
        maj = n if count == 0 else maj
        # Increment count if current number is same as majority. Decrement if not
        count = count + 1 if n == maj else count - 1
    return maj

print(majorityElement([2, 2, 1, 1, 1, 2, 2]))
