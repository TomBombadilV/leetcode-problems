# Remove Duplicates from Sorted Array II
# Walk through list, deleting objects that increase count past 2
# Time: O(n) | Space: O(1)

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    i = 0
    count = 1
    while i < len(nums) - 1:
        # If next number same as curr
        if nums[i] == nums[i + 1]:
            # And we already have 2 in a row
            if count == 2:
                del nums[i + 1]
            # Don't have 2 yet
            else:
                count += 1
                i += 1
        # Numbers are different
        else:
            count = 1
            i += 1
    return len(nums)

# Driver Code
cases = [ ([1, 1, 1, 2, 2, 3], 5),
          ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7),
]
for case in cases:
    l, expected = case
    print(removeDuplicates(l))
    print(l)
