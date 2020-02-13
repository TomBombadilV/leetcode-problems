# Combination Sum
# Recursions and such
# Time: O(n^k) | Space: O(n*k) (???)

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    return recurse(sorted(candidates), [], target, [])

def recurse(candidates: List[int], curr_list: int, target: int, solutions: List[int]) -> List[List[int]]:
    for i, c in enumerate(candidates):
        if sum(curr_list) + c == target:
            solutions.append(curr_list + [c])
        elif sum(curr_list) + c < target:
            recurse(candidates[i:], curr_list + [c], target, solutions)
        # if sum(curr_list) + c > target, ignore it
    return solutions

test_cases = [  ([2, 3, 6, 7], 7),
                ([2, 3, 5], 8),
                ([], 5)
            ]
for case in test_cases:
    candidates, target = case
    print(combinationSum(candidates, target))