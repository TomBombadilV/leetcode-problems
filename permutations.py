# Permutations

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    return recurse(nums, [[]])

def recurse(nums: List[int], solutions: List[List[int]]) -> List[List[int]]:
    print(solutions, nums)
    for i, n in enumerate(nums):
        for s in solutions:
            solutions.append(s + [n])
        recurse(nums[:i ] + nums[i + 1:], solutions)
    return solutions

for i in range(2,3):
    nums = [j for j in range(i)]
    print(nums)
    print(permute(nums))