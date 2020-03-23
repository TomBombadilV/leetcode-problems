# Shortest Unsorted Continuous Subarray
# Traverse through array, keeping track of current window and window's min and 
# max
# Time: O(n) | Space: O(1)

from math import inf
from typing import List

def findUnsortedSubarray(nums: List[int]) -> int:
    start, end = len(nums), 0
    sub_min, sub_max = inf, -inf
    for i in range(1, len(nums)):
        # If current number is smaller than previous number
        if nums[i] < nums[i - 1]:
            start = i - 1 if i - 1 < start else start
            end = i
            sub_min = min(nums[i], sub_min)
            sub_max = max(nums[i - 1], sub_max)
        # If current number is smaller than max of subarray
        if nums[i] < sub_max:
            end = i
            sub_min = min(nums[i], sub_min)
        # If a new min is added to the window, backtrack the start index to 
        # include all numbers greater than the new min
        while start > 0 and nums[start - 1] > sub_min:
            start -= 1
    return end - start + 1 if start <= end else 0

"""# Iterate from beginning to find first instance of 
def better_findUnsortedSubarray(nums: List[int]) -> int:
    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            break
        i += 1
    j = len(nums) - 1
    while j > 0:
        if nums[j] < nums[j - 1]:
            break
        j -= 1
    print(i, j)
    return j - i + 1 if i < j else 0"""

cases = [   ([2, 6, 4, 8, 10, 9, 15], 5),
            ([10, 1, 2, 3, 0], 5),
            ([1, 2, 3, 4], 0),
            ([1, 3, 2, 2, 2], 4),
            ([1, 2, 3, 4, 0], 5),
            ([10, 1, 2, 3], 4),
            ([1, 2, 10, 6, 7, 8, 0], 7)
        ]

for c in cases:
    a, s = c
    #res = findUnsortedSubarray(a)
    res = findUnsortedSubarray(a)
    print("Passed" if s == res else "{0} failed {1} expected {2}".format(a, res, s))