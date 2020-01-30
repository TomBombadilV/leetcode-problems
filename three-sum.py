# 3Sum
# Put all pairs of numbers into a dictionary with their sum as the key. Then
# pass over the list again and search if its negation is in the dictionary
# Time: O(n^2) | Space: O(n)
# Solution times out

from typing import List
from collections import defaultdict

def threeSum(nums: List[int]) -> List[List[int]]:
    solution = set()
    sum_dict = defaultdict(list)
    # Get all non-duplicate pairs
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            # Save the numbers and their indices with their sum as they key
            sum_dict[nums[i] + nums[j]].append([nums[i], nums[j], (i, j)])
    for i in range(len(nums)):
        num = nums[i]
        # Get the number that would sum this number to 0
        negator = -1 * num
        # If that sum exists, save the triple
        if negator in sum_dict:
            for pair in sum_dict[negator]:
                # Check to make sure the number is not already used
                if not(i in pair[2]):
                    solution.add(tuple(sorted([num, pair[0], pair[1]])))
    solution = [[a, b, c] for (a, b, c) in solution]
    return solution

print(threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]))