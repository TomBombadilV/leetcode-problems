# Search Insert Position
# Modify binary search to check if target is between mid and mid's left to find
# insertion point. Handle special case where target is greater than last num
# in list.
# Time: O(logn) | Space: O(1)

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    # If target is larger than largest num, insert in new end position
    if target > nums[-1]:
        return len(nums)
    # Binary search
    left, right = 0, len(nums) - 1 
    while left <= right:
        mid = (left + right) // 2
        # Target found
        if nums[mid] == target:
            return mid
        # Target is before beginning of list or target is between mid and mid-1
        if nums[mid] > target and (mid == 0 or nums[mid - 1] < target):
            return mid
        # If target is before mid
        if nums[mid] > target:
            right = mid - 1
        # If target is after mid
        else:
            left = mid + 1

# Driver code
cases = [   ([1, 3, 5, 6], 5),
            ([1, 3, 5, 6], 2),
            ([1, 3, 5, 6], 7),
            ([1, 3, 5, 6], 0)
]
for case in cases:
    print(searchInsert(case[0], case[1]))
