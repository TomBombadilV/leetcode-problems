# Single Element in a Sorted Array
# Modified binary search
# 1. Length of nums will always be odd
# 2. Single number must always be in even index
# Time: O(logn) | Space: O(1)

from test import test
from typing import List

def singleNonDuplicate(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if mid % 2 == 0:  # mid is even
            if mid >= len(nums) - 1 or mid == 0:
                return nums[mid]
            if nums[mid] == nums[mid + 1]:
                left = mid + 2
            elif nums[mid] == nums[mid - 1]:
                right = mid - 2
            else:
                return nums[mid]
        else:  # mid is odd
            # odd number index can't be single number
            if nums[mid] == nums[mid + 1]:
                right = mid - 1
            else:
                left = mid + 1
    return -1

"""def singleNonDuplicate(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1 
    while left <= right:
        mid = (left + right) // 2
        if mid % 2 == 0 and nums[mid] == nums[mid + 1] or\
           mid % 2 == 1 and nums[mid] == nums[mid - 1]:
            left = mid + 1
        elif mid % 2 == 0 and nums[mid] == nums[mid - 1] or\
             mid % 2 == 1 and nums[mid] == nums[mid + 1]:
            right = mid - 1
        else:
            return nums[mid]
    return -1"""

# Driver Code
cases = [([1,2,2,3,3,4,4,5,5], 1),
         ([1,1,2,3,3,4,4,5,5], 2),
         ([1,1,2,2,3,4,4,5,5], 3),
         ([1,1,2,2,3,3,4,5,5], 4),
         ([1,1,2,2,3,3,4,4,5], 5),
         ([1], 1)
]
test(singleNonDuplicate, cases)
