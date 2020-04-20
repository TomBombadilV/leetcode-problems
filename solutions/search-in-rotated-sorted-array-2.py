# Search in Rotated Sorted Array
# Method 1:
# Binary search to find rotation point. Recreate array. Binary search to find
# target value
# Method 2: 
# 

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
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] >= nums[left]:
            if target >= nums[left] and target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if target >= nums[mid] and target <= nums[right]:
                left = mid + 1
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

#search(cases[3], None)
