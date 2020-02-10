# Subsets

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    solution = [[]]
    for _ in range(len(nums)):
        solution = [ a + [b] for a in solution for b in nums]
    return solution

case = [1, 2, 3]
print(subsets(case))