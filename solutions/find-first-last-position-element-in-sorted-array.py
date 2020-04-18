# Find First and Last Position of Element in Sorted Array
# Modified binary search. For the second pass, you only need to look at nums[indices[0]] and on
# Time: O(logn) | Space: O(1)

from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    indices = [-1, -1]
    # First pass to find the left side
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and (mid==0 or nums[mid] > nums[mid - 1]):
            indices[0] = mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    # Only need to search from the first index and on
    offset = indices[0]
    nums = nums[offset:]
    # Second psas to find the right side
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target and (mid==len(nums)-1 or nums[mid] < nums[mid + 1]):
            indices[1] = mid + offset
        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1
    return indices

test_cases = [  ([5, 7, 7, 8, 8, 10], 8),
                ([5, 7, 7, 8, 8, 10], 6),
                ([1, 1, 1, 1, 1, 1], 1),
                ([10], 10),
                ([1, 2, 3, 4, 5, 6], 1),
                ([1, 2, 3, 4, 5, 6], 2),
                ([1, 2, 3, 4, 5, 6], 6),
                ([], 0)
            ]
expected_output = [ [3, 4],
                    [-1, -1],
                    [0, 5],
                    [0, 0],
                    [0, 0],
                    [1, 1],
                    [5, 5],
                    [-1, -1]
                ]

for i, case in enumerate(test_cases):
    nums, target = case
    ans = searchRange(nums, target)
    if ans == expected_output[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(case, ans, expected_output[i]))