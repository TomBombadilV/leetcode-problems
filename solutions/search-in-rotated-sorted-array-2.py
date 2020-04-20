# Search in Rotated Sorted Array
# Method 1:
# Binary search to find rotation point. Recreate array. Binary search to find
# target value
# Method 2: 
# Binary search. Check if target is in sorted part of array or not
# Time: O(logn) | Space: O(1)

from typing import List

# Method 1
def search(nums: List[int], target: int) -> int:
    # Find rotation point
    left, right = 0, len(nums) - 1
    rot = -1 
    while left <= right:
        mid = (right + left) // 2
        # If number to the right of mid is smaller than mid, that's the 
        # rotation point
        if mid + 1 < len(nums) and nums[mid + 1] < nums[mid]:
            rot = mid + 1
            break
        if nums[mid] >= nums[left]:
            left = mid + 1
        else: 
            right = mid - 1

    # Modify the array
    if rot > -1:
        nums = nums[rot:] + nums[:rot]
    # If rot == -1, the array was already sorted
    else:
        rot = 0
   
    # Regular binary search to find the target
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right + left) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            # If target found, return index plus offset to get original index
            return (mid + rot) % len(nums)
    return -1

# Method 2
def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    # Make sure left and right don't cross'
    while left <= right:
        mid = (left + right) // 2
        # Check mid against target
        if nums[mid] == target:
            return mid
        # If left side of array is sorted
        if nums[mid] >= nums[left]:
            # Check if target is in sorted part
            if target >= nums[left] and target < nums[mid]:
                right = mid - 1
            # Or else look on the other side
            else:
                left = mid + 1
        # If right side of array is sorted
        else:
            # Check if target is in sorted part
            if target > nums[mid] and target <= nums[right]:
                left = mid + 1
            # Or else look on the other side
            else:
                right = mid - 1
    return -1

# Driver code
cases = [   [1, 2, 3, 4, 5],
            [2, 3, 4, 5, 1],
            [3, 4, 5, 1, 2],
            [4, 5, 1, 2, 3],
            [5, 1, 2, 3, 4],
            [1],
            [1, 5],
            [5, 1]
]

for case in cases:
    print(search(case, 1))
