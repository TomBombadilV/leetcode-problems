# Search in Rotated Sorted Array
# Perform binary search to find the rotation point O(logn). Re-form the array 
# in sorted order O(1), then perform binary search again to find the target 
# value
# Time: O(logn) | Space: O(1)

from typing import List

def search(nums: List[int], target: int) -> int:
    # Find point of rotation with modified binary search
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    # Re-create array
    nums = nums[left:] + nums[:left]
    offset = left

    # Search array
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return (mid + offset) % len(nums)
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

test_cases = [  ([4, 5, 6, 7, 0, 1, 2], 0),
                ([4, 5, 6, 7, 0, 1, 2], 3),
                ([], 0),
                ([6, 7, 0, 1, 2, 3, 4], 4)
            ]

for case in test_cases:
    print("Target: {0}, Nums: {1} => {2}".format(case[1], case[0], search(case[0], case[1])))