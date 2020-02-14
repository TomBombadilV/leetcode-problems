# Subsets

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    solution = [[]]
    for n in nums:
        solution += [s + [n] for s in solution]
    return solution

for i in range(3,4):
    nums = [j + 1 for j in range(i)]
    print(subsets(nums))