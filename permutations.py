# Permutations
# Using recursion, add each number to existing solutions and pass on a new list 
# without that number
# Time: O(n*n!) | Space: O(n*n!)

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    return recurse(nums, [[]])

def recurse(nums: List[int], solutions: List[List[int]]) -> List[List[int]]:
    if not(nums):
        return solutions
    new_sols = []
    # For each number in nums (which shrinks by 1 with each call), add n to all solutions
    for i, n in enumerate(nums):
        sols = [s + [n] for s in solutions]
        # Recurse with nums minus n
        new_sols = new_sols + recurse(nums[:i ] + nums[i + 1:], sols)
    return new_sols

for i in range(4):
    nums = [j+1 for j in range(i)]
    print(permute(nums))