# First Missing Positive 
# On the first pass, remove all negative elements and all elements that are 
# greater than len(n) + 1. On the second pass, swap all elements so that they 
# are in the index that equals their value.
# Time: O(n) | Space: O(1)

from typing import List

def firstMissingPositive(nums: List[int]) -> int:

    l = len(nums)

    # Set all negative numbers and numbers higher than l to 0
    for i, n in enumerate(nums):
        if n < 0 or n > l:
            nums[i] = 0

    # Place all numbers in their corresponding indices
    temp, i = 0, 0
    while i < l:
        if nums[i] > 0 and not(nums[i] == i+1):
            temp = nums[nums[i]-1]
            # Check for duplicate numbers
            if temp == nums[i]:
                temp = 0
            nums[nums[i]-1] = nums[i]
            nums[i] = temp
        else:
            i+=1

    # Get the first index containing 0
    for i, n in enumerate(nums):
        if n == 0:
            return i + 1
    return l + 1

test_cases = [  [1, 2, 0],
                [3, 4, -1, 1],
                [7, 8, 9, 11, 12],
                [],
                [2],
                [1, 1]
            ]
expected_solutions = [3, 2, 1, 1, 1, 2]

for i, case in enumerate(test_cases):
    ans = firstMissingPositive(case)
    if ans == expected_solutions[i]:
        print("Passed")
    else:
        print("{0} => {1} expected {2}".format(case, ans, expected_solutions[i]))
